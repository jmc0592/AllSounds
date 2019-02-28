This is an experiment to see how many distinct sounds can be generated that the average human can hear.

# Dependencies:
* numpy
* pyaudio
  * Linux - portaudio19-dev, pythonX-dev

# Configuration:
If it sounds like short pops (not static-like), see https://bbs.archlinux.org/viewtopic.php?id=185736.
In /etc/pulse/daemon.conf, change add/change "default-fragments = 5" and "default-fragment-size-msec = 2".

# Running:
* python main.py
* If using pipenv:
  * pipenv shell
  * python main.py

# References:
* https://wonders.physics.wisc.edu/what-is-sound/
* http://people.csail.mit.edu/hubert/pyaudio/
* https://bbs.archlinux.org/viewtopic.php?id=185736