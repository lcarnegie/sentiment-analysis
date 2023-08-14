"""
1. Create the files and sample data needed to do the analysis 
2. Get matplotlib working so that it just outputs a picture of the analysis

"""
import matplotlib.pyplot as plt

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of words to use
positive_words = []
negative_words = []

#populate positive words 
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
#populate negative words
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(strin):
    """
    Removes punctuation characters from a string.

    Parameters:
    strin (str): The input string from which punctuation characters will be removed.

    Returns:
    str: The input string with punctuation characters removed.
    """
    for char in punctuation_chars: 
        strin = strin.replace(char, "")
    return strin 

def get_pos(sentence):
    """
    Count the number of positive words in a sentence.

    Parameters:
    sentence (str): The input sentence.

    Returns:
    int: The number of positive words in the sentence.

    """
    num_p_words = 0
    
    words = sentence.lower().split(" ")
    
    for word in words: 
        if strip_punctuation(word) in positive_words:
            num_p_words += 1
    
    return num_p_words

def get_neg(sentence): 
    """
    Counts the number of negative words in a sentence.

    Parameters:
    sentence (str): The input sentence.
    negative_words (list): A list of negative words.

    Returns:
    int: The number of negative words in the sentence.
    """
    num_n_words = 0
    
    words = sentence.lower().split(" ")
    
    for word in words: 
        if strip_punctuation(word) in negative_words:
            num_n_words += 1
    
    return num_n_words

# An 2D array with the data from the raw tweets.
file = open("project_twitter_data.csv", 'r')  # Open the file in read mode
lines = file.readlines()  # Read all the lines from the file

"""
File Organization: 
    0: tweet text
    1: retweets
    2: number of replies
"""

tweet_data = [] 

for row in lines[1:]:  
    tweet_data.append(row.strip().split(','))  

# Create .csv file that outputs (Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score) for each tweet
outfile = open("resulting_data.csv", 'w')  # Open a new file in write mode
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')  # Write the header row
outfile.write('\n')  # Write a new line character

x = [] # Net Score
y = [] # Number of Retweets

for tweet in tweet_data: 
    text = tweet[0]  # Get the tweet text
    retweets = tweet[1]
    replies = tweet[2]
    p_score = get_pos(text)  
    n_score = get_neg(text)  
    net_score = p_score - n_score  # Calculate the net score
    x.append(int(net_score)) #convert value from file from String to int, so it's usable by pyplot
    y.append(int(retweets))
    row_string = '{}, {}, {}, {}, {}'.format(retweets, replies, p_score, n_score, net_score)  # Create a string with the values
    outfile.write(row_string)  # Write the row string to the file
    outfile.write('\n') 


# Make a graph with matplotlib

plt.scatter(x, y)
plt.ylabel('Retweets')
plt.xlabel('Net Positivity Score')
plt.show()


# Close the files
file.close()
outfile.close()
    



