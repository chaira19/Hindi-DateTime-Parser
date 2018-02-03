def voice_input():
    
    #!/usr/bin/env python3
    # Requires PyAudio and PySpeech.
     
    import speech_recognition as sr
     
    # Record Audio
    r = sr.Recognizer()
    m = sr.Microphone()

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
     
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        a=r.recognize_google(audio)
        #time.sleep(1)
        
        #stop_listening = r.listen_in_background(m, callback)
       
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    print (a)
    return a



def voice_output(ans):
    import pyttsx3
    import time
    eng=pyttsx3.init()
    eng.say(ans)
    eng.runAndWait()
    
