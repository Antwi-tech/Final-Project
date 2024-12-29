# This API is specifically for the frontend interaction with the backend
from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("success.html")

# Get the data from the front-end and send it to the backend
@app.route("/submit_details", methods=['POST'])
def get_details_from_form():
    try: 
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        middle_name = request.form.get('middle_name')
        id_number = request.form.get('id_number')
        sex = request.form.get('sex')
        citizenship = request.form.get('citizenship')
        
        print(f"First name: {first_name}, Last name: {last_name}, Middle name : {middle_name},ID_number: {id_number},sex:{sex},citizenship:{citizenship}") 
        
        backend_api =  "http://127.0.0.1:5000/upload"
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "sex": sex,
            "id_number": id_number,
            "citizenship":citizenship
        }
        headers = {"Content-type":"application/json"}
        response = requests.post(backend_api, json=payload, headers=headers)
        
        

        
        print("Received data:", payload)
        
        if response.status_code == 201:
            return render_template("success.html")
        
        else:
            return({"message":f"An error occured {response.text} "}), response.status_code
        
    except Exception as e:
        return  jsonify({"An error occured":{e}})  
    
    
# @app.route("/search_card", methods=['GET'])
# def get_card():
#     try:
#         last_name = request.args.get('last_name')
#         if not last_name:
#             return jsonify({"message":"Card Not Found"}), 404
        
#         backend_url = f"http://127.0.0.1:5000/upload/{last_name}"
        
#         response = requests.get(backend_url)
#         return jsonify(response.json()), response.status_code

    
#     except Exception as e:
#         return jsonify({"error":f"{str(e)}"}), 500  
    
#Edit card detail
@app.route("/edit_details", methods=['POST'])
def edit_card_detail():
    try:
        # Collect form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        middle_name = request.form.get('middle_name')
        id_number = request.form.get('id_number')
        sex = request.form.get('sex')
        citizenship = request.form.get('citizenship')

        # Debug: Print form data to verify
        print(f"Received data: First name: {first_name}, Last name: {last_name}, Middle name: {middle_name}, ID_number: {id_number}, Sex: {sex}, Citizenship: {citizenship}")

        if not last_name:
            return jsonify({"message": "Card Not Found"}), 404

        # Backend API call
        backend_api = f"http://127.0.0.1:5000/update/{last_name}"  # Use f-string for proper URL formatting
        payload = {
            "first_name": first_name,
            "middle_name": middle_name,
            "sex": sex,
            "id_number": id_number,
            "citizenship": citizenship
        }
        headers = {"Content-type": "application/json"}
        response = requests.put(backend_api, json=payload, headers=headers)  # Use PUT request

        # Debug: Log the backend response
        print("Backend Response:", response.status_code, response.text)

        # Handle response
        if response.status_code == 200:
            return render_template("editsuccess.html")
        else:
            return jsonify({"message": f"An error occurred: {response.text}"}), response.status_code

    except Exception as e:
        return jsonify({"An error occurred": str(e)})

    
# from flask import Flask, request, render_template_string
# import requests

# app = Flask(__name__)

# @app.route("/search_card", methods=['GET'])
# def get_card():
#     try:
#         last_name = request.args.get('last_name')
#         if not last_name:
#             return """
#             <html>
#             <body>
#                 <p>Card not found. Please provide a valid last name.</p>
#             </body>
#             </html>
#             """

#         # Call the backend API
#         backend_url = f"http://127.0.0.1:5000/upload/{last_name}"
#         response = requests.get(backend_url)

#         # If no card is found
#         if response.status_code != 200:
#             return """
#             <html>
#             <body>
#                 <p>Card not found.</p>
#             </body>
#             </html>
#             """

#         # Get card details
#         card_data = response.json().get("Card Found", {})
#         if not card_data:
#             return """
#             <html>
#             <body>
#                 <p>Card not found.</p>
#             </body>
#             </html>
#             """

#         # Inject data into the HTML
#         html_response = f"""
#         <!DOCTYPE html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <link rel="icon" href="images/card.png" type="image/png">
#             <link rel="stylesheet" href="style.css">
#             <title>Card Search Results</title>
#         </head>
#         <body>
#             <nav>
#                 <p class="gc"><a href="index.html">Ghana Card Search and Details</a></p>
#                 <div class="navbar">
#                     <a href="search.html">Search</a>
#                     <a href="form.html">Entry</a>
#                 </div>
#             </nav>
#             <form action="/search_card" method="GET">
#                 <div class="search">
#                     <span class="material-symbols-outlined search_icon"></span>
#                     <input type="search" name="last_name" class="search_input" placeholder="Search" value="{last_name}">
#                 </div>
#             </form>
#             <div class="card_found" id="result">
#                 <div>
#                     <p>First Name:</p>
#                     <input type="text" id="first_name" name="first_name" value="{card_data.get('first_name', '')}" readonly>
#                 </div>
#                 <div>
#                     <p>Last Name:</p>
#                     <input type="text" id="last_name" name="last_name" value="{card_data.get('last_name', '')}" readonly>
#                 </div>
#                 <div>
#                     <p>Middle Name(s):</p>
#                     <input type="text" id="middle_name" name="middle_name" value="{card_data.get('middle_name', '')}" readonly>
#                 </div>
#                 <div>
#                     <p>ID Number:</p>
#                     <input type="text" id="id_number" name="id_number" value="{card_data.get('id_number', '')}" readonly>
#                 </div>
#                 <div>
#                     <p>Sex:</p>
#                     <input type="text" id="sex" name="sex" value="{card_data.get('sex', '')}" readonly>
#                 </div>
#                 <div>
#                     <p>Citizenship:</p>
#                     <input type="text" id="citizenship" name="citizenship" value="{card_data.get('citizenship', '')}" readonly>
#                 </div>
#                 <div class="update_btn">
#                     <a href="edit.html"> <button class="edit">Edit</button></a>
#                     <button class="edit">Delete</button>
#                 </div>
#             </div>
#         </body>
#         </html>
#         """
#         return html_response

#     except Exception as e:
#         return f"<html><body><p>Error occurred: {str(e)}</p></body></html>", 500
    
# @app.route("/search_card", methods=['GET'])
# def get_card():
#     try:
#         last_name = request.form.get('last_name')
#         if not last_name:
#             return jsonify({"message":"Card Not Found"}), 404
        
#         backend_url = f"http://127.0.0.1:5000/upload/{last_name}"
        
#         response = requests.get(backend_url)
        
#         return jsonify(response.json()), response.status_code
    
#     except Exception as e:
#         return jsonify({"error":f"{str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    