import time

from vehicle_simulation_environment import car


class TestCar(object):
    def test_no_velocity(self):
        init_params = car.Parameters(0, 0, 0, 0, 0, 0, 0)
        test_car = car.Car(init_params)

        time.sleep(1)

        test_car.stop()
        assert test_car.x == 0
        assert test_car.y == 0
        assert test_car.theta == 0
        assert test_car.vel == 0

    def test_constant_velocity(self):
        init_params = car.Parameters(0, 0, 0, 1, 0, 0, 0)
        test_car = car.Car(init_params)

        time_start = time.monotonic()
        time.sleep(1)

        dtime = test_car.cur_time - time_start
        test_car.stop()
        assert test_car.vel == 1
        assert test_car.x == 0
        expected_y = test_car.vel * dtime
        assert (expected_y - 0.05) <= test_car.y
        assert (expected_y + 0.05) >= test_car.y

    def test_constant_accel(self):
        init_params = car.Parameters(0, 0, 0, 0, 1, 0, 0)
        test_car = car.Car(init_params)

        time_start = time.monotonic()
        time.sleep(1)

        dtime = test_car.cur_time - time_start
        test_car.stop()
        assert test_car.accel == 1
        assert test_car.x == 0
        expected_y = 0.5 * 1 * (dtime**2)
        assert (expected_y - 0.05) <= test_car.y
        assert (expected_y + 0.05) >= test_car.y
