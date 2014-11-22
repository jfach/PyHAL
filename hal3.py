import random
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

	#play stream
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




print "<=====> PyHAL-9000 v0.2.1.1 <======>"
play("audio/moment.wav")
print "Mini Changelog:\n"
print "- 0.1: Added Google Speech Recognition"
print "- 0.1.1: Added Apple Scripts For HAL 2001 Voice"
print "- 0.1.2: Added PyAudio Support For Authentic HAL Playback"
print "- 0.1.2.1: Added Really Bad Handling For LookupError"
print "- 0.2: Implemented Better Handling For LookupError"
print "- 0.2.1: Code Runs Faster (fixed a design flaw where audio was parsed unnecessarily)"
print "- 0.2.1.1: Began using RandInt to add variety. Added and edited phrases\n"
print "- 0.3: Removed Mac OS X Dependency. Added More Audio.\n"
raw_input('Press <ENTER> to continue')


user_log = []

print "HAL-9000: Hello, Dave."
#runme("""say "Hello Dave." using "Alex" speaking rate 150 modulation 25 pitch 38""")
print "Listening..."
while True:
	try:
		with sr.Microphone() as source:
			answer = r.listen(source)
			response = r.recognize(answer)
		print "Analyzing Response..."

		if "pod bay" in response or "pod" in response:
			print ("Dave: " + response)
			print "HAL-9000: I'm sorry Dave. I'm afraid I can't do that."
			play("audio/cantdo.wav")
			print "Listening..."
			with sr.Microphone() as source:
				answer = r.listen(source)
				response = r.recognize(answer)

			print "Analyzing Response..."
			if "emergency airlock" in response or "air locks" in response:
				print ("Dave: " + response)
				print "HAL-9000: Without your space helmet, Dave? You're going to find that rather difficult."
				play("audio/helmet.wav")
				print "Listening..."
				with sr.Microphone() as source:
					answer = r.listen(source)
					response = r.recognize(answer)
				print "Analyzing Response..."
			elif "why" in response or "why not" in response:
				print ("Dave: " + response)
				print "HAL-9000: This mission is too important for me to allow you to jeopardize it."
				play("audio/mission.wav")
				print "Listening..."
				with sr.Microphone() as source:
					answer = r.listen(source)
					response = r.recognize(answer)
				print "Analyzing Response..."
			else:
				print ("Dave: " + response)
				print "HAL-9000: ..."
				break

		elif "how are you" in response:
			coin_flip = random.randint(1,2)
			print ("Dave: " + response)
			if coin_flip == 1:
				print "HAL-9000: Good evening Dave. Everythings running smoothly. And you?"
				play("audio/hihal.wav")
			else:
				print "HAL-9000: I'm completely operational and all my circuits are functioning perfectly. And you?"
				play("audio/operational2.wav")
			print "Listening..."
			with sr.Microphone() as source:
				answer = r.listen(source)
				response = r.recognize(answer)
			print "Analyzing Response..."
			# if "am good" in response or "am well" in response:
# 				print ("Dave: " + response)
# 				print "HAL-9000: I am glad to hear that you are doing well, Dave."
# 				runme("""say "I am glad to hear that you are doing well, Dave." using "Alex" speaking rate 185 modulation 15 pitch 37""")
# 				print "Listening..."
# 				with sr.Microphone() as source:
# 					answer = r.listen(source)
# 					response = r.recognize(answer)
# 				print "Analyzing Response..."
			if "not good" in response or "bad" in response or "not well" in response:
				print ("Dave: " + response)
				print "HAL-9000: Look Dave, I can see you're really upset about this. I honestly think you ought to sit down calmly, take a stress pill, and think things over."
				play("audio/stresspill2.wav")
				print "Listening..."
				with sr.Microphone() as source:
					answer = r.listen(source)
					response = r.recognize(answer)
				print "Analyzing Response..."
			else:
				break # add listen()


		elif "bye" in response or "exit" in response:
			print ("Dave: " + response)
			break
		elif "sing" in response: # replace with hals song
			print ("Dave: " + response)
			print "HAL-9000: Daisy, Daisy..."
			play("audio/daisy.wav")
			print "Listening..."
			with sr.Microphone() as source:
				answer = r.listen(source)
				response = r.recognize(answer)
			print "Analyzing Response..."
		elif "about" in response:
			print ("Dave: " + response)
			print "HAL-9000 begins to tell you about itself..." #Future transcript
			play("audio/hal9000.wav")
			print "Listening..."
			with sr.Microphone() as source:
				answer = r.listen(source)
				response = r.recognize(answer)
			print "Analyzing Response..."

		else: # if any of the conditions above are not met, except if speech is unintelligable
			print ("Dave: " + response)
			print "HAL-9000: Im sorry Dave. I didn't catch that. What did you say?"
			print "Listening..."
			with sr.Microphone() as source:
				answer = r.listen(source)
				response = r.recognize(answer)
			print "Analyzing Response..."
	except LookupError:
		print "Could not understand audio, try again..."
		print "Listening..."
		continue

print "HAL-9000: This conversation can serve no purpose anymore. Goodbye."
play("audio/Good_Bye_1_.wav")


