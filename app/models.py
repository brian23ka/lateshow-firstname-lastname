from . import db

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)

    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "number": self.number,
        }

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation,
        }

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id,
            "episode": self.episode.to_dict(),
            "guest": self.guest.to_dict()
        }

    def validate(self):
        errors = []
        if not 1 <= self.rating <= 5:
            errors.append("Rating must be between 1 and 5.")
        return errors
