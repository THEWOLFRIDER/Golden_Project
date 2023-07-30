'''
Hello Everyone , 
I am Om Pratap Singh
Python Development Intern at CodeClause
So this is My Golden Project : Plagiarism Checker in Python 
'''
'''
Q1:- What is Plagiarism?
Plagiarism is simply called cheating. 
When one person copies the work or idea of another person and uses that in their work by their name it is called plagiarism.

Q2:- Difflib Module
 In Python, there are various built-in modules used for making different tasks easy and difflib module is one of them.
 This module provides different functions and classes by using which we can compare the data sets. 
 In this article, we are going to use SequenceMatcher() function class of this module.
'''
# Importing SequenceMatcher
# from difflib module
from difflib import SequenceMatcher

# Declaring string 
string1 = str(input()) # To take input from user
string2 = 'Hi everyone , I am Om Pratap singh. I am Pursuing my Btech from galgotias college of engineering and technology.'

# Using the SequenceMatcher()
match = SequenceMatcher(None, string1, string2)

# convert above output into ratio
# and multiplying it with 100
result = match.ratio() * 100

# Display the final result
print('Plagiarism: ',int(result), "%")


# Thank You