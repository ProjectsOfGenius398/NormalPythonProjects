import tkinter as tk
import tkinter.messagebox
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
def copy_text():
    pyperclip.copy(output.cget('text'))

# Create window
window = tk.Tk()
window.title("Morse Code Converter")
window.configure(bg='#a1dbcd')
window.geometry("400x400")

# Create input label
input_label = tk.Label(window, text="Enter text to convert:", bg='#a1dbcd')
input_label.pack(pady=10)

# Create input box
input_text = tk.Entry(window, width=30, bd=3)
input_text.pack(pady=10)

# Create convert button
convert_button = tk.Button(window, text="Convert", command=lambda: output.config(text=to_morse(input_text.get())))
convert_button.pack(pady=10)

# Create output label
output_label = tk.Label(window, text="Converted text:", bg='#a1dbcd')
output_label.pack(pady=10)

# Create output box
output = tk.Label(window, text="", width=30, height=2, relief="solid")
output.pack(pady=10)

# Create copy button
copy_button = tk.Button(window, text="Copy", command=copy_text)
copy_button.pack(pady=10)

# Run the main loop
window.mainloop()
