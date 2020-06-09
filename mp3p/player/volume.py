def volume_help(cmd):
	"""display the help screen for the volume method."""
	print('The volume command takes a volume percentage and sets the program volume.')
	print('Syntax: volume percentage \n')
	print('The current volume is set to: ' + current_volume(cmd) + '%')


def current_volume(cmd):
	"""get and return the current program volume."""
	return str(cmd.icp.audio_get_volume())


def volume(cmd, percentage):
	"""changes the volume based on user input"""
	try:
		# Test if the input is an integer
		if percentage.isdigit():
			percentage = int(percentage)
			# all of the numbers between 0 and 100
			acceptable_range = range(101)
			# check if the input is a valid percentage
			if percentage in acceptable_range:
				if not percentage == 0:
					# cmd.vol is used as a storage var when the playback is muted
					# to roll back to the old volume when un muted
					# so it is only set when the volume isn't set to 0
					cmd.vol = percentage
				cmd.icp.audio_set_volume(percentage)
			else:
				raise ValueError('*** Value Error: percentage values have to be between 0 and 100')
		else:
			raise TypeError('*** Type Error: The given argument (' + percentage + ') is not an integer.')
	except ValueError as ex:
		print(ex)
	except TypeError as ex:
		print(ex)


def mute_help(cmd):
	"""display the help screen for the mute method."""
	print('This command (un)mutes the audio file currently playing.')
	print('Syntax: mute \n')
	string = 'The audio file is currently '
	# Ternary operators
	print(string + 'not muted') if not is_muted(cmd) else print(string + 'muted')


def is_muted(cmd):
	"""check if the playback is currently muted"""
	return cmd.icp.audio_get_volume() == 0


def mute(cmd):
	"""mute if the current volume is not zero un mute otherwise"""
	if cmd.icp.audio_get_volume() == cmd.vol:
		cmd.icp.audio_set_volume(0)
	else:
		cmd.icp.audio_set_volume(cmd.vol)
