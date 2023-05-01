import time
import random
from datetime import date, timedelta
import datetime

spinner = ['-', '\\', '|', '/']
subjects=["Science", "English", "Hindi", "Maths", "History", "Civics","Geography", "French"]
today=datetime.date.today()
yesterday = date.today() - timedelta(days=1)

def wait(howLong):
    time.sleep(howLong)

# Open file to write data
filename = "work_done.txt"
file = open(filename, "a")

for i in range(20): # number of spins
    print("\rSpinning " + spinner[i%4], end="")
    wait(0.2)

print("\n\nYour first subject is. . . . . . . . . . .")
wait(1)
sub1=random.choice(subjects)
print(sub1 + "!!")

# Get work done for subject 1
done1 = input("After you are done with " + sub1 + ", write here what you have done + the amount of pages you did: ")
# Write work done for subject 1 to file
file.write(str(today) + " - " + sub1 + ": " + done1 + "\n")

print("Your second subject is. . . . . . . . . . .")
wait(1)
sub2=random.choice(subjects)
print(sub2 + "!!")

# Get work done for subject 2
done2 = input("After you are done with " + sub2 + ", write here what you have done + the amount of pages you did: ")
# Write work done for subject 2 to file
file.write(str(today) + " --> " + sub2 + ": " + done2 + "\n")
if today!=yesterday:
    file.write("______________________________________________")

# Close file
file.close()
