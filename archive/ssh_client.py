import subprocess
import os

SSH_CLIENT_IP = os.environ.get('SSH_CLIENT').split(' ')
print(SSH_CLIENT_IP[0])
