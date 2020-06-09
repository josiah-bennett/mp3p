import vlc


def play_help(cmd):
	"""display the help screen for the play method"""
	print('The play command starts playing audio files if there is file given.')
	print('or it continues the playback of a currently paused audio.')
	print('Syntax: play (file) \n')
	s1 = 'There is '
	s2 = 'audio file currently playing.'
	print(s1 + 'a' + s2) if is_playing(cmd) else print(s1 + 'no' + s2)


def play(cmd, args):
	"""play the given audio file"""
	argument_array = args.split('|')
	file = argument_array[0]
	if len(file) == 0:
		# if no file is given check if there is a file loaded and continue playback
		if not cmd.icp.get_media() is None:
			cmd.icp.play()
		else:
			print('Input Error: There is no file loaded.')
	else:
		try:
			# check if the file exists
			f = open(file)
			f.close()
		except FileNotFoundError:
			print('file not found: Make sure the path and filename are correct.')
		else:
			# load the file and play
			audio = vlc.Instance().media_new(file)
			cmd.icp.set_media(audio)
			cmd.icp.play()


def pause_help(cmd):
	"""displays the help screen for the pause method"""
	print('the pause command pauses and continues the playback of audio files.')
	print('Syntax: pause \n')
	# TODO make a is_paused method


def pause(cmd):
	"""pauses and continues the playback of a audio file"""
	cmd.icp.pause()


def stop_help(cmd):
	"""display the help screen for the stop method"""
	print('The stop command stops the playback of the current audio file.')
	print('Syntax: stop \n')
	s1 = 'There is '
	s2 = 'audio file currently playing.'
	print(s1 + 'a' + s2) if is_playing(cmd) else print(s1 + 'no' + s2)


def stop(cmd):
	"""stops the playback of the audio file."""
	cmd.icp.stop()


def is_playing(cmd):
	"""check if a audio file is playing/paused or stopped."""
	if cmd.icp.is_playing() == 1:
		return True
	else:
		return False
