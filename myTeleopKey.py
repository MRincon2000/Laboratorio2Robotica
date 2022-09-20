
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi
from turtlesim.msg import Pose
import argparse

from pynput import keyboard as kb

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rospy.init_node('velPub', anonymous=False)
vel = Twist()
rate = rospy.Rate(10) 

def rotacion():
    lin=0
    ang=pi
    rospy.wait_for_service('/turtle1/teleport_relative')
    teleportR = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
    resp1 = teleportR(lin, ang)

def traslacion():
    x=5.5444
    y=5.5444
    ang=0
    rospy.wait_for_service('/turtle1/teleport_absolute')
    teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
    resp1 = teleportA(x, y, ang)


def pulsa(tecla):
    
    if tecla == kb.KeyCode.from_char('w'): 
        vel.linear.x = 1
        vel.angular.z = 0
        rospy.loginfo(vel)
        pub.publish(vel)
        rate.sleep()
    elif tecla == kb.KeyCode.from_char('s'):
        vel.linear.x = -1
        vel.angular.z = 0
        rospy.loginfo(vel)
        pub.publish(vel)
        rate.sleep()
    elif tecla == kb.KeyCode.from_char('d'):
        vel.linear.x = 0
        vel.angular.z = -1
        rospy.loginfo(vel)
        pub.publish(vel)
        rate.sleep()
    elif tecla == kb.KeyCode.from_char('a'):
        vel.linear.x = 0
        vel.angular.z = 1
        rospy.loginfo(vel)
        pub.publish(vel)
        rate.sleep()
    elif tecla == kb.Key.space:
        rotacion()
    elif tecla == kb.KeyCode.from_char('r'):
        traslacion()

    elif tecla == kb.KeyCode.from_char('m'):
        return False
    


with kb.Listener(pulsa) as escuchador:
    escuchador.join()



