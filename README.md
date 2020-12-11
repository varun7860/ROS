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

Peer-to-Peer
Tools-based (microkernel)
Multi-language
Thin
Free and open source.
Covering each point in turn:

Peer to Peer: A sufficiently complex robot comprises several onboard computers or boards connected via Ethernet, plus sometimes offboard computers for intensive computation tasks. A peer-to-peer architecture coupled to a buffering system and a lookup system (a name service called ‘master’ in ROS), enables each component to dialogue directly with any other, synchronously or asynchronously as required.

Multi-language: ROS is language-neutral, and can be programmed in various languages. The ROS specification works at the messaging layer. Peer-to-peer connections are negotiated in XML-RPC, which exists in a great number of languages. To support a new language, either C++ classes are re-wrapped (which was done for the Octave client, for example) or classes are written enabling messages to be generated. These messages are described in IDL (Interface Definition Language).

Tools-based: Rather than a monolithic runtime environment, ROS adopted a microkernel design, which uses a large number of small tools to build and run the various ROS components. As you cover the ROS tutorials, you will learn to use several commands used to manipulate nodes and messages. Each command is in fact an executable. The advantage of this system is that a problem with one executable does not affect the others, which makes the system more robust and flexible than a system based on a centralised runtime environment.

Thin: To combat the development of algorithms that are entangled to a lesser or greater degree with the robotics OS and are therefore hard to reuse subsequently, ROS developers intend for drivers and other algorithms to be contained in standalone executables. This ensures maximum reusability and, above all, keeps its size down. This method makes ROS easy to use, the complexity being in the libraries. This arrangement also facilitates unit testing. Lastly, ROS uses code (drivers and algorithms) from other open source projects:

Player/Stage project simulators
Image processing and artificial vision libraries from OpenCV
Planning algorithms from OpenRave
etc
For a full list of the available algorithms, visit: http://www.ros.org/wiki/StackList

Free and open source: We have already explained the reasons for this choice. Note however that the architecture chosen is consistent with that choice. ROS passes data between modules using inter-process communications and, as a result, modules do not need to be linked within a single process, thereby making the use of different licences a possibility.

