from ape import project,accounts

def main():

    admin = accounts.test_accounts[0]
    user1 = accounts.test_accounts[1]
    user2 = accounts.test_accounts[2]
    user3 = accounts.test_accounts[3]
    user4 = accounts.test_accounts[4]


    main = project.Credit.at(0x5FbDB2315678afecb367f032d93F642f64180aa3)

    print("Balance before")
    print(f"Balance of admin is ----> {main.getBalance(sender=admin)}")
    print(f"Balance of user1 is ----> {main.getBalance(sender=user1)}")
    print(f"Balance of user2 is ----> {main.getBalance(sender=user2)}")
    print(f"Balance of user3 is ----> {main.getBalance(sender=user3)}")
    print(f"Balance of user4 is ----> {main.getBalance(sender=user4)}")

    main.transferFrom(admin,user4,int(1e18),sender=user1)
    main.transferFrom(user1,user4,int(1e18),sender=user2)
    main.transferFrom(user2,user4,int(1e18),sender=user3)

    print(f"Admin approved amount to {user1} is ----> {main.getAllowances(user1,sender=admin)}")
    print(f"User1 approved amount to {user2} is  ----> {main.getAllowances(user2,sender=user1)}")
    print(f"User2 approved amount to {user3} is ----> {main.getAllowances(user3,sender=user2)}")

    print(100 * "*")

    print("Balance after")
    print(f"Balance of admin is ----> {main.getBalance(sender=admin)}")
    print(f"Balance of user1 is ----> {main.getBalance(sender=user1)}")
    print(f"Balance of user2 is ----> {main.getBalance(sender=user2)}")
    print(f"Balance of user3 is ----> {main.getBalance(sender=user3)}")
    print(f"Balance of user4 is ----> {main.getBalance(sender=user4)}")