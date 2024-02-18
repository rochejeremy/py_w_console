from classes.awsClasses import InstanceManager
from classes.awsClasses import SecurityGroupManager
import logger
import os

def exec_option5():
    """Updating Security Group on Assets """
    print("Updating Security Group on Assets")
    SSH_CLIENT_IP = os.environ.get('SSH_CLIENT').split(' ')
    print("updating security group")
     
    securitygroup = SecurityGroupManager()
    securitygroup.updateRemoteSg(SSH_CLIENT_IP[0].strip())
    






exec_option5()
