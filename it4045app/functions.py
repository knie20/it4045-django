__author__ = 'Andrew'
from models import Car, CarDescription, Transmission, Motor
def authenticate(request):
    return True


def create_new_car(*args, **kwargs):

    motor = Motor()
    motor.displacement = kwargs.get("displacement")
    motor.family = kwargs.get("family")
    motor.horsepower = kwargs.get("horsepower")
    motor.rpm = kwargs.get("rpm")
    motor.save()

    transmission = Transmission()
    transmission.speed = kwargs.get("speed")
    transmission.type = kwargs.get("transmission_type")
    transmission.save()

    #create car description before save
    car_description = CarDescription()
    car_description.description = kwargs.get("description", "n/a")
    car_description.mileage = kwargs.get("mileage")
    car_description.mpg = kwargs['mpg']
    car_description.motor = motor
    car_description.transmission = transmission
    car_description.save()



    car = Car()
    car.make = kwargs.get("make")
    car.model = kwargs.get("model")
    car.color = kwargs.get("color")
    car.year = kwargs.get("year")
    car.description = car_description
    car.save()


def filter_cars(*args, **kwargs):
    cars = Car.objects.filter(**kwargs)
    # car = Car.objects.get(id=1)
    # objs = Car.objects.filter(**kwargs)
    return cars

def get_car(*args, **kwargs):
    return Car.objects.get(id=1)



