from tests.base import BaseTestCase
from models.trip import TripModel

class TestModelTrip(BaseTestCase):

  def test_constructor(self):
    trip = TripModel('Dash', [])
    self.assertEqual(trip.dog, 'Dash')
    self.assertEqual(trip.legs, [])

  def test_db_save(self):
    trip = TripModel('Dash', [])
    trip.db_save()
    self.assertEqual(trip.id, 1)

  def test_find_by_id(self):
    trip = TripModel('Dash', [])
    trip.db_save()
    trip2 = TripModel.find_by_id(trip.id)
    self.assertEqual(trip.id, trip2.id)
    self.assertEqual(trip.dog, trip2.dog)

  def test_json(self):
    trip = TripModel('Dash', [])
    json = trip.json()
    self.assertEqual(json['dog'], 'Dash')

if __name__ == '__main__':
    unittest.main()
