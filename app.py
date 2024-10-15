from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to perform calculations
@app.route("/calculate", methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    operation = data.get("operation")
    
    if not all([num1, num2, operation]):
        return jsonify({"error": "Missing data!"}), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
        else:
            return jsonify({"error": "Invalid operation!"}), 400
        
        return jsonify({"result": result})

    except ValueError:
        return jsonify({"error": "Invalid input!"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Running on port 5001 to avoid conflict with Streamlit
