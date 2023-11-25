import warnings

import rospy

from crazyswarm.msg import WebotsFullState


# (self, dt, desired_vx, desired_vy, desired_yaw_rate, desired_altitude, actual_roll, actual_pitch, actual_yaw_rate,
#           actual_altitude, actual_vx, actual_vy)


class VisWebots:

    def __init__(self) -> None:
        #  Items required to Publish:
        #  dt
        #  desired_vx
        #  desired_vy
        #  desired_yaw_rate
        #  desired_altitude
        #  actual_roll
        #  actual_pitch 
        #  actual_yaw_rate
        #  actual_altitude
        #  actual_vx
        #  actual_vy
        rospy.init_node("CrazyWebotVisualiser", anonymous=False)
        self.init = True
        self.cmdFullStatePublishers = rospy.Publisher("/webots_full_state", WebotsFullState, queue_size=1)
        self.drone_positions = None
        self.cmdFullStateMsg = WebotsFullState()
        self.cmdFullStateMsg.header.seq = 0

    def __del__(self):
        self.cmdFullStatePublishers.unregister()

    def update(self, t, crazyflies):
        if self.init:
            #  initialise all information on first update
            self.init = False
            print("Webots Initialisation Complete.")
        rate = rospy.Rate(5)
        for drone in crazyflies:
            self.cmdFullStateMsg.header.stamp = rospy.Time.now()
            self.cmdFullStateMsg.header.seq += 1
            print(self.cmdFullStateMsg.header.stamp)
            print(self.cmdFullStateMsg.header.seq)
            self.cmdFullStatePublishers.publish(self.cmdFullStateMsg)
            rate.sleep()

    def render(self):
        warnings.warn("Rendering video not supported in VisWebots yet.")
        return None