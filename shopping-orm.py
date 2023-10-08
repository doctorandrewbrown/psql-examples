from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Shopping" table
class Shopping(base):
    __tablename__ = "Shopping"
    Item_id = Column(Integer, primary_key=True)
    Name = Column(String)
    Type = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


#Select all records from the "Shopping" table
'''shopping = session.query(Shopping)
for item in shopping:
     print(item.Item_id, item.Name, item.Type, sep=" | ")'''

#Select all records from the "Shopping" table where "Type" is 'meat'
'''shopping = session.query(Shopping).filter(Shopping.Type=="meat").all()
for item in shopping:
     print(item.Item_id, item.Name, item.Type, sep=" | ")'''

#Add row to "Shopping" table. Note autoincrement of PK 
shopping = Shopping(Name='carrot', Type= 'veg')
session.add(shopping)
session.commit()

#Delete row from "Shopping" table by Item_id
'''shopping = session.query(Shopping).filter_by(Item_id=1).delete()
session.commit()'''

#Update Type field in shopping table
'''shopping = session.query(Shopping).filter_by(Item_id=3).first()
shopping.Type="meat"
session.commit()'''

# loop through shopping list and print 
shopping_list = session.query(Shopping)
for item in shopping_list:
    print(item.Name)