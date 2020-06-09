from mp3p.time_util import TimeUtil


def goto_help(cmd):
	"""display the help screen for the goto method."""
	print('The goto command takes a timestamp and jumps to that location in the audio.')
	print('Syntax: goto timestamp')
	print('timestamp: hour:minutes:seconds')
	print('           minutes:seconds')
	print('           seconds \n')
	print('the current location is: ' + str(current_location(cmd)) + 'ms')


def goto(cmd, timestamp):
	"""Specify a timestamp in the audio to jump to."""
	time_array = timestamp.split(':')
	# convert the timestamp to milliseconds
	time = TimeUtil(time_array).time_to_ms()
	if time < cmd.icp.get_length():
		cmd.icp.pause()
		cmd.icp.set_time(time)
		cmd.icp.play()
	else:
		print('*** Warning: The given timestamp exceeds the length of the audio.')


def jump_help(cmd):
	"""display the help screen for the jump method"""
	print('The jump commend takes a interval in seconds and jumps according to the symbol forwards or backwards.')
	print('Syntax: jump +/-interval \n')
	print('The current location is: ' + str(current_location(cmd)) + 'ms')


def jump(cmd, interval):
	"""Jump forward or backward in the audio by the specified time interval."""
	symbols = ['+', '-']
	for i in symbols:
		if interval.startswith(i):
			interval = interval.strip(i)
			print(interval)
			if interval.isdigit():
				cmd.icp.pause()
				time = 'cmd.icp.get_time() ' + i + ' int(interval) * 1000'
				cmd.icp.set_time(eval(time))
				cmd.icp.play()
				return
	print('*** The time interval specified is not a valid number.')


# TODO implement a better location method
def current_location(cmd):
	"""return the current playback location"""
	return cmd.icp.get_time()
