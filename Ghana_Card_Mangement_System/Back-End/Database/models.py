from sqlalchemy import Column,Integer,String,CHAR,Enum
from sqlalchemy.orm import declarative_base
from config import session

Base = declarative_base()

# Creating tables in the Ghana Card database
# class Card(Base):
#     __tablename__ = "card" 
#     id_number = Column(CHAR(14) , primary_key = True, nullable = False)
    
class Person(Base):  
    __tablename__ = "person"
    id = Column(Integer, primary_key = True, autoincrement=True)
    first_name = Column(String(250), nullable = False) 
    last_name = Column(String(250) , nullable= False) 
    middle_name = Column(String(250), nullable = True) 
    sex = Column(Enum('male','female', name ='sex'), nullable=False )
    citizenship = Column(Enum('citizen','non-citizen', name='citizenship'), nullable = False)
    id_number = Column(CHAR(14) , primary_key = True, nullable = False)

    
    
if __name__ == '__main__':
    try:
        Base.metadata.create_all(session.bind)
        print('Card and Person table created successfully')
        
    except Exception as e:
        print(f'An error occurred: {e}')