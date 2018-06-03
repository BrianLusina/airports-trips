import uuid
from nameko.rpc import rpc
from nameko_redis import Redis


class TripsService(object):
    name = "trips_service"

    redis = Redis("development")

    @rpc
    def get(self, trip_id):
        """
        Gets the trip object from Redis database using the trip_id
        :param: trip_id
        :return: Trip object
        :rtype: object
        """
        trip = self.redis.get(trip_id)
        return trip
    
    @rpc
    def create(self, airport_from_id, airport_to_id):
        """
        Creates a Trip object with the airiport_from_id and airport_do_id
        :param: airport_from_id Where the trip beings
        :param: airport_to_id Id of the airport for the given destination
        :return: Trip id
        :rtype: str
        """
        trip_id = uuid.uuid4().hex
        self.redis.set(trip_id, {
            "from": airport_from_id,
            "to": airport_to_id
        })
        return trip_id
