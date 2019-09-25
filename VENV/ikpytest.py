from ikpy.chain import Chain
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D

ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')

my_chain = Chain.from_urdf_file("urdf/iCook.urdf")

joint_angles = my_chain.inverse_kinematics([[1, 0, 0, 1],
                             [0, 1, 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])

my_chain.plot(joint_angles, ax)
matplotlib.pyplot.show()