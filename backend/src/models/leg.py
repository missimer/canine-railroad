from db import db

class LegModel(db.Model):
  __tablename__ = 'leg'

  id = db.Column(db.Integer, primary_key=True)
  trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'))
  trip = db.relationship('TripModel', back_populates='legs')
