import warnings

import rospy


# (self, dt, desired_vx, desired_vy, desired_yaw_rate, desired_altitude, actual_roll, actual_pitch, actual_yaw_rate,
#           actual_altitude, actual_vx, actual_vy)


class VisWebots:

    def __init__(self) -> None:
        pass

    def update(self, t, crazyflies):
        pass

    def render(self):
        warnings.warn("Rendering video not supported in VisWebots yet.")
        return None