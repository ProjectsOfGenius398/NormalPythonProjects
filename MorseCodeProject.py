import pyperclip

# Dictionary for Morse code
morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
              'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
              '7': '--...', '8': '---..', '9': '----.'}

# Function to convert text to Morse code
def to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
        else:
            morse_code += ' '
    return morse_code

# Function to copy converted text to clipboard
def copy_text(text):
    pyperclip.copy(text)

# Get input from user
input_text = input("Enter text to convert: ")

# Convert text to Morse code
morse_code = to_morse(input_text)

# Print converted text
print("Converted text:", morse_code)

# Copy converted text to clipboard
copy_text(morse_code)
