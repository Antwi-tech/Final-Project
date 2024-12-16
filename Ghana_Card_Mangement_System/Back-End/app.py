from flask import Flask, request, jsonify
import json

app = Flask(__name__)


# Using the data.json file to upload data
@app.route('/upload', methods=["POST"])
def upload_data():
    try:
        # Extract form data from request
        card = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "other_name": request.form.get("other_names"),
            "id_number": request.form.get("id_number"),
            "gender": request.form.get("gender"),
            "national": request.form.get("national")
        }

        # Print the received data for debugging
        # print(card)

        # Load existing data from JSON file
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []  # Initialize empty list if file doesn't exist or is invalid

        # Append the new record
        data.append(card)

        # Save back to the JSON file
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

        # Return success response
        return jsonify({"message": "Data successfully saved!", "data": card}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
    
    

if __name__ == '__main__':
    app.run(debug=True)
