import string
import random

# Define the code system
CODE = {
    'a': 'q',
    'b': 'w',
    'c': 'e',
    'd': 'r',
    'e': 't',
    'f': 'y',
    'g': 'u',
    'h': 'i',
    'i': 'o',
    'j': 'p',
    'k': 'a',
    'l': 's',
    'm': 'd',
    'n': 'f',
    'o': 'g',
    'p': 'h',
    'q': 'j',
    'r': 'k',
    's': 'l',
    't': 'z',
    'u': 'x',
    'v': 'c',
    'w': 'v',
    'x': 'b',
    'y': 'n',
    'z': 'm'
}

# Generate a random question
questions = [
    'What is the capital of France?',
    'Who invented the telephone?',
    'What is the highest mountain in the world?',
    'What is the largest country by area?',
    'Who wrote the novel "Pride and Prejudice"?'
]
question = random.choice(questions)

# Ask the user the random question
answer = input(question + '\n').lower()

# Check if the answer is correct
if answer == 'paris':
    print('Correct!')
    messages = []  # list to store encoded/decoded messages
    action = input('Do you want to encode (e), decode (d), or quit (q)? ').lower()
    while action != 'q':
        if action == 'e':
            plaintext = input('Enter the message you want to encode: ').lower()
            ciphertext = ''.join([CODE.get(c, c) for c in plaintext])
            messages.append(('encode', plaintext, ciphertext))  # add message to list
            print('Encoded message:', ciphertext)
        elif action == 'd':
            ciphertext = input('Enter the message you want to decode: ').lower()
            plaintext = ''.join([next((k for k, v in CODE.items() if v == c), c) for c in ciphertext])
            messages.append(('decode', ciphertext, plaintext))  # add message to list
            print('Decoded message:', plaintext)
        else:
            print('Invalid action!')
        action = input('Do you want to encode (e), decode (d), or quit (q)? ').lower()
    
    save_or_delete = input('Do you want to save (s) or delete (d) the encoded/decoded messages history? ').lower()
    if save_or_delete == 's':
        with open('history.txt', 'w') as f:
            for message in messages:
                f.write(message[0] + ': ' + message[1] + ' -> ' + message[2] + '\n')  # write each message to file
        print('History saved!')
    elif save_or_delete == 'd':
        import os
        os.remove('history.txt')
        print('History deleted!')
    else:
        print('Invalid option!')
else:
    print('Incorrect answer!')
