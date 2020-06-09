from mp3p.command_player import ICP


def main():
	prompt = ICP()
	prompt.prompt = '(mp3p) '
	prompt.cmdloop('Starting Mp3 Player...')


if __name__ == '__main__':
	main()
