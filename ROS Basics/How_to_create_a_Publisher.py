#import the necessary library
import rospy

#import the message file (It will be in .msg format in your package)
from std_msgs.msg import String

def main():
    #create the node
    rospy.init_node('new_node')
    
    #create the publisher
    pub = rospy.Publisher('<put the topic name here>', String, queue_size = 10)
    rate = rospy.Rate(1)
    
    while rospy.is_not_shutdown():
        #create a message variable and set the message you want.
        message = String()
        message.data = 'Hey I am the New Node'
        
        #publish the message using your publisher
        pub.publish(message)
        
        rospy.sleep(1)
        
if __name__ == '__main__':
    main()
      
