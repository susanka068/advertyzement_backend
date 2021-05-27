from models import engine , db_session , Base , Banks , Branches 
Base.metadata.create_all(bind = engine) 

bank1 = Banks(name="STATE BANK OF INDIA	1", id =1 )
bank2 = Banks(name="PUNJAB NATIONAL BANK", id =2 )
bank3 = Banks(name="CANARA BANK", id =3 )

db_session.add(bank1)
db_session.add(bank2)
db_session.add(bank3)

branch1 = Branches(ifsc = "SBIN0018402" , bank_id = 1 , branch = "KONGANAPURAM" , address = "MORAMBUKADU, OMALUR MAIN ROAD, KONGANAPURAM, DIST. SALEM, TAMIL NADU - 637102" , city="SALEM" , district="SALEM" , state="TAMIL NADU" )


db_session.add(branch1)
db_session.commit()
print("inserted data in db session")


banks = db_session.query(Banks).all()

for bank in banks:
    print(bank.name)
