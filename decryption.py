#HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "Downloads/code_ProblemSet6/words.txt"

# -----------------------------------
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("Downloads/code_ProblemSet6/story.txt", "r").read()
# -----------------------------------

#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    lower = string.ascii_lowercase*2
    upper = string.ascii_uppercase*2
    dic = {'a': lower[shift], 'b': lower[1+shift], 'c': lower[2+shift], 'd': 
    lower[3+shift], 'e': lower[4+shift], 'f': lower[5+shift], 'g': lower[6+shift],
    'h': lower[7+shift], 'i': lower[8+shift], 'j': lower[9+shift], 'k': lower[10+shift]
    , 'l': lower[11+shift], 'm': lower[12+shift], 'n': lower[13+shift], 'o':
    lower[14+shift], 'p': lower[15+shift], 'q': lower[16+shift], 'r': lower[17+shift]
    , 's': lower[18+shift], 't': lower[19+shift], 'u': lower[20+shift], 
    'v': lower[21+shift], 'w': lower[22+shift], 'x': lower[23+shift], 'y':
    lower[24+shift], 'z': lower[25+shift], 'A': upper[shift], 'B': upper[1+shift]
    , 'C': upper[2+shift], 'D': upper[3+shift], 'E': upper[4+shift], 'F': upper[5+shift]
    , 'G': upper[6+shift], 'H': upper[7+shift], 'I': upper[8+shift], 'J': upper[9+shift]
    , 'K': upper[10+shift], 'L': upper[11+shift], 'M': upper[12+shift], 'N': upper[13+shift]
    , 'O': upper[14+shift], 'P': upper[15+shift], 'Q': upper[16+shift], 'R': upper[17+shift]
    , 'S': upper[18+shift], 'T': upper[19+shift], 'U': upper[20+shift], 'V': upper[21+shift]
    , 'W': upper[22+shift], 'X': upper[23+shift], 'Y': upper[24+shift], 'Z': upper[25+shift]}
    return dic

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    message = ''
    for letter in text:
        if letter in coder.keys():
            message += str(coder.get(letter))
        else:
            message += str(letter)
    return message

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    shift = 0
    temp_count = 0
    new_shift = 0
    while shift < 26:
        message = ''
        last_count = temp_count
        message = applyShift(text, shift).split(' ')
        for word in message:
            if isWord(wordList, word):
                temp_count += 1
        if temp_count > last_count:
            new_shift = shift
        shift += 1
    return new_shift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    story = getStoryString()
    best_shift = findBestShift(loadWords(), story)
    message = str(applyShift(story, best_shift))
    return message
    
print decryptStory()

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    #wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
        decryptStory()
