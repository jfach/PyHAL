import pyaudio
import wave
import sys
import speech_recognition as sr
import os
from subprocess import Popen, PIPE

r = sr.Recognizer()

def play(filename):
	#define stream chunk
	chunk = 1024

	#open a wav format music
	f = wave.open(filename,"rb")
	#instantiate PyAudio
	p = pyaudio.PyAudio()
	#open stream
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
	#read data
	data = f.readframes(chunk)

	#paly stream
	while data != '':
    		stream.write(data)
    		data = f.readframes(chunk)

	#stop stream
	stream.stop_stream()
	stream.close()

	#close PyAudio
	p.terminate()

def runme(scpt, args=[]):
     p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
     stdout, stderr = p.communicate(scpt)
     return stdout


#def listen(): # will this work???
	#with sr.Microphone() as source:
	#	answer = r.listen(source)

print "<=====> PyHAL-9000 v0.2 <======>"
play("audio/moment.wav")
print "Mini Changelog:\n"
print "- 0.1: Added Google Speech Recognition"
print "- 0.1.1: Added Apple Scripts For HAL 2001 Voice"
print "- 0.1.2: Added PyAudio Support For Authentic HAL Playback"
print "- 0.1.2.1: Added Really Bad Handling For LookupError"
print "- 0.2: Implemented Better Handling For LookupError\n"
raw_input('Press <ENTER> to continue')


user_log = []

print "HAL-9000: Hello, Dave."
runme("""say "Hello Dave." using "Alex" speaking rate 150 modulation 25 pitch 38""")
print "Listening..."
while True:
	try:
		with sr.Microphone() as source:
			answer = r.listen(source)
			user_log.append(r.recognize(answer))
		print "Analyzing Response..."

		if "pod bay" in r.recognize(answer) or "pod" in r.recognize(answer):
			print ("Dave: " + r.recognize(answer))
			print "HAL-9000: I'm sorry Dave. I'm afraid I can't do that."
			play("audio/cantdo.wav")
			print "Listening..."
			with sr.Microphone() as source:
				answer = r.listen(source)

			print "Analyzing Response..."
			if "emergency airlock" in r.recognize(answer) or "air locks" in r.recognize(answer):
				print ("Dave: " + r.recognize(answer))
				print "HAL-9000: Without your space helmet, Dave? You're going to find that rather difficult."
				runme("""say "Without your space helmet, Dave? You're going to find that rather difficult." using "Alex" speaking rate 160 modulation 20 pitch 38""")
				print "Listening..."
				with sr.Microphone() as source:
					answer = r.listen(source)
				print "Analyzing Response..."
			elif "why" in r.recognize(answer) or "why not" in r.recognize(answer):
				print ("Dave: " + r.recognize(answer))
				print "HAL-9000: This mission is too important for me to allow you to jeopardize it."
				play("audio/mission.wav")
				print "Listening..."
				with sr.Microphone() as source:
					answer = r.listen(source)
				print "Analyzing Response..."
			else:
				print ("Dave: " + r.recognize(answer))
				print "HAL-9000: ..."
				break

		elif "hello" in r.recognize(answer) or "hi" in r.recognize(answer): # this code is bad
			print ("Dave: " + r.recognize(answer))
			print "HAL-9000: Hello again, Dave."
			runme("""say "Hello again, Dave." using "Alex" speaking rate 160 modulation 20 pitch 38""")
			print "Listening..."
			with sr.Microphone() as source:
				answer = r.listen(source)
			print "Analyzing Response..."
		elif "how are you" in r.recognize(answer):

			print ("Dave: " + r.recognize(answer))
			print "HAL-9000: Good evening Dave. Everythings running smoothly. And you?"
			play("audio/hihal.wav")
			print "Listening..."
			with sr.Microphone() as source:
				answer = r.listen(source)
			print "Analyzing Response..."
			if "am good" in r.recognize(answer) or "am well" in r.recognize(answer):
				print ("Dave: " + r.recognize(answer))
				print "HAL-9000: I am glad to hear that you are doing well, Dave."
				runme("""say "I am glad to hear that you are doing well, Dave." using "Alex" speaking rate 185 modulation 15 pitch 37""")
				print "Listening..."
				with sr.Microphone() as source:
					answer = r.listen(source)
				print "Analyzing Response..."
			elif "not good" in r.recognize(answer) or "bad" in r.recognize(answer) or "not well" in r.recognize(answer):
				print ("Dave: " + r.recognize(answer))
				print "HAL-9000: Look Dave, I can see you're really upset about this. I honestly think you ought to sit down calmly, take a stress pill, and think things over."
				runme("""say "Look Dave, I can see you're really upset about this. I honestly think you ought to sit down calmly, take uhstress pill, and think things over." using "Alex" speaking rate 180 modulation 10 pitch 38""")
				print "Listening..."
				with sr.Microphone() as source:
					answer = r.listen(source)
				print "Analyzing Response..."
			else:
				break # add listen()


		elif "bye" in r.recognize(answer) or "exit" in r.recognize(answer):
			print ("Dave: " + r.recognize(answer))
			break
		elif "sing" in r.recognize(answer): # replace with hals song
			print ("Dave: " + r.recognize(answer))
			print "HAL-9000: Daisy, Daisy, Give me your answer do! Im half crazy, All for the love of you!"
			runme("""say "Daisy, Daisy, Give me your answer do! I'm half crazy, All for the love of you!" using "Alex" speaking rate 150 modulation 0 pitch 36""")
			break
		elif "about" in r.recognize(answer):
			print ("Dave: " + r.recognize(answer))
			print "HAL-9000 begins to tell you about itself..." #Future transcript
			play("audio/hal9000.wav")
			print "Listening..."
			with sr.Microphone() as source:
				answer = r.listen(source)
			print "Analyzing Response..."

		else: # if any of the conditions above are not met, except if speech is unintelligable
			print ("Dave: " + r.recognize(answer))
			print "HAL-9000: Im sorry Dave. I did not catch that. What did you say?"
			runme("""say "I'm sorry Dave. I did not catch that. What did you say?" using "Alex" speaking rate 185 modulation 15 pitch 37""")
			print "Listening..."
			with sr.Microphone() as source:
				answer = r.listen(source)
			print "Analyzing Response..."
	except LookupError:
		print "Could not understand audio, try again..."
		print "Listening..."
		continue

print "HAL-9000: This conversation can serve no purpose anymore. Goodbye."
play("audio/Good_Bye_1_.wav")

print user_log

