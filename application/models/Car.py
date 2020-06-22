from .. import db, ma

class Car(db.Model):
    __tablename__ = "cars"
    car_id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String()) # this would normally be a make_id if we were making more tables
    model = db.Column(db.String()) # this would normally be a model_id if we were making more tables
    mileage = db.Column(db.Integer)

    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage

    def __repr__(self):
        return f"<Car car_id={self.car_id} make={self.make} model={self.model} mileage={self.mileage}>"

class CarSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Car

car_schema = CarSchema()