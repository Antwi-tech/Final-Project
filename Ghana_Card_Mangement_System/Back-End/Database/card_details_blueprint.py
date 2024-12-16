from flask import Blueprint, request, jsonify
from card import Card_details

person_card = Blueprint('persons', __name__)
card = Card_details()

@person_card.route("/upload", methods=['POST'])
def record_card_details():
    credentials = request.get_json()

    try:
        if not credentials:
            return jsonify({"Error": "Enter data to continue"}), 400
        
        sex = credentials.get('sex')
        if sex not in ['male', 'female']:
            return jsonify({"Error occured at sex input":"sex must be male or female"})

        citizenship = credentials.get('sex')
        if citizenship not in ['citizen', 'non-citizen']:
            return jsonify({"Error occured at citizen staus input":"cititzenship must be citizen or non-citizen"})

        found_card = card.add_missing_card(
            first_name=credentials.get('first_name'),
            last_name=credentials.get('last_name'),
            middle_name=credentials.get('middle_name'),
            sex=sex,
            id_number=credentials.get('id_number'),
            citizenship=citizenship  
        )
        

        return jsonify({
            "Person_card": {
                "first_name": found_card.first_name,
                "last_name": found_card.last_name,
                "middle_name": found_card.middle_name,
                "sex": found_card.sex,
                "id_number": found_card.id_number,
                "citizenship": found_card.citizenship
            }
        }), 201

    except Exception as e:
        return jsonify({"Unexpected error": str(e)}), 500

# @person_card.route("/upload/search", methods=['PUT'])
# def update_card():
#     try:
#         # Get the query parameter for last_name
#         last_name = request.args.get('q')  # 'q' is the query parameter name
#         if not last_name:
#             return jsonify({"message": "Query parameter 'q' (last_name) is required"}), 400

#         # Find the card by last_name
#         ghana_card = card.get_card_by_lastname(last_name)
#         if ghana_card is None:
#             return jsonify({"message": f'Card with last name {last_name} does not exist'}), 404

#         # Get the updated data from the request body
#         update_data = request.get_json()
#         if not update_data:
#             return jsonify({"message": "No update data provided"}), 400

#         # Update the fields (example of updating first_name and citizenship)
#         if 'first_name' in update_data:
#             ghana_card.first_name = update_data['first_name']
#         if 'citizenship' in update_data:
#             ghana_card.citizenship = update_data['citizenship']

#         # Commit the changes to the database
#         card.session.commit()

#         return jsonify({
#             "message": f"Ghana Card with last name '{last_name}' has been updated.",
#             "Person_card": {
#                 "first_name": ghana_card.first_name,
#                 "last_name": ghana_card.last_name,
#                 "middle_name": ghana_card.middle_name,
#                 "sex": ghana_card.sex,
#                 "id_number": ghana_card.id_number,
#                 "citizenship": ghana_card.citizenship
#             }
#         }), 200


#     except Exception as e:
#         return jsonify({"Error occurred": str(e)}), 500



# Search for a card according to last name
@person_card.route("/upload/<string:last_name>", methods=['GET'])
def get_laptop_by_last_name(last_name):
    try:
        # Validate the input
        if not isinstance(last_name, str) or not last_name.isalpha():
            raise ValueError("Last name consists of letters only")
        
        # Perform the database operation
        credentails = card.get_card_by_lastname(last_name)
        
        # Check if a card was found
        if not credentails:
            return jsonify({"message": "Sorry, Card not found yet"}), 400
        
        # Return success response
        return jsonify({
            "Card Found": {
                "first_name": credentails.first_name,
                "last_name": credentails.last_name,
                "middle_name": credentails.middle_name,
                "sex": credentails.sex,
                "id_number": credentails.id_number,
                "citizenship": credentails.citizenship
            },
            "message": "Card found successfully!! Visit our office for retrieval."
        })

    # Handle validation errors
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400 #Bad request

    # Catch all other exceptions
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500 #Internal Server Error

    

@person_card.route('/upload', methods=['GET'])    
def get_card():
    cards_found=card.get_all_found_cards()
    list_card_found = []
    
    try:
        for cards in cards_found:
                list_card_found.append({
                "first_name": cards.first_name,
                "last_name": cards.last_name,
               "middle_name": cards.middle_name,
                "sex": cards.sex,
               "id_number": cards.id_number,
               "citizenship": cards.citizenship
                })
        return jsonify({"All cards in the system": list_card_found})  
    
    except Exception as e:
        return jsonify({"Unexpected Error":{e}})      

@person_card.route("/upload/<string:id_number>" , methods=['DELETE'])
def delete_found_card(id_number):
    found_card = card.get_card_by_id(id_number)
    try:
        if not found_card:
            return jsonify({"Card has been retrieved already"}), 404
    
        card.delete_card(id_number)
        return jsonify({"message":f"Card with id {id_number} has been deleted"})
    
    except Exception as e:
        return jsonify({"Error occured":{e}})