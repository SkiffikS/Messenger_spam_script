import pyautogui as pg
from time import sleep
#from win10toast import ToastNotifier


#toast = ToastNotifier()

def say_position(time):

	time = int(time)
	sleep(time)
	global position
	position = pg.position()
	return "Координати чату: Х = " + str(position[0]) + " Y = " + str(position[1])

def spam(position, col, message, time):

	a = col
	#toast.show_toast("Початок спаму", "спам почнеться через",time," секунд, приготуйтесь", duration=20,icon_path = "spam.ico")
	sleep(time)

	while a > 0:

		pg.click(position)
		pg.typewrite(message)
		pg.press("enter")
		a -= 1

	#toast.show_toast("Кінець спаму", "спим закінчився", duration = 20, icon_path = "spam.ico")

if __name__ == "__main__":

	#pos = say_position(8)
	#print(pos)
	Telegram = (885, 2021)
	Instagram = (1899, 1933)

	spam(Telegram, 10, "test spam script", 10)