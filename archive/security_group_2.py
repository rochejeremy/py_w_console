import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')

SecGroupRuleID = "sgr-03a24f42370f46326"
SecGroupID="sg-02b30b4f4c9682563" 
ip="8.8.8.8" 



def des_sg(SecGroupRuleID, ip, SecGroupID):
    """
    Replace the security group  with the security group rule containing your IP you SSH from.
    """
    sg_rules_list = [{'SecurityGroupRuleId': f'{SecGroupRuleID}',
                  'SecurityGroupRule': {
                      'IpProtocol': 'tcp',
                      'FromPort': 22,
                      'ToPort': 22,
                      'CidrIpv4': f'{ip}/32',
                      'Description': 'Added SSH port via script for 8.8.8.8'
                  }
                  }
                 ]
    try:
        ## replace the below with the security group ID that contains the SG Rule
        response = ec2.modify_security_group_rules(GroupId=SecGroupID, SecurityGroupRules=sg_rules_list)
        print(f"Response code = {response['ResponseMetadata']['HTTPStatusCode']}")
    except ClientError as e:
        print(e)

des_sg(SecGroupRuleID, ip, SecGroupID)



















#Security_Group_Name = "jumpboxssh"
# Get the security group ID
#filters = [{'Name': 'tag:Name', 'Values': ['Isolated-vm-test']}]

#describe_instances_response = ec2.describe_instances(Filters=filters)
#for res in describe_instances_response["Reservations"]:
#    security_groups = res["Instances"][0]["SecurityGroups"]
#    for sg in security_groups:
#         print(sg['GroupName'] + " " + sg['GroupId'])
#         if sg['GroupName'] == Security_Group_Name:
#             New_GroupId = sg['GroupId']
#print('new sg is ' + New_GroupId)

# Detach from Instance

# Delete Security Group
#try:
#    response = ec2.delete_security_group(GroupName=Security_Group_Name)
#    print('Security Group Deleted')
#except ClientError as e:
#    print(e)


# Create the security Group
#try:
#    response = ec2.create_security_group(GroupName=Security_Group_Name,
#                                         Description='DESCRIPTION',
#                                         VpcId='vpc-6ff65106')
#    security_group_id = response['GroupId']
#    print('Security Group Created %s in vpc %s.' % (security_group_id, 'vpc-6ff65106'))
#    data = ec2.authorize_security_group_ingress(
#        GroupId=security_group_id,
#        IpPermissions=[
#            {'IpProtocol': 'tcp',
#             'FromPort': 22,
#             'ToPort': 22,
#             'IpRanges': [{'CidrIp': '3.137.179.211/32'}]}
#        ])
#    print('Ingress Successfully Set %s' % data)
#except ClientError as e:
#    print(e)



# Attach to Instance 
