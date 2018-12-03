#!/usr/bin/env python
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image
from feature_visual_odometry.image_manager import ImageManager


def publish_images():
    bridge = CvBridge()
    pub = rospy.Publisher('/image_vo_topic', Image, queue_size=1)
    my_image_manager = ImageManager()

    image_path_1 = '/home/guillem/Documents/feature_alignment/catkin_ws/src/image_provider/Images/IMG_0568.JPG'
    my_image_manager.read_image(image_path_1)
    ros_img = bridge.cv2_to_imgmsg(my_image_manager.image)
    pub.publish(ros_img)

    rospy.sleep(1)

    image_path_2 = '/home/guillem/Documents/feature_alignment/catkin_ws/src/image_provider/Images/IMG_0570.JPG'
    my_image_manager.read_image(image_path_2)
    ros_img = bridge.cv2_to_imgmsg(my_image_manager.image)
    pub.publish(ros_img)


if __name__ == '__main__':
    rospy.init_node('image_provider', anonymous=False)
    publish_images()
