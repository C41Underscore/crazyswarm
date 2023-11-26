import warnings

import numpy as np

import rospy

from crazyswarm.msg import VelocityWorld


class VisWebots:

    def __init__(self) -> None:
        rospy.init_node("CrazyWebotVisualiser", anonymous=False)
        self.cmdFullStatePublishers = rospy.Publisher("/webots_full_state", VelocityWorld, queue_size=1)
        self.cmdFullStateMsg = VelocityWorld()
        self.cmdFullStateMsg.header.seq = 0
        self.rate = rospy.Rate(10)
        self.times_called = 0

        self.init = True
        self.drone_positions = None
        self.prev_time = None

    def __del__(self):
        self.cmdFullStatePublishers.unregister()
        print(self.times_called)

    def __vis_init(self, crazyflies):
        #  initialise all information on first update
            self.drone_positions = {drone: drone.position() for drone in crazyflies}
            self.prev_time = rospy.Time.now().nsecs
            self.init = False
            print("Webots Initialisation Complete.")

    def __compute_velo(self, t, drone):
        pos = drone.position()
        dt = np.abs((t - self.prev_time))
        vel = (pos - self.drone_positions[drone])/dt
        return vel

    def update(self, t, crazyflies):
        self.times_called += 1
        if self.init:
            self.__vis_init(crazyflies)

        for drone in crazyflies:
            self.cmdFullStateMsg.header.stamp = rospy.Time.now()
            self.cmdFullStateMsg.header.seq += 1

            vel = self.__compute_velo(t, drone)
            print(vel)

            self.cmdFullStateMsg.vel.x = vel[0]
            self.cmdFullStateMsg.vel.y = vel[1]
            self.cmdFullStateMsg.vel.z = vel[2]
            self.cmdFullStatePublishers.publish(self.cmdFullStateMsg)

            self.drone_positions = {drone: drone.position() for drone in crazyflies}
            self.prev_time = t
            self.rate.sleep()

    def render(self):
        warnings.warn("Rendering video not supported in VisWebots yet.")
        return None