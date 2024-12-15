from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

database_username = os.getenv("DATABASE_USERNAME")
database_password = os.getenv("DATABASE_PASSWORD")
database_name = os.getenv("DATABASE_NAME")

connection_str = f"mysql+mysqlconnector://{database_username}:{database_password}@localhost/{database_name}"

engine = create_engine(connection_str)

try:
    connection = engine.connect()
    print("Connection established successfully")
    connection.close()

except Exception as e:
    print(f'An error occured: {e}. ') 
    
    
DBSession = sessionmaker(bind=engine)  
session = DBSession() 
       