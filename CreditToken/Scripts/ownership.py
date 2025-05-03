from ape import project,accounts

def main():

    
    newAdmin = accounts.test_accounts[9]
    admin = accounts.test_accounts[0]

    main = project.Credit.at(0x5FbDB2315678afecb367f032d93F642f64180aa3)

    main.transferOwnership(admin,sender=newAdmin)

    print(f"New owner is ---> {main.owner()}")

