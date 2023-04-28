import pandas as pd

contactInfo=['']
name=input("What is the name of your friend")
contactInfo.append(name)
age=input("What's their age?")
contactInfo.append(age)
phone=input("What's their phone number?")
contactInfo.append(phone)
address=input("What's their address")
contactInfo.append(address)
length=input("How long have ya'll been friends?")
contactInfo.append(length)

contants = {'Name':contactInfo[0],
			'Age':contactInfo[1],
			'Contact No.':contactInfo[2],
			'Address':contactInfo[3],
			'Friendship Length':contactInfo[4],
			}

print(contants)