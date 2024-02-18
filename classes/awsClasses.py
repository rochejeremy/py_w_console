import logger
import boto3
import subprocess
import json
import requests
import time
from botocore.exceptions import ClientError


class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""

    def __init__(self, sns_resource):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sns_resource

    def publish_message(topic, message, attributes):
        """
        Publishes a message, with attributes, to a topic. Subscriptions can be filtered
        based on message attributes so that a subscription receives messages only
        when specified attributes are present.

        :param topic: The topic to publish to.
        :param message: The message to publish.
        :param attributes: The key-value attributes to attach to the message. Values
                           must be either `str` or `bytes`.
        :return: The ID of the message.
        """
        try:
            att_dict = {}
            for key, value in attributes.items():
                if isinstance(value, str):
                    att_dict[key] = {
                        'DataType': 'String', 'StringValue': value}
                elif isinstance(value, bytes):
                    att_dict[key] = {
                        'DataType': 'Binary', 'BinaryValue': value}
            response = topic.publish(
                Message=message, MessageAttributes=att_dict)
            message_id = response['MessageId']
            logger.info(
                "Published message with attributes %s to topic %s.", attributes,
                topic.arn)
        except ClientError:
            logger.exception(
                "Couldn't publish message to topic %s.", topic.arn)
            raise
        else:
            return message_id
class InstanceManager:
    """ Manage an instance through SSH """
    #Class Attributes
    #INSTANCE_ID = 'i-033182bde833796cb'
    AWS_REGION = "us-east-2"

    def startInstance(self, INSTANCE_ID):    
        EC2_RESOURCE = boto3.resource('ec2', region_name=self.AWS_REGION)
        instance = EC2_RESOURCE.Instance(INSTANCE_ID)
        instance.start()
        instance.wait_until_running()
        while instance.state['Name'] not in ('running'):
            time.sleep(5)
            instance.load()
            print(f'EC2 instance "{instance.id}" is starting')
        print(f'EC2 instance "{instance.id}" has been started')
        print(f'Public IPv4 address: {instance.public_ip_address}')
    
    def stopInstance(self, INSTANCE_ID):
        EC2_RESOURCE = boto3.resource('ec2', region_name=self.AWS_REGION)
        instance = EC2_RESOURCE.Instance(INSTANCE_ID)
        instance.stop()
        while instance.state['Name'] not in ('stopped'):
            time.sleep(5)
            instance.load()
            print(f'EC2 instance "{instance.id}" is stopping')
    def getSecurityGroup(self, INSTANCE_ID):
        EC2_RESOURCE = boto3.resource('ec2', region_name=self.AWS_REGION)
        instance = EC2_RESOURCE.Instance(INSTANCE_ID)

class MetaData:
    """ Interact with MetaData Service V2"""
    #Class Attributes
    meta_data_endpoint = "http://169.254.169.254/latest/"
    
    def __init__(self):
        pass

    def getIPv4(self):
        try:
            token = requests.put(self.meta_data_endpoint + "api/token",
                             headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"})
            response = requests.get(self.meta_data_endpoint + "meta-data/public-ipv4",
                                headers={"X-aws-ec2-metadata-token": token.text})
            return(response.text)
        except requests.exceptions.RequestException as e:
            print(e)
            return None 

class SecurityGroupManager:
    """ Manage Security Groups """
    """ input IP, port, instanceID and unique description. Add them to the group, Then find the entries with same port and desciption 
    and remove them """
    
    #Class Attributes
    
    

    def __init__(self):
        pass
       
    
    def updateSg(self, SSH_CLIENT_IP):
        """
        Replace the security group  with the security group rule containing your IP you SSH from.
        """
        SecGroupRuleID = "sgr-03a24f42370f46326"
        SecGroupID = "sg-02b30b4f4c9682563"
        ip = SSH_CLIENT_IP
        ec2 = boto3.client('ec2')
        sg_rules_list = [{'SecurityGroupRuleId': f'{SecGroupRuleID}',
                          'SecurityGroupRule': {
                              'IpProtocol': 'tcp',
                              'FromPort': 22,
                              'ToPort': 22,
                              'CidrIpv4': f'{ip}/32',
                              'Description': 'SSH port via script for 1.1.1.1'
                          }
                          }
                         ]
        print("starting update")
        try:
            # replace the below with the security group ID that contains the SG Rule
            response = ec2.modify_security_group_rules(
                GroupId=SecGroupID, SecurityGroupRules=sg_rules_list)
            print(
                f"Response code = {response['ResponseMetadata']['HTTPStatusCode']}")
        except ClientError as e:
            print(e)
    def updateRemoteSg(self, SSH_CLIENT_IP):
            """
            Replace the security group  with the security group rule containing your IP you SSH from.
            """
            #SecGroupRuleID = "sgr-039b4cd2757ad1a77"
            SecGroupID = "sg-0b87a7028c315da8c"
            ip = SSH_CLIENT_IP
            ec2 = boto3.client('ec2')
            sg_rules_list = [{'SecurityGroupRuleId': 'sgr-00bbcdfc48a615d01',
                              'SecurityGroupRule': {
                                  'IpProtocol': 'tcp',
                                  'FromPort': 22,
                                  'ToPort': 22,
                                  'CidrIpv4': f'{ip}/32',
                                  'Description': f'SSH for remote {SSH_CLIENT_IP} '
                              }
                              },
                              {'SecurityGroupRuleId': f'sgr-07149726ba97e226b',
                              'SecurityGroupRule': {
                                  'IpProtocol': 'tcp',
                                  'FromPort': 8443,
                                  'ToPort': 8443,
                                  'CidrIpv4': f'{ip}/32',
                                  'Description': f'8443 for remote {SSH_CLIENT_IP} '
                              }
                              }
                             ]
            print("starting update")
            try:
                # replace the below with the security group ID that contains the SG Rule
                response = ec2.modify_security_group_rules(
                    GroupId=SecGroupID, SecurityGroupRules=sg_rules_list)
                print(
                    f"Response code = {response['ResponseMetadata']['HTTPStatusCode']}")
            except ClientError as e:
                print(e)
