# @ Made by Mansour & Kush - 28-10-2021
# IDS Autumn #1 Hand In assignment.
# This is a Personal Assistance bot, just like Cortana and Alexa.
# The goal of this program is to implement different APIs features,
# such as the things listed bellow. We want our PA(donna) to help us with different queries.

# Adding Speech Recognizer (speech_recognition)
# Pyttsx3 is used to text to speech
# PyWhatKit offers different features to our program, including YouTube
# Importing datetime to get the time
# Importing wikipedia API
# Importing pyjokes for a library of jokes
# Importing webbrowser for google maps location search

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()

# This 'engine' is used to form a text to speech 'fx. engine.say'.
engine = pyttsx3.init()
# Declaring voices to be the property of all voices
# Then we set the property of all the voices to the index of '1', which is the voice ID.
# Index 1 is female voice, and Index 0 is male, in this case we want a female voice.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    # Try/testing microphone
    try:

        # Using microphone as a source, calling to speech recognizer to listen to the source
        # Source is the source of the audio
        # The speech recognition is using the Google speech API

        with sr.Microphone() as source:
            print('Hello, how can I help you?')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # If 'donna' is mentioned it will answer to your command.
            if 'donna' in command:
                # Example you want search for a song name, you don't want 'donna' to be a part of the search
                # This way we can exclude the output 'donna'
                command = command.replace('donna', '')
                # To test if it works, we print command
                print(command)

    except:
        pass
    return command

    # calling the source command


# Running our personal assistant
# Declaring 'run donna'
# Here we will be including all the ability for our PA.
def run_donna():
    command = take_command()
    print(command)
    # Here we make use of the 'play' function to search and play the input of a song-name
    # Just like before, we replace the 'play' so it doesn't print it in the output.
    # Adding the pywhatkit to search for songs.
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

        # Time & Date package
        # strftime (formatting how we want the program to output the time)
        # elif = else if
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(' Current time is ' + time)

        # Wikipedia Package
        # wikipedia.summary(person, 1) = By this line we only get information of 1 sentence.
        # Printing the info and making the PA to speech
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

        # PyJokes is a package full of random jokes
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'find location' in command:
        location = command.replace('find location', '')
        url = 'https://www.google.com/maps/place/' + location + '/amp;'
        webbrowser.get().open(url)
        print('Here is the location of ' + location)
        talk('Here is the location of ' + location)

    # If the PA doesn't understand you, she will ask you again.
    else:
        talk('Please say that again.')


# Looping, so that the program keeps running after a command.
while True:
    run_donna()
