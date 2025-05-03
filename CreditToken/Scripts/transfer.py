from ape import project,accounts

def main():

    admin = accounts.test_accounts[0]
    users = accounts.test_accounts[1:7]

    main = project.Credit.at(0x5FbDB2315678afecb367f032d93F642f64180aa3)
    print(f"Balance of owner before transfer ----> {admin.balance}")
    
    for user in users:
        main.transfer(user,int(8),sender=admin)

    print(f"Balance of owner after transfer ----> {admin.balance}")
    for user in users:
        print(f"Balance of {user} ----> {main.getAnyonesBalance(user,sender=admin)}")