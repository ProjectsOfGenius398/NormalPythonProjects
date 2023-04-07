# initialize the variables
name = input("Enter student name: ")
subjects = ["Hindi", "English", "French", "Science", "Social Science", "Information Technology", "Mathematics"]
marks = []

# loop to get the marks of each subject for all 4 tests
for i in range(len(subjects)):
    marks.append([])
    print("Enter marks for", subjects[i])
    for j in range(4):
        if j == 0 or j == 2:
            max_marks = 40
        else:
            max_marks = 80
        while True:
            try:
                mark = float(input("Test {}: ".format(j+1)))
                if mark < 0 or mark > max_marks:
                    raise ValueError
                marks[i].append(mark)
                break
            except ValueError:
                print("Invalid input. Please enter a mark between 0 and", max_marks)

# calculate the percentage for each subject and the overall percentage
subject_percents = []
total_marks = 0
total_max_marks = 0
for i in range(len(subjects)):
    subject_marks = sum(marks[i])
    subject_max_marks = len(marks[i]) * 80 if i == 1 else len(marks[i]) * 40
    subject_percent = round(subject_marks / subject_max_marks * 100, 2)
    subject_percents.append(subject_percent)
    total_marks += subject_marks
    total_max_marks += subject_max_marks
overall_percent = round(total_marks / total_max_marks * 100, 2)

# display the results for each subject and the overall percentage
print("\n{}'s marks:".format(name))
for i in range(len(subjects)):
    print("{}: {}%".format(subjects[i], subject_percents[i]))
print("Overall percentage: {}%".format(overall_percent))

# save the results to a txt file
with open("marks.txt", "a") as f:
    f.write("{}'s marks:\n".format(name))
    for i in range(len(subjects)):
        f.write("{}: {}%\n".format(subjects[i], subject_percents[i]))
    f.write("Overall percentage: {}%\n".format(overall_percent))
