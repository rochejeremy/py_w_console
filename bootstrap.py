#from classes.utilityClasses import Notification
#from classes.utilityClasses import RandomWords
import json
from classes.utilityClasses import RemoteBootStrapIVMS
#from classes.awsClasses import MetaData
from classes.awsClasses import InstanceManager
#import json

# Return to random words
#mywords = RandomWords()
#mywords = mywords.getTwoRandomWords()
#mywords = json.loads(mywords)
#print(mywords)

    # Create a notification
#notification = Notification("A new Notification", "https://appblepear.example.com")

    # Send the notification
#response =notification.send()
#print(response)

    # Get IPv4 Address
#metadata = MetaData()
#ip_address = metadata.getIPv4()
#print(ip_address)

remote_ivms = RemoteBootStrapIVMS()
print(remote_ivms.get_remote_info())
