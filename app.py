from flask import Flask, jsonify, request

app = Flask(__name__)

players = [
    {
        "id": "1",
        "name": "Bob",
        "level": 33,
        "class": "Warrior",
        "zone": "Ogrimmar City",
    },
    {
        "id": "2",
        "name": "Rose",
        "level": 40,
        "class": "Hunter",
        "zone": "Stormwind City",
    },
    {
        "id": "3",
        "name": "Sodapopin",
        "level": 60,
        "class": "Druid",
        "zone": "Thunder City",
    },
]


@app.route("/")
def home():
    return jsonify({"message": "This is home, please go to /data"})



# Work on this shitty part.

@app.route("/data/<int:playerID>", methods=["GET"])
def users(playerID):
    print(request.args)
    if request.args is None:
        return jsonify({"XD": "hahaha"})

    return jsonify(players[playerID])


@app.errorhandler(404)
def not_found(e):
    path = request.path.replace("/", "")
    return jsonify({"message": "Not Found", "code": 404, "path": path}), 404


if __name__ == "__main__":
    app.run(debug=True)
