from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO


from car.serializers import CarSerializer


from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_data = JSONRenderer().render(serializer.data)
    return json_data


def deserialize_car_object(json: bytes) -> Car:
    stream = BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        car = serializer.save()
        return car
    else:
        raise ValueError("Invalid data")
