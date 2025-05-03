from ape import project,accounts

def main():

    admin = accounts.test_accounts[0]
    user1 = accounts.test_accounts[1]
    user2 = accounts.test_accounts[2]
    user3 = accounts.test_accounts[3]

    main = project.Credit.at(0x5FbDB2315678afecb367f032d93F642f64180aa3)

    main.approve(user1,int(1e18),sender=admin)
    main.approve(user2,int(9e18),sender=user1)
    main.approve(user3,int(9e18),sender=user2)

    print(f"Admin approved amount to {user1} is ----> {main.getAllowances(user1,sender=admin)}")
    print(f"User1 approved amount to {user2} is  ----> {main.getAllowances(user2,sender=user1)}")
    print(f"User2 approved amount to {user3} is ----> {main.getAllowances(user3,sender=user2)}")