from flask_restful import Resource
from models.trip import TripModel

class TripResource(Resource):
    def get(self, trip_id):
        return TripModel.find_by_id(trip_id).json()
