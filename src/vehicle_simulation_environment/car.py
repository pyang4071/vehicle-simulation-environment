import numpy as np
import time


class Parameters(object):
    def __init__(
        self,
        x_start,
        y_start,
        theta_start,
        vel_start,
        accel_start,
        angvel_start,
        ang_accel_start,
    ):
        self.x = x_start
        self.y = y_start
        self.theta = theta_start
        self.vel = vel_start
        self.accel = accel_start
        self.ang_vel = angvel_start
        self.ang_accel = ang_accel_start


class Car(object):
    """Model of a car as a point"""

    def __init__(self, init_param):
        self.reset(init_param)

    def reset(self, param):
        self.x = param.x
        self.y = param.y
        self.theta = param.theta
        self.vel = param.vel
        self.ang_vel = param.ang_vel
        self.prev_time = time.monotonic()
        self.cur_time = time.monotonic()
        self.update_param(param)

    def update_param(self, param):
        self.accel = param.accel
        self.ang_accel = param.accel

    def update_location(self):
        self.cur_time = time.monotonic()
        dtime = self.cur_time - self.prev_time
        self.prev_time = self.cur_time

        self.vel += self.accel * dtime
        self.ang_vel += self.ang_accel * dtime

        self.theta += self.ang_vel * dtime
        self.theta = self.theta % (2 * np.pi)
        mag_dist = self.vel * dtime

        dx = mag_dist * np.sin(self.theta)
        dy = mag_dist * np.cos(self.theta)
        self.x += dx
        self.y += dy
