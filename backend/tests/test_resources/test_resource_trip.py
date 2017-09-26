from tests.base import BaseTestCase
from models.trip import TripModel
from flask_api import status
from tests.util import jsonify_response

class TestResourceTrip(BaseTestCase):

  def test_get_success(self):
    trip = TripModel('Dash', [])
    trip.db_save()
    result = self.app.get('/trip/1')
    self.assertEqual(result.status_code, status.HTTP_200_OK)
    json_response = jsonify_response(result)
    self.assertEqual(json_response['id'], 1)
    self.assertEqual(json_response['dog'], 'Dash')

if __name__ == '__main__':
    unittest.main()
