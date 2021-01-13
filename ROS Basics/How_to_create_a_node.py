#import the necessary library for ros
import rospy

def main():
    '''init_node() takes argument which is the name of the node
       you can put any name of node you want. You can make node
       node anonymous by putting anonymous = True as second
       argument'''
    
    #create a new node in ros by rospy.init_node() function.
    rospy.init_node('new_node')
    
    #print on the terminal by rospy.loginfo() function
    rospy.loginfo('Node created successfully')
    
if __name__ == '__main__':
    main()
