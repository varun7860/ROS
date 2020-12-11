# About this Repo
This repo consists of all the projects of ros done by me till now.It covers up all the basics of ROS that a novice user needs to get started with it.Below are the general details
about ros ,its history and its installation.Read it all to get you started. 
For the Installation refer the section : Ïnstallation of ROS.

# What is ROS?
As the full name of Robot Operating System suggests, ROS is an operating system for robots. In the same way as operating systems for PCs, servers or standalone devices, ROS is a full operating system for service robotics.
ROS is in fact a meta-operating system, something between an operating system and middleware.
It provides not only standard operating system services (hardware abstraction, contention management, process management), but also high-level functionalities (asynchronous and synchronous calls, centralised database, a robot configuration system, etc.).

# The history of ROS
1. Many robot frameworks exist, produced for a specific reason, for prototyping purposes. ROS was intended to be more general-purpose, although its designers do not believe it to be the ultimate OS able to do everything.

2. ROS is developed and maintained by a Californian company, Willow Garage, formed in 2006 by Scott Hassan, one of Google’s first employees who was involved in the development of search engine technology and who was also behind Yahoo! Groups (eGroups, in fact, which became Yahoo! Groups). The President and CEO of Willow Garage is Steeve Cousins, previously at IBM.

3. Willow Garage is a private company that maintains close links with Stanford University, which is not far from Willow Garage (in Palo Alto, California).Willow Garage describes itself as a research laboratory and technology incubator for personal robotics, focused on research more than on profits (at the outset, at least).

4. Willow Garage develops both software with ROS and hardware with their PR2 and TurtleBot robots. Everything produced is open source (BSD licences). Their idea is that if we want to see robots reach our homes, then research needs to be accelerated by providing solid hardware and software bases that are open source.

5. It would appear that Willow Garage wishes to build the robotics community rather than robotics in and of itself. Interviewed by business magazine L’Expansion, Scott Hassan said that his objectives are the same as those of Irobot, but that the strategy to achieve them is different.

6. Four reasons to believe that Willow Garage will succeed according to the singularityhub.com website:

  - They want to provide resources to avoid reinventing the wheel, in order to speed up robotics research;
  - They have the necessary funds;
  - They have the attention of the research community;
  - They want to encourage the roll-out of their technology free of charge, before thinking of earning money.
  
# The general organisation of ROS

ROS’ philosophy can be summarised in the following five main principles:

- Peer-to-Peer
- Tools-based (microkernel)
- Multi-language
- Thin
- Free and open source.
- Covering each point in turn:

**Peer to Peer**: A sufficiently complex robot comprises several onboard computers or boards connected via Ethernet, plus sometimes offboard computers for intensive computation tasks. A peer-to-peer architecture coupled to a buffering system and a lookup system (a name service called ‘master’ in ROS), enables each component to dialogue directly with any other, synchronously or asynchronously as required.

**Multi-language**: ROS is language-neutral, and can be programmed in various languages. The ROS specification works at the messaging layer. Peer-to-peer connections are negotiated in XML-RPC, which exists in a great number of languages. To support a new language, either C++ classes are re-wrapped (which was done for the Octave client, for example) or classes are written enabling messages to be generated. These messages are described in IDL (Interface Definition Language).

**Tools-based**: Rather than a monolithic runtime environment, ROS adopted a microkernel design, which uses a large number of small tools to build and run the various ROS components. As you cover the ROS tutorials, you will learn to use several commands used to manipulate nodes and messages. Each command is in fact an executable. The advantage of this system is that a problem with one executable does not affect the others, which makes the system more robust and flexible than a system based on a centralised runtime environment.

**Thin**: To combat the development of algorithms that are entangled to a lesser or greater degree with the robotics OS and are therefore hard to reuse subsequently, ROS developers intend for drivers and other algorithms to be contained in standalone executables. This ensures maximum reusability and, above all, keeps its size down. This method makes ROS easy to use, the complexity being in the libraries. This arrangement also facilitates unit testing. Lastly, ROS uses code (drivers and algorithms) from other open source projects:

- Player/Stage project simulators
- Image processing and artificial vision libraries from OpenCV
- Planning algorithms from OpenRave

For a full list of the available algorithms, visit: http://www.ros.org/wiki/StackList

**Free and open source: We have already explained the reasons for this choice. Note however that the architecture chosen is consistent with that choice. ROS passes data between modules using inter-process communications and, as a result, modules do not need to be linked within a single process, thereby making the use of different licences a possibility.**

# The main principles of ROS
1. **Programming with ROS:**
ROS is language-independent. At this time, three main libraries have been defined for ROS, making it possible to program ROS in Python, Lisp or C++. In addition to these three libraries, two experimental libraries are offered, making it possible to program ROS in Java or Lua.

