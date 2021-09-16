# convert usr input string to morse code

# morse code dictionary
morse_code_dict = {'A': '·-', 'J': '·---', 'S': '···', '1': '·----', 'B': '-···', 'K': '-·-', 'T': '-', '2': '··---',
                   'C': '-·-·', 'L': '·-··', 'U': '··-', '3': '···--', 'D': '-··', 'M': '--', 'V': '···-',
                   '4': '····-', 'E': '·', 'N': '-·', 'W': '·--', '5': '·····', 'F': '··-·', 'O': '---', 'X': '-··-',
                   '6': '-····', 'G': '--·', 'P': '·--·', 'Y': '-·--', '7': '--···', 'H': '····', 'Q': '--·-',
                   'Z': '--··', '8': '---··', 'I': '··', 'R': '·-·', '0': '-----', '9': '----·'}

morse_code = ""
# get user input string
user_str = input("Please input the string to convert to Morse Code: ")

#  space will not convert
for letter in user_str:
    if letter == " ":
        code = " "
# convert letter to morse code
    else:
        letter = letter.upper()
        code = morse_code_dict[letter]
# insert space between letters
    morse_code += f" {code}"
print(f"The morse code is: {morse_code}")

