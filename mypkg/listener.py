# SPDX-FileCopyrightText: 2024 Yuuya Tanaka s23c1086uu@s.chibakoudai.jp
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %.2f" % msg.data)


def main():
    pub = node.create_subscription(Float64, "kabuka", cb, 10)
    rclpy.spin(node)
