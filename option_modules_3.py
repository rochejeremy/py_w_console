from classes.awsClasses import InstanceManager

def exec_option3():
    """Bootstrap Console Instance """
    print("Stop Instance i-033182bde833796cb")

    #start up the instace
    instance = InstanceManager()
    instance.stopInstance('i-033182bde833796cb')

    #reomte command to bootstrap tools






