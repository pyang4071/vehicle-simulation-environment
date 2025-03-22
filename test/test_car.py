import pytest
import time
import numpy as np

from vehicle_simulation_environment import car


class TestCar(object):
    @pytest.mark.parametrize(
        "x,y,theta,vel,accel",
        [
            (0, 0, 0, 0, 0),
            (0, 0, 0, 1, 1),
            (2, 3, 0, 3, -1),
            (-2.5, -3.5, 0, -2, -0.5),
            (0, 0, np.pi, 1, 0),
            (1, 1, np.pi / 2, 3, -3),
            (1, 2, np.pi / 4, -2, 4),
        ],
    )
    def test_linear_movement(self, x, y, theta, vel, accel):
        init_params = car.Parameters(x, y, theta, vel, accel, 0, 0)
        test_car = car.Car(init_params)

        time_start = time.monotonic()
        time.sleep(2)
        test_car.stop()

        dtime = test_car.cur_time - time_start
        print(f"\n dtime = {dtime}")

        mag_dist = vel * dtime + 0.5 * test_car.accel * (dtime**2)
        expected_x = x + mag_dist * np.cos(test_car.theta)
        expected_y = y + mag_dist * np.sin(test_car.theta)
        expected_vel = vel + test_car.accel * dtime

        assert test_car.theta == theta
        assert test_car.accel == accel
        assert test_car.x >= (expected_x - 0.05)
        assert test_car.x <= (expected_x + 0.05)
        assert test_car.y >= (expected_y - 0.05)
        assert test_car.y <= (expected_y + 0.05)
        assert test_car.vel >= (expected_vel - 0.05)
        assert test_car.vel <= (expected_vel + 0.05)
