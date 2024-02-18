import boto3
import subprocess
import json


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


AWS_REGION = "us-east-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = 'i-033182bde833796cb'
instance = EC2_RESOURCE.Instance(INSTANCE_ID)
#instance.start()
#print(f'Starting EC2 instance: {instance.id}')
    
instance.wait_until_running()
print(f'EC2 instance "{instance.id}" has been started')
print(f'Public IPv4 address: {instance.public_ip_address}')

cmd = "ssh ec2-user@" + str(instance.public_ip_address) + " -i ~/.ssh/isolated-vm-key.pem '/usr/bin/pwsh /home/ec2-user/bootstrap-isolated-vm-services.psh'"

result = json.loads(getProcessOutput(cmd))
print(result['ConnectionInfo'])

