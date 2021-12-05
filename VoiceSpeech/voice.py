import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)
engine.setProperty('rate', 200)
# engine.say("Hello, How are you ?")
engine.runAndWait()

def speak(str):
    engine.say(str)
    engine.runAndWait()

speak("""
While most of North Korea’s 25 million citizens cannot 
afford more than the simplest garb, leather jackets reminiscent of 
the country’s all-powerful dictator have become the go-to fashion 
in the capital of Pyongyang and other cities where members of the upper 
crust of military officers, government officials and members 
of the ruling Workers’ Party live and work.
""")
