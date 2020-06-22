from flask import request, jsonify
from .. import main
from ... import db
from ...models.Car import Car, car_schema

@main.route("/get-cars", methods=["GET"])
def get_cars():
    cars = Car.query.all()
    cars_json = car_schema.dump(cars, many=True)
    response = {"cars": cars_json}
    return response