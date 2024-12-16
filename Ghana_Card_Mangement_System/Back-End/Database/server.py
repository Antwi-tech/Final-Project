# API endpoints
from flask import Flask, request, jsonify
from card_details_blueprint import *




app = Flask(__name__)
app.register_blueprint(person_card)

cards = Card_details
@app.route("/")
def home():
    return "Welcome Home" 
        
        
            
if __name__ == "__main__":
    app.run(debug=True)