# from https://vegibit.com/how-to-use-python-regular-expressions-for-pattern-matching/
import re
import sys

# a) Plural and non-plural
text = "gray eyes"
pattern = r"[a-zA-Z]+s*"
match = re.search(pattern, text)

if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")

# b) a's following !'s
text = "eyes!a"
pattern = r"[a-zA-Z]+!a+"
match = re.search(pattern, text)

if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")    

# c) no stop's (wont match if there are stop words)
pattern = r"([tT]he) ([aA]t)"
text = "Kenneth stopped looking at the sun" #should fail to match
match = re.search(pattern, text)
if match:
    print("Pattern found stop word," , match.groups())
else:
    print(text)  

# 2.1)
    # reads input text(string) and outputs text(string)
def ELIZA(text):
   
    pattern1 = r".*\bI'm (depressed|sad).*"
    x1 = re.sub(pattern1, r'I AM SORRY TO HEAR YOU ARE DEPRESSED OR SAD', text)
    match1 = re.search(pattern1, text)

    pattern2 = r".*\bI am (depressed|sad).*"
    x2 = re.sub(pattern2, r"WHY DO YOU THINK YOU ARE DEPRESSED OR SAD", text)
    match2 = re.search(pattern2, text)

    pattern3 = r".*all.*"
    x3 = re.sub(pattern3, r"IN WHAT WAY?", text)
    match3 = re.search(pattern3, text)
    
    pattern4 = r".*always.*"
    x4 = re.sub(pattern4, r"CAN YOU THINK OF A SPECIFIC EXAMPLE?", text)
    match4 = re.search(pattern4, text)

    if match1:
        print("ELIZA: " + x1.rstrip("\n"))
    elif match2:
        print("ELIZA: " + x2.rstrip("\n"))
    elif match3:
        print("ELIZA: " + x3.rstrip("\n"))
    elif match4:
        print("ELIZA: " + x4.rstrip("\n"))
    else:
        print("ELIZA: I dont understand...?")

# 2)
user = input("USER: ")
while (user != 'exit'):
    ELIZA(user)
    user = input()
        



