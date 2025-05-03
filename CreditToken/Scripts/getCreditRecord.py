from ape import project,accounts

def main():

    admin = accounts.test_accounts[0]
    user1 = accounts.test_accounts[1]
    

    main = project.Credit.at(0x5FbDB2315678afecb367f032d93F642f64180aa3)
    
    print(main.getCreditRecord(user1,sender=admin))