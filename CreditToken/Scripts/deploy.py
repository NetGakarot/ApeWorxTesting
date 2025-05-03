from ape import project,accounts

def main():

    admin = accounts.test_accounts[0]

    contract = project.Credit.deploy(18000000,sender=admin)

    main = project.Credit.at(contract.address)

    print(f"✅ Contract deployed at ---> {main.address}")
    print(f"Project Name ----> {main.name()}")
    print(f"Project Symbol ----> {main.symbol()}")
    print(f"Project Total Supply ----> {main.totalSupply()}")
    print(f"Project owner ----> {main.owner()}")