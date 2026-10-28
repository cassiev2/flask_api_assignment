from flask import Flask, request, jsonify

app = Flask(__name__)

# DICTIONARIES for value lookup
coin_ledger = {"grover": 150, "cassie": 45, "ollie": 10}


# GET endpoint - personal greeting
@app.get("/hello")
def hello():
    # extract 'name' from hello get string
    name = request.args.get("name")

    if name:
        response = {"message": f"Warm greetings, traveler {name}.", "status": "success"}
        return jsonify(response)
    else:
        response = {
            "message": "Not used to strangers in these parts",
            "status": "success",
        }
        return jsonify(response)


# GET endpoint - player coin balance
@app.get("/coinbal")
def coinbal():

    name = (request.args.get("name") or "").strip().lower()

    if not name:
        response = {"message": "You didn't provide a ?name=", "status": "error"}
        return jsonify(response), 400

    coins = coin_ledger.get(name)

    if coins is None:
        response = {"coinbal": 0, "status": "not found"}
        return jsonify(response), 404
    else:
        response = {"coinbal": coins, "status": "success"}
        return jsonify(response)


# POST endpoint
@app.post("/sum")
def sum_numbers():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    if "numbers" not in data:
        return jsonify({"error": "expected dataset not provided"}), 400

    numbers = data["numbers"]

    if not isinstance(numbers, list):
        return jsonify({"error": "A list was not provided"}), 400

    try:
        total = sum(numbers)

    except TypeError:
        return jsonify({"error": "Non-numeric values were provided"}), 400

    return jsonify({"sum": total}), 200


if __name__ == "__main__":
    app.run(debug=True)
