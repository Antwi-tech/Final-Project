from config import session
from models import Person

class Card_details:
    def __init__(self):
        self.session = session

    def add_missing_card(self, first_name, last_name, middle_name, sex, id_number, citizenship):
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

card = Card_details()
