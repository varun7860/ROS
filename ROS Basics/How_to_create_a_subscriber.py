#import the necessary library
import rospy

#import the message file.
from std_msgs.msg import String

def callback(msg):
    #put the message in a variable.
    message = msg.data
    
    #print the message on terminal
    rospy.loginfo('Message:')
    rospy.loginfo(message)

def main():
    #create a node with different name(This name should not be same as publisher node).
    rospy.init_node('Subscriber_Node', anonymous = True)
    
    #create the Subscriber.
    sub = rospy.Subscriber('<Topic name same as publisher node>', String, callback, queue_size = 10)
    
    #This will prevent the code from shutting down
    rospy.spin()
    
if __name__ == '__main__':
    main()