2. **A word about ROSJAVA and Android:**
Rosjava (http://code.google.com/p/rosjava/) is something different from the Java library found in ROS that we have just mentioned. Rosjava is a pure Java implementation of ROS created and maintained by Google and Willow Garage. Under Rosjava, instead of having a client library in Java giving access to the ROS core, which is written in C++, the Rosjava project totally rewrote the ROS core in Java. Google’s objective is to have a version of ROS that is fully compatible with Android, Google’s thin operating system. Rosjava can be used to control robots for which the operating system is not Linux, but Android (even if Android is based on Linux).

3. **ROS-compatible robots:**
The list of ROS-compatible robots grows constantly. For a full list, visit the Willow Garage website at http://www.ros.org/wiki/Robots
However, it is worth mentioning the best-known, namely NAO, Lego Mindstorms NXT, IRobot Roomba, TurtleBot and last but definitely not least, Willow Garage’s iconic PR2.

# The ROS file system

ROS resources are organised into a hierarchical structure on disc. Two important concepts stand out:

1. The package: the fundamental unit within ROS software organisation. A package is a directory containing nodes (nodes are explained below), external libraries, data, configuration files and one xml configuration file called manifest.xml.
2. The stack: a collection of packages. It offers a set of functionalities such as navigation, positioning, etc. A stack is a directory containing package directories plus a configuration file called stack.xml.

In addition to these two very important notions, the idea of ‘a distribution’ is also worth noting, which is, as in Linux, a collection of versioned stacks.

The latest ROS distributions to date:

- ROS Fuerte, published on 23 April 2012
- ROS Electric, published on 30 August 2011
- ROS Diamondback, published on 2 March 2011
- ROS C Turtle, published on 2 August 2010
- ROS Box Turtle, published on 2 March 2010

# Basic notions in ROS

The basic principle of a robot operating system is to run a great number of executables in parallel that need to be able to exchange data synchronously or asynchronously. For example, a robotics OS needs to query robot sensors at a set frequency (ultrasound or infra-red distance sensor, pressure sensor, temperature sensor, gyroscope, accelerometer, cameras, microphone, etc.), retrieve this data, process it (carry out what is known as a data merge), pass it to processing algorithms (speech processing, artificial vision, SLAM – simultaneous localisation and mapping, etc.) and lastly control the motors in return. This whole process is carried out continuously and in parallel. Moreover, the robotics OS needs to manage contention to ensure efficient access to robot resources.

The concepts brought together in ROS under the name of “ROS Computation Graph”, enabling these objectives to be reached, are described below. These are concepts used by the system as it is running, whereas the ROS File System described in the previous section is a static concept.

## Nodes
- ROS addresses this entire issue using some simple basic notions. The first of these is the notion of the node.
- In ROS, a node is an instance of an executable. A node may equate to a sensor, motor, processing or monitoring algorithm, and so on. Every node that starts running declares itself to the Master. This comes back to the microkernel architecture, whereby each resource is an independent node.

## Master
- The Master is a node declaration and registration service, which makes it possible for nodes to find each other and exchange data. The Master is implemented via XMLRPC.

The Master includes a heavily-used component called the Parameter Server, also implemented in the form of XMLRPC, and which is, as the name implies, a kind of centralised database within which nodes can store data and, in so doing, share system-wide parameters.

## Topics
- Data is exchanged asynchronously by means of a topic and synchronously via a service.
- A topic is a data transport system based on a subscribe/publish system. One or more nodes are able to publish data to a topic, and one or more nodes can read data on that topic. 
- A topic is, in a way, an asynchronous message bus, a little like an RSS feed. This notion of an asynchronous, many-to-many bus is essential in a distributed system situation.
- A topic is typed, meaning that the type of data published (the message) is always structured in the same way. Nodes send and receive messages on topics.

## Messages
- A message is a compound data structure. A message comprises a combination of primitive types (character strings, Booleans, integers, floating point, etc.) and messages (a message is a recursive structure). For example, a node representing a robot servo motor will certainly publish its status on a topic (depending how you programmed it) with a message containing, for instance, an integer representing the motor’s position, a floating point for its temperature, another floating point for its speed, and so on.
- The message description is stored in package_name/msg/myMessageType.msg. This file describes the message structure

## Services
- A topic is an asynchronous communication method used for many-to-many communication. A service meets a different kind of need; that for synchronous communication between two nodes. The idea is similar to that of a remote procedure call.
- The service description is stored in package_name/srv/myServiceType.srv. This file describes the data structures for requests and responses.

## Bags
- Bags are formats for storing and playing back message data. This mechanism makes it possible, for example, to collect data measured by sensors and subsequently play it back as many times as desired to simulate real data. It is also a very useful system for debugging a system after the event.
- The rosbag tool can be used to display data saved in bag files in graphical form
