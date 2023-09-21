#! /usr/bin/env python3
  
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
  
class turtleSim:
    def __init__(self):
        rospy.init_node('move_turtlesim', anonymous=True)
        self.twist_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1000)
        rospy.Subscriber('turtle1/pose',Pose, self.poseCallback)
        rospy.Timer(rospy.Duration(1.0), self.timerCallback)
  
        twist = Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        self.twist_pub.publish(twist)
  
    def poseCallback(self, pose):
        rospy.loginfo("x:%f", pose.x)
  
    def timerCallback(self, event):
        self.setMoveVector(0.3, 5)
        self.setMoveVector(-0.3, 5)
 
    def setMoveVector(self, linear_x, cnt):
        twist = Twist()
        r = rospy.Rate(10)
  
        twist.linear.x = linear_x
        twist.angular.z = 0.0
  
        for i in range(0, cnt):
            self.twist_pub.publish(twist)
            r.sleep()
  
if __name__ == '__main__':
  
    try:
        ts = turtleSim()
        rospy.spin()
    except rospy.ROSInterruptException: pass