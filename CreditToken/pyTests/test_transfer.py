from ape import accounts, project
import pytest
from ape.exceptions import ContractLogicError

@pytest.fixture
def credit():
    admin = accounts.test_accounts[0]
    contract = project.Credit.deploy(int(18e9),sender=admin)
    return admin,contract

@pytest.mark.parametrize("amount",[0,int(1e18),int(2e18)])
def test_transfer_fail(credit,amount):
    admin,contract = credit
    user1 = accounts.test_accounts[1]
    user2 = accounts.test_accounts[2]

    if amount == 0:
        # user1 has 0 balance
        with pytest.raises(ContractLogicError) as e:
            contract.transfer(user2, amount, sender=user1)
        assert e.value.__class__.__name__ == "AmountZero"

    elif amount > contract.getBalance(sender=user1):
        with pytest.raises(ContractLogicError) as e:
            contract.transfer(user2, amount, sender=user1)
        assert e.value.__class__.__name__ == "InsufficientBalance"

    else:
        contract.transfer(user2, amount, sender=user1)
        

