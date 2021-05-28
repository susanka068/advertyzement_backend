from models import engine , db_session , Base , Banks , Branches 
import glob
import os
import pandas as pd
from sqlalchemy import text

Base.metadata.create_all(bind = engine)




# banks = db_session.query(Banks).all()

# for bank in banks:
#     print(bank.name)

def create_banks():
	bank_data = pd.read_csv('banks.csv')

	for ind in bank_data.index:
		bank_row = Banks(name = bank_data['name'][ind] , id = bank_data['id'][ind]  )
		db_session.add(bank_row)



def create_branches():

	branches_data = pd.read_csv('bank_branches.csv')

	for ind in branches_data.index:
		ifsc = branches_data['ifsc'][ind] 
		bank_id = branches_data['bank_id'][ind] 
		branch = branches_data['branch'][ind] 
		address = branches_data['address'][ind] 
		city=branches_data['city'][ind] 
		district=branches_data['district'][ind] 
		state=branches_data['state'][ind]
		# print(f"{ifsc} , {bank_id} , {branch} , {address} , {branch} , {address} , {city} , {district} , {state} ")
		branch_row = Branches(ifsc = ifsc , bank_id = bank_id , branch = branch , address = address , city=city , district=district , state=state )
		db_session.add(branch_row)


create_banks()
create_branches()

db_session.commit()

print("inserted data in db session")
