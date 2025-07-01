
def intersection(foo:str, bar:str) -> str | None:
    result = ''
    for ch in foo:
        if ch in bar and ch not in result: # not duplicates
            result = result + ch #nothing + intersection of characters
    return result if result else None # result is none if there is no intersection

def is_alphabetical(string:str) -> bool:
    valid = True
    for i in range(len(string)):
        ascii = ord(string[i]) #changes string into ascii
        if not (97 <= ascii <= 122):
            valid = False # if not a letter return flase
        if i > 0 and ord(ascii[i - 1]) > ascii:
            valid = False # if not alphabetical return false
    return valid

def letters_only(string:str) -> str | None:
    result = ''
    for i in range(len(string)):
        ascii = ord(string[i])
        if (65 <= ascii <= 90) or (97 <= ascii <= 122): #letter only
            result = string[i]
    return result if result != '' else None # if result is NOT empty, return result, else return NONE.

def generate_palindrome(string:str) -> str | None:
    resversed_string = '' # makes reversed_string able to hold a string inside?
    i = len(string) - 1
    while i >= 0:
        reversed_string = reversed_string + string[i]
        i = i - 1 # i is counting down from len(string)
    result = string + reversed_string
    return result if result != '' else None

def is_palindrome(string:str) -> bool:
    # ignore capitalization, punctuation, spaces
    valid = True
    filtered = ''
    for i in range(len(string)): #filtering the string to only recognize letters, and numbers
        ascii = ord(string[i])
        if (65 <= ascii <= 90) or (97 <= ascii <= 122) or (48 <= ascii <= 57):
            filtered = filtered + string[i].lower()
    left = 0
    right = len(filtered) - 1
    while left < right: # by defining these sides as numbers, we are telling the program to only count before the midpoint
        if filtered[left] != filtered[right]:
            valid = False
        left = left + 1
        right = right - 1 #instructing how right and left should count.
    return valid



#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
