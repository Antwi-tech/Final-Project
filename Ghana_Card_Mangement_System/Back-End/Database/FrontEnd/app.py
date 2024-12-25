# This API is specifically for the frontend interaction with the backend
from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("success.html")

# Get the data from th front-end
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
    
    
@app.route("/search_card", methods=['GET'])
def get_card():
    try:
        last_name = request.args.get('last_name')
        if not last_name:
            return jsonify({"message":"Card Not Found"}), 404
        
        backend_url = f"http://127.0.0.1:5000/upload/{last_name}"
        
        response = requests.get(backend_url)
        
        return jsonify(response.json()), response.status_code
    
    except Exception as e:
        return jsonify({"error":f"{str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    