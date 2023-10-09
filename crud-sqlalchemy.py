# CRUD using "sqlalchemy" ORM 
##############################

from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Shopping" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# Make instances of programmer based on model

ada_lovelace = Programmer(first_name = "Ada",
    last_name = "Lovelace",
    nationality = "UK",
    famous_for = "first_name")

grace_hopper = Programmer(first_name = "Grace",
    last_name = "Hopper",
    nationality = "US",
    famous_for = "COBOL language")

# Add (CREATE) instances to session individually
session.add(ada_lovelace)
session.add(grace_hopper)

# Commit all together
session.commit()

# READ all rows from "Programmer" table
results = session.query(Programmer)

for result in results:
    print(result.id, result.first_name)