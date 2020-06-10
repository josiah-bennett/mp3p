# mp3p
command line mp3-player

## Description
mp3p is a python program used to play mp3 files.

### Commands
play &nbsp; - &nbsp; plays an audio file given as an argument or starts playback after the pause command (no argument)\
pause &nbsp; - &nbsp; pauses the playback and also continues playback if paused\
stop &nbsp; - &nbsp; stops the playback\
volume &nbsp; - &nbsp; sets the volume based on an argument given as a percentage\
mute &nbsp; - &nbsp; toggles between 0% volume and the last nonzero volume\
goto &nbsp; - &nbsp; jumps to the specified timestamp in the audio file\
jump &nbsp; - &nbsp; jump forward or backward in the audio by the specified amount in seconds\
exit &nbsp; - &nbsp; exit out of the program

## Istallation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mp3p.
```bash
pip install mp3p
```

## Usage
```bash
$ mp3p

(mp3p) play test.mp3
(mp3p) volume 50
(mp3p) pause
(mp3p) play
(mp3p) mute
(mp3p) stop
```
The timestamp can be specified as:\
(hours:minutes:seconds)\
(minutes:seconds)\
(seconds)
```bash
(mp3p) goto 1:25:04
(mp3p) goto 45:23
(mp3p) goto 12

(mp3p) jump +30
(mp3p) jump -15
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
