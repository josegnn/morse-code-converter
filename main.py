# TODO 01: IMPORT STATEMENTS
import requests

# TODO 02: GET THE MORSE CODE DICTIONARY
URL_MORSE_CODE = "https://gist.githubusercontent.com/mohayonao/094c71af14fe4791c5dd/raw/" \
                 "8399262545d0d88507ce42069b0b50043f0eddbc/morse-code.json"
morse_dictionary = requests.get(URL_MORSE_CODE).json()


# TODO 03: CREATE A FUNCTION TO TRANSLATE TEXT TO MORSE CODE
def translate_text_or_code(text, to_morse):
    result = ""
    text = text.lower()

# If the user looks for translating from Plain Text to Morse Code, the code bellow will be executed:
    if to_morse:
        for character in text:
            if character == " ":
                result = result.strip(" ")
                result += "/"
            elif character == "\n":
                result = result.strip(' ')
                result += '\n'
            else:
                result += morse_dictionary[character]
                result += " "

# But, if instead the user needs to translate from Morse Code to Plain Text, the code bellow will be executed:
    else:
        words = text.split('/')
        for word in words:
            letters = word.strip(" ").split(" ")
            for letter in letters:
                if "\n" in letter:
                    letter = letter.split("\n")
                    for i, letter_1 in enumerate(letter):
                        key = [key for key in morse_dictionary if morse_dictionary[key] == letter_1]
                        try:
                            if i == 0:
                                result += key[0] + '\n'
                            else:
                                result += key[0]
                        except KeyError:
                            result += '\n'
                else:
                    key = [key for key in morse_dictionary if morse_dictionary[key] == letter]
                    result += key[0]
            result += " "
    return result


# TODO 04: SELECT THE TRANSLATION DIRECTION
direction = input('Type\n(1) for translating from text to morse code or \n'
                  '(2) for translating from morse code to text:\n')

if direction == "1":
    direction = True
else:
    direction = False

# TODO 05: ASK FOR USER INPUT (TEXT TO BE TRANSLATED)
to_be_translated = input('Welcome to the Morse Code Converter!\nPlease, insert the text/code that you would'
                         ' like to convert.'
                         '\nIf you prefer, you can type TXT for providing an .txt file.\n')

# If the user prefer to use a .txt file instead of typing the text, he/she can give the file name here. If the file is
# not in the same directory of the main.py file, the full path must be given (or, at lead, the relative path.

if to_be_translated.lower() == "txt":
    to_be_opened = input('Please, insert the name of the file to be opened.\n(Do not include .txt)\n')
    with open(f'{to_be_opened}.txt', 'r') as text_to_be_translated:
        to_be_translated = text_to_be_translated.read()

# TODO 06: TRANSLATE
# Here, we simply trigger the function.
result = translate_text_or_code(to_be_translated, direction)

# TODO 07: RETURN THE RESULT AND ASK IF USER WANTS TO SAVE AS .TXT
# In this step, the final result is displayed to the user. It's also asked if the user wants to save it as .txt.
save = input('Here your translated text is:\n'
             f'{result}\n'
             'Would you like of saving it as a txt?\n'
             '(Y) for yes and (N) for no.')

# TODO 08: IF SO, SAVE AS .TXT
# Now, the file is being saved as the user asked.
if save.lower() == "y":
    name = input('Type the name of the file:\n(Do not include .txt)\n')

    with open(f'{name}.txt', "w") as result_file:
        result_file.write(result)

else:
    pass

# TODO 09: TELL THE USER THE PROGRAM IS FINISHED
print('Program Successfully Complete! Restart to translate another text!')
