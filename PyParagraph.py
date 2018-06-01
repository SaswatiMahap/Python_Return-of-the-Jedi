import os
import csv
import array
import pandas as pd
import re




# Open the file in "read" mode ('r') and store the contents in the variable "text"


    # Store all of the text inside a variable called "lines"
 

    # Print the contents of the text file
 
    

# Import a text file filled with a paragraph of your choosing.

file = 'paragraph_2.txt'


# # Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:
    # print(text)

    lines = text.read()
    #print(lines)

# * Approximate word count

    words_cnt = len(lines.split(" "))
    print('Approximate word count:',words_cnt)

#   * Approximate sentence count
    sen = (len(lines.split("."))-1)
    print('Approximate sentence count:',sen)
    
#   * Approximate letter count (per word)
    words = lines.split(" ")
    average = sum(len(word) for word in words) / len(words)
    print ('Approximate letter count:',average)

#   * Average sentence length (in words)
       

average=0
average = words_cnt/sen
print ('The average amount of words in the sentence is' ,average, 'words')

# # Paragraph Analysis
# # -----------------
# # Approximate Word Count: 122
# # Approximate Sentence Count: 5
# # Average Letter Count: 4.56557377049
# # Average Sentence Length: 24.4
# # ```

# # * 
# # **Special Hint:** You may find this code snippet helpful when determining sentence length 
# # (look into [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) if interested in learning more):
# # ```python
# import re
# re.split("(?&lt;=[.!?]) +", paragraph)

# sentences = re.split(r' *[\.\?!][\'"\)\]]* *', lines)

# # for stuff in sentences:
# #     print(stuff) 

# nbrChar = 0
# average=0
# for word in sentences:
#     nbrChar+= len(word)
#     average= nbrChar // len(sentences)


