from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import random
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


TopSecretAPIKey = os.environ.get("TopSecretAPIKey")


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict()), 200


@app.route("/all")
def get_all_cafes():
    all_cafes = Cafe.query.all()
    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes]), 200


@app.route("/search")
def search_for_cafe():
    query_location = request.args.get("loc").title()
    cafes_result = Cafe.query.filter_by(location=query_location).all()
    if cafes_result:
        return jsonify(cafe=[cafe.to_dict() for cafe in cafes_result])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404



@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(name=request.form.get("name"),
                    map_url=request.form.get("map_url"),
                    img_url=request.form.get("img_url"),
                    location=request.form.get("location"),
                    seats=request.form.get("seats"),
                    has_toilet=bool(request.form.get("has_toilet")),
                    has_wifi=bool(request.form.get("has_wifi")),
                    has_sockets=bool(request.form.get("has_sockets")),
                    can_take_calls=bool(request.form.get("can_take_calls")),
                    coffee_price=request.form.get("coffee_price"))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 200

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    client_api_key = request.args.get("TopSecretAPIKey")
    if client_api_key == TopSecretAPIKey:
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "Successfully deleted the cafe."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Not Authorized": "Sorry you are not authorized to make this action." }), 403


if __name__ == '__main__':
    app.run(debug=True)