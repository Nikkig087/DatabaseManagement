
#### Initial ORM Setup ####
from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer" #matches the class name
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Progammer table
#ada_lovelace = Programmer(
#    first_name="Ada",
#    last_name="Lovelace",
#    gender="F",
#    nationality="British",
#    famous_for="First Programmer"
#)

#alan_turing = Programmer(
#    first_name="Alan",
#    last_name="Turing",
#    gender="M",
#    nationality="British",
#    famous_for="Modern Computing"
#)

#grace_hopper = Programmer(
#    first_name="Grace",
#    last_name="Hopper",
#    gender="F",
#    nationality="American",
#    famous_for="COBOL language"
#)

#margaret_hamilton = Programmer(
#    first_name="Margaret",
#    last_name="Hamilton",
#    gender="F",
#    nationality="American",
#    famous_for="Apollo 11"
#)

#bill_gates = Programmer(
#    first_name="Bill",
#    last_name="Gates",
#    gender="M",
#    nationality="American",
#    famous_for="Microsoft"
#)

#tim_berners_lee = Programmer(
#    first_name="Tim",
#    last_name="Berners-Lee",
#    gender="M",
#    nationality="British",
#    famous_for="World Wide Web"
#)

# add each instance of our programmers to our session
#session.add(ada_lovelace) #like github where we git add
#session.add(alan_turing)
#session.add(grace_hopper)
#session.add(margaret_hamilton)
#session.add(bill_gates)
#session.add(tim_berners_lee)

# updating a single record
#programmer = session.query(Programmer).filter_by(id=7).first() #first method gives us one specific query 
#programmer.last_name = "Getsee" # this is col we are updating



# commit our session to the database
#session.commit() #like github where we commit



# updating multiple records this is the U
# people = session.query(Programmer) # all records on programmer table
#for person in people: #for each person in the people groupp
#     if person.gender == "F":
#         person.gender = "Female" # we want to update gender to female
#     elif person.gender == "M":
#         person.gender = "Male" # we want to update gender to male
#     else:
#         print("Gender not defined")
#     session.commit()


# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first() # this is querying the programmer table using the input information above
# defensive programming, we want to make sure its the right programmer
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ") # the ans is sent to a new varible confirmation
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#    print("No records found")


# delete multiple/all records
# programmers = session.query(Programmer) #find all records in the programmer table
# for programmer in programmers: # for each programmer in the programmer table
#     session.delete(programmer)
#     session.commit()

def update_all_primary_keys():
    # Fetch all records
    programmers = session.query(Programmer).all()
    
    # Update each primary key
    new_id = 1
    for programmer in programmers:
        programmer.id = new_id
        new_id += 1

    # Commit the changes
    session.commit()
    print("All primary keys have been updated successfully!")

# Example usage
try:
    update_all_primary_keys()
except Exception as e:
    print(f"An error occurred: {e}")
    session.rollback()


# query the database to find all Programmers, this is the R in CRUD
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )