import re


def welcome_msg():
        print("""
        ************************
        welcome to the madlib game
        This game will ask the user to input some words through the command line interactions, then it will generate 
        a text that contain these words.
        ************************
        """)

def read_templet(file):
    """
     function for reading a file.
    """
    try:
     with open(file, 'r') as file:
         content = file.read()
     return content
    except FileNotFoundError:
        return [False, 'File was not found!']

def parse_templet(content):
    """
     function that takes in a template string and returns a string with language parts
    removed and a separate list of those language parts.
    """
    parts = []
    string = re.findall(r'\{.*?\}', content)  # find list of all words between {}
    text = re.sub("{[^}]*}", " {}", content)  # removes the words in {}
    for i in string:
        parts.append(i.strip("{ }"))
    return parts, text

def merge(text,word):
    """function that takes in a “bare” template and a list of user entered language parts,
     and returns a string with the language parts inserted into the template."""
    str = text.format(*word)
    return str

def copyFile(text):
    """ new text file """
    file = open('../assests/output.txt','w')
    file.write(text)


if __name__ == "__main__":
    welcome_msg()
    content = read_templet("../assests/input.txt")
    parts = parse_templet(content)
    word = []
    for i in parts[0]:
        input = input("Enter a  " + i + ":")
        word.append(input)
    copy = merge(parts[1], word)
    copyFile(copy)




