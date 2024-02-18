from classes.awsClasses import InstanceManager
from classes.awsClasses import SecurityGroupManager
import logger
import os

def exec_option4():
    """Updating Security Group on Assets """
    print("Updating Security Group on Assets")
    SSH_CLIENT_INFO = os.environ.get('SSH_CLIENT').split(' ')
    print(SSH_CLIENT_INFO[0])
    #SSH_CLIENT_IP = "3.138.67.39" 

    print("updating security group")
    #security group update
    securitygroup = SecurityGroupManager()
    securitygroup.updateRemoteSg(SSH_CLIENT_INFO[0])
    

    #reomte command to bootstrap tools






