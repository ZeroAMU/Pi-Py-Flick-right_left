import keyboard
import signal
import flicklib
import time

while True :
	@flicklib.flick()
	def flick(start,finish):
		if (start == 'south' and finish == 'north'):
			time.sleep(1)
			keyboard.press_and_release('up')
		elif (start == 'north' and finish == 'south'):
			time.sleep(1)
			keyboard.press_and_release('down')
		elif (start == 'east' and finish == 'west'):
			time.sleep(1)
			keyboard.press_and_release('left')
		elif (start == 'west' and finish == 'east'):
			time.sleep(1)
			keyboard.press_and_release('right')
