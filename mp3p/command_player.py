from cmd import Cmd
import mp3p.controls as ctrl
import mp3p.volume as vol
import mp3p.time_manipulation as tm
import vlc


class ICP(Cmd):

	def __init__(self):
		super().__init__()
		self.vol = 50
		self.icp = vlc.MediaPlayer()
		self.icp.audio_set_volume(self.vol)

	@staticmethod
	def do_exit(args):
		"""Exit out of the program"""
		print('Quitting...')
		raise SystemExit

	def help_play(self):
		ctrl.play_help(self)

	def do_play(self, args):
		ctrl.play(self, args)

	def help_pause(self):
		ctrl.pause_help(self)

	def do_pause(self, args):
		ctrl.pause(self)

	def help_stop(self):
		ctrl.stop_help(self)

	def do_stop(self, args):
		self.icp.stop()

	def help_volume(self):
		vol.volume_help(self)

	def do_volume(self, args):
		vol.volume(self, args)

	def help_mute(self):
		vol.mute_help(self)

	def do_mute(self, args):
		vol.mute(self)

	def help_goto(self):
		tm.goto_help(self)

	def do_goto(self, args):
		tm.goto(self, args)

	def help_jump(self):
		tm.jump_help(self)

	def do_jump(self, args):
		tm.jump(self, args)
