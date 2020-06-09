# mp3p
command line mp3-player

## Description
mp3p is a python program used to play mp3 files.

### Commands
play &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : plays an audio file given as an argument or starts playback after the pause command (no argument)\
pause &nbsp;&nbsp; : pauses the playback and also continues playback if paused\
stop &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : stops the playback\
volume &nbsp;: sets the volume based on an argument given as a percentage\
mute &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: toggles between 0% volume and the last nonzero volume\
goto &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : jumps to the specified timestamp in the audio file\
jump &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: jump forward or backward in the audio by the specified amount in seconds\
exit &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: exit out of the program\

## Istallation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mp3p.
```bash
pip install mp3p
```

## Usage
```bash


play test.mp3
volume 50
pause
play
mute
stop
```
The timestamp can be specified as:\
(hours:minutes:seconds)\
(minutes:seconds)\
(seconds)
```bash
goto 1:25:04
goto 45:23
goto 12

jump +30
jump -15
```

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
