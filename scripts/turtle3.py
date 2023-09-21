#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class TurtleListener():
    def __init__(self): #コンストラクタ　__init__
                        #selfはインスタンス変数？
            super().__init__('turtle_listener_node')
            self.subscription = self.create_subscription(Twist,'cmd_vel', self.listener_callback, 10) 
            #subscriberの生成
            #1番目の引数　Twist＝メッセージ型
            #2番目の引数　cmd_vel トピック名　？
            #3番目の引数  callback関数
            #4番目の引数  キューのサイズ　？
    def listener_callback(self, Twist):
         self.get_logger().info("Velocity: Linear=%f angular=%f" % (Twist.linear.x,Twist.angular.z)) 

if __name__ == '__main__':  # 初期化宣言 
     rospy.init_node("turtle_lintener_node") 
     turtle_listener = TurtleListener()
     rospy.spin()           #ノードが動いている間コールバック関数を呼び続ける