from __future__ import annotations
from typing import Tuple
from array import array
import base64
import math
import pprint
import re
import struct
import sys
import os
import tkinter as tk
import wave
a4 = 440
step = 2**(1/12)
default_rate = 2048
default_pace = 120

icon = b'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'

notes = {
	'-': 0,
	'c4': int(a4*step**-9),
	'#c4': int(a4*step**-8),
	'd4': int(a4*step**-7),
	'#d4': int(a4*step**-6),
	'e4': int(a4*step**-5),
	'f4': int(a4*step**-4),
	'#f4': int(a4*step**-3),
	'g4': int(a4*step**-2),
	'#g4': int(a4*step**-1),
	'a4': int(a4*step**0),
	'#a4': int(a4*step**1),
	'b4': int(a4*step**2)
}

def recalc_notes():
	global notes
	notes = {
		'-': 0,
		'c4': int(a4*step**-9),
		'#c4': int(a4*step**-8),
		'd4': int(a4*step**-7),
		'#d4': int(a4*step**-6),
		'e4': int(a4*step**-5),
		'f4': int(a4*step**-4),
		'#f4': int(a4*step**-3),
		'g4': int(a4*step**-2),
		'#g4': int(a4*step**-1),
		'a4': int(a4*step**0),
		'#a4': int(a4*step**1),
		'b4': int(a4*step**2)
	}

def get_freq(note: str) -> int:
	tone: str
	octave: int
	base: int
	if note[0] == '#':
		tone = note[1]
		octave = int(note[2])
		base = notes[''.join(['#',tone,'4'])]
	elif note[0] == '-':
		octave = 4
		base = 0
	else:
		tone = note[0]
		octave = int(note[1])
		base = notes[''.join(['',tone,'4'])]
	distance = 12*(octave-4)
	return(int(base*step**distance))

def parse_sound(note: Tuple[str,str,str,str,str,str,str,str,str,str]) -> Tuple[float,int]:
	time = 4/float(note[5])
	broken = note[6]
	sound = note[7]
	octave = note[8]
	extended = note[9]
	if extended:
		time *= 1.5
	return (time, get_freq(broken+sound+octave))

def parse_silence(note: Tuple[str,str,str,str,str,str,str,str,str,str]) -> Tuple[float,int]:
	time = 4/float(note[1])
	extended = note[3]
	if extended:
		time *= 1.5
	return (time, get_freq('-'))

def parse_note(note: Tuple[str,str,str,str,str,str,str,str,str,str]) -> Tuple[float,int]:
	result: Tuple[float,int]
	if note[7]:
		result = parse_sound(note)
	elif note[2]:
		result = parse_silence(note)
	else:
		raise Exception("Wait, what?")
	return result

# r"((\d+)(-)(\.?))|((\d+)([#]?)([a-g])(\d+)(\.?))" to match notes.
# There are two alternatives: sounds and silences
# SILENCES (1st alternative)
## \d+ matches digits, which correspond to the duration of the silence.
## - is literally the indicator of a silence.
## There may be an optional dot to tell that the note is 1.5x times of its own duration.
# SOUNDS (2nd alternative)
## \d+ matches digits like the silence one. It is duration of the sound.
## A # is optional. It indicates that the note is half a sound higher pitched than its normal one.
## The notes are "a b c d e f g", corresponding to "la sol si do re mi fa sol" This part is telling that we are reading a sound
## Some digits are mandotary to know the octave of the sound; thus, \d+
## An optional dot has the same meaning like its silence counterpart

# r"\[([\s\S]*?)\]|(\S+(?:\[[^\]]*\])?)" to differ repeated parts and unrepeated ones.
## We escaped brackets with backslash, since they have meanings for regex.
## We have one matching group. This starts with a character class.
## The class is \s and \S, which mean "non-whitespace character" and "whitespace ones", respectively.
## We match this characters until we see a closing bracket.
## The other alternative is all the other that are not in brackets.
## With this regex, we can distinguish between repeated notes and non-repeated notes.
## 1st group has repeated ones, 2nd one has non-repeateds.

