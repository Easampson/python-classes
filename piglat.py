#!usr/bin/env python


vowels = "aeiouy"
clusters = ["kn", "sh", "ch", "th", "wh", "ph", "gh", "ng","br", "cr", "dr", "fr", "gr", "pr", "tr", "sc", "sk", "sl", "sm", "sn", "sp", "st", "sw"]

def vowel_shifter(word0):
    return word0 + "way"

def cluster_shifter(word0):
    front = word0[:2]
    word0 = word0[2:] + front
    return word0 + "ay"

def const_shifter(word0):
    front = word0[:1]
    word0 = word0[1:] + front
    return word0 + "ay"

# checks for the first 2 letters in a word to
# determine which function to pass the string
def letter_check(word):
    word = word.lower()
    if word[0] in vowels:
       return vowel_shifter(word)
    elif word[:2] in clusters:
       return cluster_shifter(word)
    else:
       return const_shifter(word)

# splits the input (sentence) string to words
# and passes them to letter_check() to which they
# are returned to a string and concatonated to 
# followed by space strings
def to_piglat(not_piglat):
    eng_strgs = not_piglat.split()
    pig_strg = ''
    for a in eng_strgs:
        pig_strg += letter_check(a)
 	pig_strg += ' '
    return pig_strg    

# starts the program prompting user and passing 
# input to worker function
def main():
    the_string = raw_input("I am Piglat. I turn American English into Pig-latin. Enter phrase now: \n")
    print "\n" + to_piglat(the_string)
    print ("\nHave nice day, goodbye")
    
main()
