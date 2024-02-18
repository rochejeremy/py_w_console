import json
import boto3
import datetime

now = datetime.datetime.now()

formatted_string = now.strftime("%b-%d at %I:%M %p GMT")

print(formatted_string)


sns_client = boto3.client('sns')
MessageArn = "arn:aws:sns:us-east-2:271875751869:mymessagedeliv"
subject = "New Notification " + formatted_string
print(subject)
Title = "Notification Info"
alink = "http://applepotatoe.jeremyroche.net" 

def write_break(str_input, str_character):
    #counter = len(str_input)
    out_str = str_character
    for i in range(len(str_input)):
        out_str += str_character    
    return out_str

title_break = write_break(Title,"=")
link_break = write_break(alink,"..")
message = f"""
{title_break}
{Title}
{title_break}

[  ] check that the correct outbound IP is being used
[  ] check that the fingerprint is correct

{link_break}
{alink}
{link_break}
"""
print(message)
response = sns_client.publish(TargetArn=MessageArn, Message=message,Subject=subject)
print(response)
