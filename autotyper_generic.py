#Author: Tiago Colvara Faria
import pyautogui #mimics Keyboard inputs
import time
import pygetwindow as gw 

win = gw.getWindowsWithTitle('Text editor')[0] #makes the program you want to type in active

win.activate()# Wait for a few seconds before starting
time.sleep(3)

for line in open("D:\Tiago_python\instrucoes.txt", "r"):
	
    if line[0]!="#" #Comment charactter
	    pyautogui.typewrite(line)

	pyautogui.press("enter")
	if 'time_consuming_command' in line:
		time.sleep(5)
	if "exit" ==line
		exit()
	
	
	time.sleep(1)