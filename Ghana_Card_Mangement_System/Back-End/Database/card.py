from config import session
from models import Person
from sqlalchemy.exc import IntegrityError

class Card_details:
    def __init__(self):
        self.session = session
        
# Add a missing but found card(Usage of create in CRUD)
    def add_missing_card(self, first_name, last_name, middle_name, sex, id_number, citizenship):
        try:
            found_card = Person(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                sex=sex,
                id_number=id_number,
                citizenship=citizenship
            )
            self.session.add(found_card)
            self.session.commit()

            return found_card
        
        except IntegrityError as e:
            self.session.rollback() 
            print(f"Error occurred: {e}")
    
# Retrieve all missing but found cards that have been uploaded to the system
    def get_all_found_cards(self):
        try:
            return self.session.query(Person).all()
        
        except Exception as e:
            return f"Ops Error!:{e}"
    
# Get card according to lastname
    def get_card_by_lastname(self, last_name):
        try:
            
            card = session.query(Person).filter_by(last_name=last_name).first() 
            if not card:
                raise ValueError(f"No card found with last name '{last_name}'")
            
            return card
        
        except Exception as e:
            return f"Error Occured while retrieving last anme: {e}"
        
    
    def get_card_by_id(self, id_number):
        return session.query(Person).filter_by(id_number=id_number).first() 
    
#Update input from user. 
    def update_card_by_name(self, last_name,first_name = None, middle_name=None,id_number=None, sex=None, citizenship=None):
        selected_card = self.session.query(Person).filter_by(last_name=last_name).first()
        if selected_card:
            if first_name:
                selected_card.first_name = first_name    
            if middle_name:
              selected_card.middle_name = middle_name
            if sex:
                selected_card.sex = sex
            if id_number:
                selected_card.id_number = id_number  
            if citizenship:
                selected_card.citizenship = citizenship       
        session.commit()        
        return selected_card
        
# Delete a card if the card has been retrieved

    def delete_card(self, id_number):
        retrieved_card = session.query(Person).filter_by(id_number=id_number).first()
        if retrieved_card:
             self.session.delete(retrieved_card)
        session.commit()     
        return retrieved_card
        
        
        
        

card = Card_details()
