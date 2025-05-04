from ape import project,accounts
from hypothesis import given ,strategies as st
from ape.exceptions import ContractLogicError
import pytest

@given(amount=st.integers(min_value=0,max_value=int(2e18)))
def test_transfer(amount):
    admin = accounts.test_accounts[0]
    user1 = accounts.test_accounts[1]
    contract = project.Credit.deploy(180000000,sender=admin)

    if amount==0:
        with pytest.raises(ContractLogicError) as e:
            contract.transfer(user1,amount,sender=admin)
            assert "AmountZero" in str(e.value)

    elif amount > contract.getBalance(sender=admin):
        with pytest.raises(ContractLogicError) as e:
            contract.transfer(user1,amount,sender=admin)
            assert "InsufficientBalance" in str(e.value)

    else:
        contract.transfer(user1,amount,sender=admin)
        assert contract.getBalance(sender=user1) == amount