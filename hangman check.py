# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 00:55:27 2017

@author: Adwait
"""
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    ans=True
    for let in secretWord:        
        if let in lettersGuessed:
            ans=ans and True
        else:
            ans=False
    return ans
    
            
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ans=''
    for k in secretWord:
        if k in lettersGuessed:
            ans=ans+k+''
        else:
            ans=ans+'_ '
    return ans



def getAvailableLetters(allLettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in allLettersGuessed:
        if let in l:
            l.remove(let)
    ans=''
    for nlet in l:
        ans=ans+nlet
    return ans



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long')
    lettersGuessed=[]
    allLettersGuessed=[]
    guesses=8
    print('-----------')
    
    
    while guesses>0:
        
        if isWordGuessed(secretWord, lettersGuessed)==True:
            print('Congratulations, you won!')
            break
        else:
            print('You have', guesses,'guesses left')
            print('Available Letters:', getAvailableLetters(allLettersGuessed))
            letterin=input('Please guess a letter: ')
            letter=letterin.lower()
            if letter not in getAvailableLetters(allLettersGuessed):
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            else:
                if letter in secretWord:
                    lettersGuessed+=letter
                    allLettersGuessed+=letter
                    print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
                else:
                    print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
                    allLettersGuessed+=letter
                    guesses-=1
        print('-----------')
    if isWordGuessed(secretWord, lettersGuessed)==False:
        print('Sorry, you ran out of guesses. The word was', secretWord)
            