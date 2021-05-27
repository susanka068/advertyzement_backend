from models import Banks , Branches , db_session

banks = db_session.query(Banks).all()


for bank in banks:
    print(bank.name)

