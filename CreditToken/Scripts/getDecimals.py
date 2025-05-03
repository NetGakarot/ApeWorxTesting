from ape import project,accounts

def main():

    main = project.Credit.at(0x5FbDB2315678afecb367f032d93F642f64180aa3)

    print(f"Decimal places of token is ----> {main.getdecimals()}")