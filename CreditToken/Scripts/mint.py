from ape import project,accounts

def main():

    admin = accounts.test_accounts[0]

    main = project.Credit.at(0x5FbDB2315678afecb367f032d93F642f64180aa3)

    print(f"Old balance of owner is ----> {main.getBalance(sender=admin)} ")
    print(f"Project Total Supply ----> {main.totalSupply()}")

    main.mint(11000000000000000000000000,sender=admin)

    print(f"New balance of owner is ----> {main.getBalance(sender=admin)} ")
    print(f"Project Total Supply ----> {main.totalSupply()}")