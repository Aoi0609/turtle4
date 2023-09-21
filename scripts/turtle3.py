#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class DrawSquare:
    def __init__(self):
        rospy.init_node('draw_spuare', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(1)  # 1 Hz (adjust the rate as needed)

    def move_forward(self, distance):
        vel_msg = Twist()
        vel_msg.linear.x = 1.0  # Move forward at 1 m/s
        total_distance = 0
        while total_distance < distance and not rospy.is_shutdown():
            self.velocity_publisher.publish(vel_msg)
            total_distance += 1.0  # Assuming a rate of 1 Hz
            self.rate.sleep()
        vel_msg.linear.x = 0  # Stop the turtle
        self.velocity_publisher.publish(vel_msg)

    def turn(self):
        vel_msg = Twist()
        vel_msg.angular.z = 1.0  # Rotate at 1 rad/s (adjust as needed)
        angle_turned = 0
        target_angle = 1.5708  # 90 degrees in radians
        while angle_turned < target_angle and not rospy.is_shutdown():
            self.velocity_publisher.publish(vel_msg)
            angle_turned += 1.0  # Assuming a rate of 1 Hz
            self.rate.sleep()
        vel_msg.angular.z = 0  # Stop the turtle
        self.velocity_publisher.publish(vel_msg)

    def draw_square(self, side_length):
        for _ in range(4):
            self.move_forward(side_length)
            self.turn()

if __name__ == '__main__':
    try:
        square_drawer = DrawSquare()
        side_length = 2.0  # Length of each side of the square (adjust as needed)
        square_drawer.draw_square(side_length)
    except rospy.ROSInterruptException:
        pass
