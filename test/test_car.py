import time

from vehicle_simulation_environment import car


class TestCar(object):
    def test_car_movement(self):
        init_params = car.Parameters(0, 0, 0, 0, 0, 0, 0)
        test_car = car.Car(init_params)

        time.sleep(1)
        assert test_car.x == 0
        assert test_car.y == 0
        assert test_car.theta == 0
        assert test_car.vel == 0

        test_car.stop()
        print("here")
