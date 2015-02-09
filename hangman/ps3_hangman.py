# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/ddeiveegan/python/python/hangman/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    result = True
    for letter in secretWord :
        if letter in lettersGuessed :
            continue
        else :
            return False
    return result



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord :
        if letter in lettersGuessed :
            result += letter+' '
        else :
            result += '_ ' 
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = string.ascii_lowercase
    remainingLetters = ""
    for letter in allLetters:
        if letter not in lettersGuessed :
            remainingLetters += letter
    return remainingLetters

def isLetterInWord(secretWord, letter):
    if letter in secretWord :
        return True
    else :
        return False

def goodGuess(secretWord, lettersGuessed) :
    resultStr = "Good guess: "+getGuessedWord(secretWord,lettersGuessed)
    return resultStr

def badGuess(secretWord, lettersGuessed):
    resultStr = "Oops! That letter is not in my word: "+getGuessedWord(secretWord,lettersGuessed)
    return resultStr

def sameGuess(secretWord, lettersGuessed):
    resultStr = "Oops! You've already guessed that letter: "+getGuessedWord(secretWord,lettersGuessed)
    return resultStr
    
def isLetterAlreadyGuessed(letter, lettersGuessed):
    if letter in lettersGuessed :
        return True
    else :
        return False

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
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+str(len(secretWord))+" letters long."
    print "----------"
    numberOfGuesses = 8
    userLetter = ""
    lettersGuessed = []
    while numberOfGuesses > 0 :
        print "You have "+str(numberOfGuesses)+" guesses left."
        print "Available letters: "+getAvailableLetters(lettersGuessed)
        userLetter = raw_input("Please guess a letter: ")
        userLetter = userLetter.lower()
        if(isLetterAlreadyGuessed(userLetter,lettersGuessed)) :
            print sameGuess(secretWord, lettersGuessed)
            print "-----------"
        else :
            lettersGuessed.append(userLetter)
            if(isWordGuessed(secretWord, lettersGuessed)) :
                print goodGuess(secretWord,lettersGuessed)
                print "----------"
                break
            else :
                if(isLetterInWord(secretWord, userLetter)) :
                    print goodGuess(secretWord,lettersGuessed)
                    print "----------"
                else :
                    print badGuess(secretWord,lettersGuessed)
                    print "----------"
                    numberOfGuesses -= 1
    if numberOfGuesses > 0:
        print "Congratulations, you won!"
    else :
        print "Sorry, you ran out of guesses. The word was "+secretWord



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = "dinesh"
hangman(secretWord)
