import speech_recognition 
import pyttsx3
import google.generativeai as genai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 140)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """Listen for a voice command and return the recognized text."""
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("I'm listening... Please speak clearly.")
        r.pause_threshold = 1.0
        r.energy_threshold = 189
        try:
            audio = r.listen(source, timeout=10)
        except Exception as e:
            print("Sorry, I couldn't hear anything. Please check your microphone.")
            return "None"
    try:
        print("Processing your command...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        return query
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return "None"

def main():
    print("Hello BOSS.")
    while True:
        query = takeCommand().lower()
        if query != "none":
            genai.configure(api_key="GOOGLE GEMINI API KEY HERE")
            model = genai.GenerativeModel("gemini-2.0-flash-lite") #please check the available models of gemini
            response = model.generate_content(f"Sir : {query}")

            if response.text:
                response_text = str(response.text).strip()
                print(f"NAVIDS: {response_text}")
                speak(response_text)
            else:
                raise Exception("Empty response from Gemini")
                    
if __name__ == "__main__":
    main()