def main(filename: str, pace: int, sample_rate: int):
	out = os.path.splitext(filename)[0] + '.wav'
	if len(sys.argv) == 4:
		sample_rate = int(sys.argv[3])
	content: str
	with open(filename,'r') as file:
		content = file.read()
	to_repeat = re.findall(r"\[([\s\S]*?)\]|([\S\s]+?(?![^[]]))", content)
	new_content: str = ""
	for block in to_repeat:
		if block[0]:
			new_content += (block[0] + '\n') * 2
		elif block[1]:
			new_content += block[1]
	note_list = re.findall(r"((\d+)(-)(\.?))|((\d+)([#]?)([a-g])(\d+)(\.?))", new_content)
	parsed = [parse_note(note) for note in note_list]
	data = bytearray()
	sound_file: wave.Wave_write = wave.open(out, 'wb')
	sound_file.setnchannels(1)
	sound_file.setsampwidth(2)
	sound_file.setframerate(sample_rate)
	for (duration,pitch) in parsed:
		duration *= 60/pace
		for i in range(0,int(sample_rate*duration)):
			w = int(32765*math.sin(2*math.pi*pitch*i/sample_rate))
			arr = struct.pack('<h',w)
			data.append(arr[0])
			data.append(arr[1])
	sound_file.writeframesraw(data)
	sound_file.close()

def create(event: tk.Event):
	global default_pace, default_rate
	wind: WindowApp = event.widget.master.master
	pace_str: str = wind.paceBox.get()
	if pace_str == "":
		pace = default_pace
	else:
		pace = int(pace_str)
	
	rate_str: str = wind.rateBox.get()
	if rate_str == "":
		rate = default_rate
	else:
		rate = int(rate_str)
	
	a4freq_str: str = wind.freqBox.get()
	if a4freq_str == "":
		a4freq = 440
	else:
		a4freq = int(a4freq_str)

	global a4
	a4 = a4freq
	recalc_notes()

	filename: str = wind.filenameBox.get()
	if filename == "":
		wind.msg.config(fg='red')
		wind.mesg.set("You must enter a file name!")
		return

	try:
		main(filename, pace, rate)
	except Exception as e:
		wind.msg.config(fg='red')
		wind.mesg.set(f"An error occured:\n{str(e)}")
	out = os.path.splitext(filename)[0] + '.wav'
	f = open(out, 'rb')
	size = len(f.read())
	f.close()
	wind.msg.config(fg='green')
	wind.mesg.set(f"Wrote {size/1024**2: .2f} MB")

class WindowApp(tk.Tk):
	def __init__(self):
		super().__init__()
		default_file: str = ''
		if len(sys.argv) >= 2:
			default_file = sys.argv[1]
		self.filename = tk.Frame(width=150, height=100)
		self.filenameSelector = tk.Label(self.filename, text="File Name:")
		self.filenameBox = tk.Entry(self.filename)
		self.filenameBox.insert(tk.INSERT, default_file)

		self.options = tk.Frame(width=150, height=100)
		
		self.pace = tk.Frame(self.options, width=50, height=100)
		self.paceLabel = tk.Label(self.pace, text="Pace:")
		self.paceBox = tk.Entry(self.pace)

		self.rate = tk.Frame(self.options, width=50, height=100)
		self.rateLabel = tk.Label(self.rate, text="Bitrate:")
		self.rateBox = tk.Entry(self.rate)

		self.freq = tk.Frame(self.options, width=50, height=50)
		self.freqLabel = tk.Label(self.freq, text="Frequency of A4:")
		self.freqBox = tk.Entry(self.freq)

		self.creation = tk.Frame(width=150, height=100)
		self.startbtn = tk.Button(self.creation, text="Start Conversion")
		self.startbtn.bind('<Button-1>', create)
		self.mesg = tk.StringVar(self.creation, "")
		self.msg = tk.Label(self.creation, textvariable=self.mesg)

		self.place()
	def place(self):
		self.filename.pack()
		self.filenameSelector.pack()
		self.filenameBox.pack()

		self.options.pack()

		self.pace.pack(side='left')
		self.paceLabel.pack()
		self.paceBox.pack()

		self.rate.pack(side='left')
		self.rateLabel.pack()
		self.rateBox.pack()

		self.freq.pack(side='right')
		self.freqLabel.pack()
		self.freqBox.pack()
		
		self.creation.pack()
		self.startbtn.pack()
		self.msg.pack()

if __name__ == "__main__":
	app = WindowApp()
	app.title("Composer")
	app.geometry("350x150")
	app.resizable(False,False)
	ico = base64.b64decode(icon)
	img = tk.PhotoImage(data=ico)
	app.tk.call('wm', 'iconphoto', app._w, img) # type: ignore
	app.mainloop()
