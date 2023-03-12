from . import db
class Property(db.Model):
    __tablename__='propertytable'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    bedrooms_no = db.Column(db.Integer, nullable=False)
    bathrooms_no = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    photo_filename = db.Column(db.String(100), nullable=False)

    def __init__(self, title, type, bedrooms_no, bathrooms_no, location, price, description, photo_filename):
        self.title = title
        self.type = type
        self.bedrooms_no = bedrooms_no
        self.bathrooms_no = bathrooms_no
        self.location = location
        self.price = price
        self.description = description
        self.photo_filename = photo_filename
