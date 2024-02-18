
import json
import subprocess
import boto3
#from classes.awsClasses import InstanceManager

def exec_option2():
    print("Initializing Remote Command")
    AWS_REGION = "us-east-2"
    EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
    INSTANCE_ID = 'i-033182bde833796cb'
    instance = EC2_RESOURCE.Instance(INSTANCE_ID)
    #instance.wait_until_running()
    #print(f'EC2 instance "{instance.id}" is running')
    print(f'Public IPv4 address: {instance.public_ip_address}')

    cmd = "ssh ec2-user@" + str(instance.public_ip_address) + \
        " -i ~/.ssh/isolated-vm-key.pem '/usr/bin/pwsh /home/ec2-user/bootstrap-isolated-vm-services.psh'"
    print(cmd)
    result = json.loads(getProcessOutput(cmd))
    print(result['ConnectionInfo'])

    

    


def getProcessOutput(cmd):
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE)
    process.wait()
    data, err = process.communicate()
    if process.returncode == 0:
        return data.decode('utf-8')
    else:
        print("Error:", err)
    return ""






