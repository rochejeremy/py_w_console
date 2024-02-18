import logging
import requests
import boto3

headers={'User-Agent': 'requests/2.2.15'}



logging.basicConfig(filename='/home/ec2-user/py_w_console/logs/ps_access2.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def rest_get_request(url):
    """ Make a URL get request with logging """
    try:
        response = requests.get(url, headers)
        response.raise_for_status()
        logging.info(f"GET request to {url} successful.")
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"GET request to {url} failed: {str(e)}")

"""Get Public IP"""
checkip = rest_get_request("https://checkip.amazonaws.com")
ip = checkip.text.split(" ")[0].rstrip()
logging.info(f"request results {ip}")

""" Get Password from Parameter Store """
ssm_client = boto3.client('ssm')
DNSkey = ssm_client.get_parameter(Name="DNSKey", WithDecryption=True)
secret = DNSkey['Parameter']['Value']
logging.info(f"DNSKey donwloaded")

""" build URL for request to Google Domains """
URL_STEM = "domains.google.com/nic/update?hostname="
HOSTNAME = "gammadrum.viginti.one"
URI_QUERY = "&myip="
google_url = "https://" + secret + "@" + URL_STEM + HOSTNAME + URI_QUERY + ip

""" Make Request to Google """
dns_update = rest_get_request(google_url)
logging.info(f"dns update {dns_update}")
