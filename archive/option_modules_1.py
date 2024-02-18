import requests
import boto3
import classes.awsClasses

meta_data_endpoint = "http://169.254.169.254/latest/"
    
def exec_option1():

    print("Getting IP Address")
    token = requests.put(meta_data_endpoint + "api/token",
                         headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"})

    response = requests.get(meta_data_endpoint + "meta-data/public-ipv4", headers={"X-aws-ec2-metadata-token": token.text})
    print(response.text)
    option = int(input('Enter your choice: '))
    
    
    
    
