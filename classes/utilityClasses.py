import json
import boto3
import datetime
import requests
import random
import json
import subprocess

class RandomWords:
    """A class that generates two random words from a wordlist"""
    #Class Attributes
    
    #def __init__(self):

    def getTwoRandomWords(self):
        """Open the wordlist file in read mode."""
        with open("include/wordlist.txt", "r") as f:
        
            # check the file opened
            if not f:
                 print("The wordlist file count not open.")
                 exit(1)
            """Read all the words from the file"""
            words = f.read().split()
    
            """Check if the file is empty"""
            if not words:
                 print("The wordlist file is empty.")
                 exit(1)
    
            """Generate two random numbers between 0 and the number of words in the file."""
            random_word_1 = random.randint(0, len(words) - 1)
            random_word_2 = random.randint(0, len(words) - 1)
    
        """Check if the two random numbers are the same"""
        while random_word_1 == random_word_2:
            random_word_2 = random.randint(0, len(words) - random.randint(0, len(words) - 1))
        two_words = (words[random_word_1], words[random_word_2])
        json_random_words = json.dumps(two_words)        
        """return the JSON"""
        return(two_words)


class BgColors:
    """ Used to format Menu text see table in ./README.md """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    MAINMENU = '\u001b[33m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Notification:
    """A class that represents a notification."""
    # Class attributes
    
    def __init__(self, title, alink):
        """The constructor for the Notification class."""
        MessageArn = "arn:aws:sns:us-east-2:271875751869:mymessagedeliv"
        self.title = title
        self.alink = alink
        self.MessageArn = MessageArn

    def write_break(self, str_input, str_character):
        """Returns a string with the given a given character repeated to create nice breaks."""
        out_str = str_character
        for i in range(len(str_input)):
            out_str += str_character
        return out_str
    
    def send(self):
        """Sends the notification."""
        now = datetime.datetime.now()
        date_string = now.strftime("%b-%d at %I:%M %p GMT")
        subject = self.title + " " + date_string
        title_break = self.write_break(self.title, "=")
        link_break = self.write_break(self.alink, "..")
        message = f"""
        {title_break}
        {self.title}
        {title_break}

        [  ] check that the correct outbound IP is being used
        [  ] check that the fingerprint is correct

        {link_break}
        {self.alink}
        {link_break}

        """
        sns_client = boto3.client('sns')
        response = sns_client.publish(
            TargetArn=self.MessageArn,
            Message=message,
            Subject=subject,
        )
        return(response)

