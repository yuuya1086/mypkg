import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Float64, "countup", 10)
        self.n = 10000.0
        self.add_initial_value = False
        self.create_timer(5, self.cb)

    def cb(self):
        msg = Float64()
        if not self.add_initial_value:
            self.n += 0.05
            self.add_initial_value = True
        else:
            self.n += random.uniform(-0.9, 0.9)

        msg.data = round(self.n, 2)
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
