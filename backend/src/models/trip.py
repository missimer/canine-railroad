from db import db
from models.leg import LegModel

class TripModel(db.Model):
  __tablename__ = 'trip'

  id = db.Column(db.Integer, primary_key=True)
  dog = db.Column(db.String(128))
  legs = db.relationship('LegModel', back_populates='trip')

  def __init__(self, dog, legs):
    self.dog = dog
    self.legs = legs

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

  def json(self):
    return {
      'id' : self.id,
      'dog' : self.dog
    }

  def db_save(self):
    db.session.add(self)
    db.session.commit()
