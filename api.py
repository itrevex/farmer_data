from flask import Flask
from flask import jsonify
from data.map_data import MapData

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    farmer_data = MapData().get_districts_farmer_data()
    return jsonify(farmer_data)


if __name__ == "__main__":
    app.run(debug=True, port=8002)
