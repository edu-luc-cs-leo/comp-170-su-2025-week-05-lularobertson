
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

"""
    MIDTERM REVIEW:

    Within the first five assignments, I think my coding has gotten a lot better.
    It's still challenging to be able to translate what I'm thinking into
    computer-talk though. One mistake I repeated a few times was lack of comments. I've been trying
    to get better by writing while I go to try to explain to myself
    what is happening so it makes it a lot easier to understand
    later on when I'm writing a relfection on it or something. All my code has executed at least
    a little. I'm sure there are a lot of things I could have done better so they would be
    more optimized, but they all ran without the terminal giving me errors. I have definitely been
    better about trying to optimize things as much as I can and making it look cleaner
    espeically because I get lost within all the words easily.

    I think I have been very good about going to class and doing so on time. There was that one time
    I had to leave early, but I hope my email beforehand made it less bad. I also think that my participation
    and proactiveness has been good, like emailing you when I need help with the tests, and asking
    questions in class when I have them. I have not done any additional problems, but I do think
    reading code from the book links with explaination helps me learn. It's helpful to see code
    that works and then internalizing why it works. I don't know if I have been putting as much
    commitment into the course as 9 extra hours. Probably not that much. Whne moving
    foreward, I will make an active effort to spend more time with this information than I am
    currently, as well as making sure to start the homework earlier since it is currently 17:47
    CT which is 22:47 UTC. Which is my fault for not following the first part of the instructions
    which was reviewing the due date. 
"""

"""
REFLECTION:

1. For both the shortest and longest word tests, our code was very similar except
I did not define longest as None. I know that you set longest to None so the function
would return None if the list of words did not meet the requirements. The code did pass the
test so I think it would work. The only issue maybe would be clarity. The other differences
between those two tests would be that you used "for word in words:" loop which I'm not sure
if I fully understand that bit. I think it means "for each element (that we're calling "word")
of the list words". I used range(1, len(words)) because that felt easier to me in the moment.

2. Same thing as number 1.

3. The same issue in my code where I did not write odd = None before the if statement, but again
passed the test. And the word in words for statement difference.

4. Our code seems to be relatively the same here too. The difference being you setting
averages = None where I just put the whole thing in an if statement. It passed the test so I hope it's
fine. And then I used the absolute value thing to see if the length of some word was woithin 1
letter of the average of all the words.

5. While your code has both f and b counting in both lists, I just counted
in my first list and used "in" instead of "==" when defining found again. I'm not sure
if mine has a problem or not. It passed the test.
"""

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#

 # Testing here is done a bit more formally than using simple print statements.

# This type of testing is called "Unit Testing" and can be extremely useful.

# Unit testing applies to small components of the software we write -- in this

# case the units tested are the individual methods we wrote.

#


import unittest
class TestStringMethods(unittest.TestCase):


    def test_intersection(self):

        self.assertEqual(intersection("airplanes", "repairman"), "airpne")

        self.assertEqual(intersection("abc", "def"), "")

        self.assertEqual(intersection("hello", "hello"), "hello")

        self.assertEqual(intersection("aaaa", "aaa"), "a")

        self.assertEqual(intersection("", "abc"), None)

        self.assertEqual(intersection("abc", ""), None)

        self.assertEqual(intersection("", ""), None)

        self.assertEqual(intersection("abc", "cab"), "abc") # preserves order of `foo`


    def test_is_alphabetical(self):

        self.assertTrue(is_alphabetical("abcXYZ"))

        self.assertFalse(is_alphabetical("abc1"))

        self.assertFalse(is_alphabetical("hello!"))

        self.assertFalse(is_alphabetical(" "))

        self.assertFalse(is_alphabetical(""))

        self.assertFalse(is_alphabetical(None))

        self.assertTrue(is_alphabetical("ZzAaBb"))


    def test_letters_only(self):

        self.assertEqual(letters_only("abc123XYZ!@#"), "abcXYZ")

        self.assertEqual(letters_only("!@#$%^&*()"), "")

        self.assertEqual(letters_only(""), None)

        self.assertEqual(letters_only(None), None)

        self.assertEqual(letters_only("LettersONLY"), "LettersONLY")


    def test_generate_palindrome(self):

        self.assertEqual(generate_palindrome("mice"), "miceecim")

        self.assertEqual(generate_palindrome("mad"), "madam")

        self.assertEqual(generate_palindrome("a"), "a")

        self.assertEqual(generate_palindrome(""), None)

        self.assertEqual(generate_palindrome(None), None)


    def test_is_palindrome(self):

        self.assertTrue(is_palindrome("Racecar"))

        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))

        self.assertTrue(is_palindrome("No 'x' in Nixon"))

        self.assertFalse(is_palindrome("Hello"))

        self.assertFalse(is_palindrome("Palindrome"))

        self.assertFalse(is_palindrome(""))

        self.assertFalse(is_palindrome(None))




    # This allows the test to be run from the command line using `python -m unittest filename.py`

        if __name__ == '__main__':

            unittest.main()



