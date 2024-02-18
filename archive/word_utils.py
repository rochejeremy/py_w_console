import requests
import random
import json
import re


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
         t_words = [word for word in words if re.match(r'(t.*)', word)]
         n_words = [word for word in words if re.match(r'(n.*)', word)]
         c_words = [word for word in words if re.match(r'(c.*)', word)]
         
         # Check if the file is empty.
         if not words:
             print("The wordlist file is empty.")
             exit(1)
     
         # Generate three random numbers between 0 and the number of words in the file.
         random_t_word = random.randint(0, len(t_words) - 1)
         random_n_word = random.randint(0, len(n_words) - 1)
         random_c_word = random.randint(0, len(c_words) - 1) 
         
     
         # Check if the two random numbers are the same.
         three_words = (t_words[random_t_word], n_words[random_n_word], c_words[random_c_word])
         # Print the two random words.
         #print("The two random words are:",
         #      words[random_word_1], words[random_word_2])
         # Convert the dictionary to JSON.
         json_random_words = json.dumps(three_words)

        # Print the JSON.
        # print(json_random_words)
         print(t_words[random_t_word] + n_words[random_n_word] + c_words[random_c_word])



getTwoRandomWords()
