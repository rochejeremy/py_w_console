import boto3
import requests
import json
import logging

ip_url = "https://checkip.amazonaws.com"
response = requests.get(ip_url)
ip = response.text.split(" ")[0].rstrip()

#ip="3.17.77.37"
URL_STEM = "domains.google.com/nic/update?hostname="
HOSTNAME = "gammadrum.viginti.one"
URI_QUERY = "&myip=" 

ssm_client = boto3.client('ssm')
DNSkey = ssm_client.get_parameter(Name="DNSKey", WithDecryption=True)
secret = DNSkey['Parameter']['Value']
url = "https://" + secret + "@" + URL_STEM + HOSTNAME + URI_QUERY + ip
headers={'User-Agent': 'requests/2.2.15'}

response = requests.get(url, headers)

if response.status_code != 200:
    print("The request failed with status code {}.".format(response.status_code))

# Handle the response
if response.status_code == 200:
    # The request was successful
    # Do something with the response data
    response_data = response.content
    for c in response.iter_lines():
        print(c.decode('utf-8'))
    # The request failed
    # Handle the error
else:
    print("The request failed with status code {}.".format(response.status_code))


