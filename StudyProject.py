import time
import random
import datetime

current_date = datetime.date.today()
spinner = ['-', '\\', '|', '/']
subjects=["Science", "English", "Hindi", "Maths", "History", "Civics","Geography", "French"]
examSubjects=["Hindi", "English", "Science", "Maths", "French"]
now = datetime.datetime.now()
other_time = datetime.time(8, 0, 0)



exam_dates = [
    datetime.date(2023, 3, 1),
    datetime.date(2023, 3, 3),
    datetime.date(2023, 3, 6),
    datetime.date(2023, 3, 10),
    datetime.date(2023, 3, 13),
]
today_date = datetime.date.today()

days_left = (exam_dates[0] - today_date).days




def wait(howLong):
    time.sleep(howLong)
for i in range(20): # number of spins
    print("\rSpinning " + spinner[i%4], end="")
    wait(0.2)

print("\n\nYour first subject is. . . . . . . . . . .")
wait(1)
print(random.choice(subjects) + "!!")


print("Your second subject is. . . . . . . . . . .")
wait(1)
print(random.choice(subjects) + "!!")

if days_left < 4:
    print("However, I would suggest preparing for your "+examSubjects[0]+" exam, its less than ", days_left, " days away.")
if days_left = 56:
    print("Forget everything, your "+examSubjects[0]+" exam is tomorrow. C'mon, you got this!")
    exam_dates.pop(0)
    examSubjects.pop(0)
elif today_date == exam_dates[0] and now.time > other_time:
    print("Your "+examSubjects[0]+" exam is today. Good luck!")
    exam_dates.pop(0)
    examSubjects.pop(0)
elif now.time < other_time or today_date != exam_dates[0]:
    print("Your "+examSubjects[0]+" exam is over! Awesome!")
    exam_dates.pop(0)
    examSubjects.pop(0)
else:
    print("And don't worry. You still have ",days_left," days to prepare for your "+examSubjects[0]+" exam.")
