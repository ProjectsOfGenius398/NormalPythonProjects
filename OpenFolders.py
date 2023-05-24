import subprocess

folder_path = r'C:\Users\anant\Desktop\Random Stuff\Pictures\Water'

code=int(input("Enter the code. You know what I'm saying right? "))
if code == 1201:
	sure=input("Are you really, really sure that you want to open this folder? y/n ")
	sure=sure.lower()
	if sure=="y":
		sure1=input("Are you fully sure? 100% dedication? y/n ")
		sure1=sure1.lower()
		if sure1=="y":
			sure2=input("Final warning. There is no going back after this. y/n ")
			sure2=sure2.lower()
			if sure2=="y":
				print("Good luck then. I'm opening it")
				subprocess.Popen(f'explorer "{folder_path}"')
