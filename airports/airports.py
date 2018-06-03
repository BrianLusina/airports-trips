import uuid
from nameko.rpc import rpc
from nameko_redis import Redis


class AirportService(object):
    name = "airports_service"

    redis = Redis("development")

    @rpc
    def get(self, airport_id):
        """
        Gets the airport object from Redis database using the airport_id
        :param: airport_id
        :return: Airport object
        :rtype: object
        """
        airport = self.redis.get(airport_id)
        return airport
    
    @rpc
    def create(self, airport):
        """
        Creates an airport object and returns the airport id
        :param: airport Airport Object
        :return: Airport id
        :rtype: str
        """
        airport_id = uuid.uuid4().hex
        self.redis.set(airport_id, airport)
        return airport_id