from A2.db import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    country = db.Column(db.String)

    def __init__(self, firstname, lastname, password, email, country):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.email = email
        self.country = country

    def json(self):
        return {'id': self.id, 'firstname': self.firstname, 'lastname': self.lastname, 'email': self.email,
                'password': self.password, 'country': self.country}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        # print(email)
        """searching by username"""
        return cls.query.filter_by(email=email).first()

    @classmethod
    def fetch_country_by_email(cls, email):
        # return db.session.query(cls.country).filter_by(email=email).first()
        return cls.query.filter_by(email=email).first().country
