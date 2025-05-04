from ape import accounts, project
import pytest
from pytest import approx
from ape.exceptions import ContractLogicError

@pytest.fixture
def credit():
    admin = accounts.test_accounts[0]
    contract = project.Credit.deploy(int(18e9),sender=admin)
    return admin,contract

def test_transfer(credit):
    admin,contract = credit
    user1 = accounts.test_accounts[1]
    contract.transfer(user1, int(2e18), sender=admin)
    assert contract.getBalance(sender=user1) == int(2e18)

def test_approve(credit):
    admin,contract = credit
    user1 = accounts.test_accounts[1]
    contract.approve(user1, int(2e18),sender=admin)
    assert contract.getAllowances(user1,sender=admin) == int(2e18)

    contract.decreaseAllowance(user1, int(2e18), sender=admin)
    assert contract.getAllowances(user1,sender=admin) == 0

def test_transferFrom(credit):
    admin,contract = credit
    user1 = accounts.test_accounts[1]
    user2 = accounts.test_accounts[2]
    contract.approve(user1,int(2e18),sender=admin)
    assert contract.getAllowances(user1,sender=admin) == int(2e18)


    contract.transferFrom(admin,user2,int(1e18),sender=user1)
    assert contract.getBalance(sender=user2) == int(1e18)

def test_fail_mintBurn(credit):
    admin,contract = credit
    contract.mint(int(1e27),sender=admin)
    assert contract.totalSupply() == approx(int(19e27), rel=1e-6)

    contract.burn(int(1e27),sender=admin)
    assert contract.totalSupply() == approx(int(18e27), rel=1e-6)

def test_fail_transfer(credit):
    admin,contract = credit
    user1 = accounts.test_accounts[1]
    user2 = accounts.test_accounts[2]
    with pytest.raises(ContractLogicError) as e:
        contract.transfer(user2,int(1e18),sender=user1)
        assert "InsufficientBalance" in str(e.value)