import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/exouser/URDF_2_Moveit_Lecture/Lab1/install/buzz_arm_planning_lab'
