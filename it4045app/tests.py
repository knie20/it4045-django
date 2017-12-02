__author__ = 'Andrew'
from django.test import TestCase
from it4045app.models import Car, Motor, Transmission, CarDescription

class CarsTestCase(TestCase):
    def setUp(self):
        motor = Motor()
        motor.displacement = '352'
        motor.family = 'FE'
        motor.horsepower = 275
        motor.rpm = '4400'
        motor.save()

        transmission = Transmission()
        transmission.speed = 3
        transmission.type =  'automatic'
        transmission.save()




        car_description = CarDescription()
        car_description.description = "n/a"
        car_description.mileage = '1111111'
        car_description.mpg = '12'
        car_description.motor = motor
        car_description.transmission = transmission
        car_description.save()

        car = Car()
        car.make = "ford"
        car.model = 'f250'
        car.color = 'blue'
        car.year = '1966'
        car.description = car_description
        car.save()


    def test_get_cars(self):
        print ("tests running")
        for car in Car.objects.filter():
            print  (car.make + " " +car.model)

    def test_get_car(self):
        car = Car.objects.get(id=1)
        self.assertEqual(car.id, 2)
        # print car.make + " " + car.model + " "+ str(car.id)
        # print "%s %s %s" %(car.make, car.model, car.id)
