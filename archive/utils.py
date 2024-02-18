import requests
import random
import json


# This fucntion reads in 2 random words from a wordlist file called `wordlist.txt`.
def getTwoRandomWords():

# Open the wordlist file in read mode.
     with open("../include/wordlist.txt", "r") as f:
     
         #check the file opened
         if not f:
             print("The wordlist file count not open.")
             exit(1)

         # Read all the words from the file.
         words = f.read().split()
     
         # Check if the file is empty.
         if not words:
             print("The wordlist file is empty.")
             exit(1)
     
         # Generate three random numbers between 0 and the number of words in the file.
         random_word_1 = random.randint(0, len(words) - 1)
         random_word_2 = random.randint(0, len(words) - 1)
         
     
         # Check if the two random numbers are the same.
         while random_word_1 == random_word_2:
             random_word_2 = random.randint(
                 0, len(words) - random.randint(0, len(words) - 1))
         two_words = (words[random_word_1], words[random_word_2])
         # Print the two random words.
         #print("The two random words are:",
         #      words[random_word_1], words[random_word_2])
         # Convert the dictionary to JSON.
         json_random_words = json.dumps(two_words)

        # Print the JSON.
         print(json_random_words)



getTwoRandomWords()
