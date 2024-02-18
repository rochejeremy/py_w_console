from classes.awsClasses import InstanceManager
from classes.awsClasses import SecurityGroupManager

def exec_option1():
    """Bootstrap Console Instance """
    print("Starting Instance i-033182bde833796cb")

    #start up the instace
    instance = InstanceManager()
    instance.startInstance('i-033182bde833796cb')

    #print("updating security group")
    #security group update
    #securitygroup = SecurityGroupManager()
    #securitygroup.updateSg()

    #reomte command to bootstrap tools






