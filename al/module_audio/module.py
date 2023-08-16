import pyttsx3

def run(txt="Bonjour et Bienvenue dans le projet ROBOTECH... Et n'oublier pas: on est la pour s'amuser..."):
    print("Hello Module Audio")

    # To initialize the motor
    engine = pyttsx3.init()

# *********************************************************************
    # Define the text to be converted into speech:
    txt_1 = "life is a game... enjoy it!"
    txt_2 = "Les chaussettes de l'archiduchesse sont-elles sèches?"
    txt_3 = "42 est, sans aucun doute, la meilleure ecole du monde."
    txt_4 = "42 is, without doubt, the best school in the world."
# *********************************************************************

    # Adjusting speech rate and volume:
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 45)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 0.50)

    # Select language and track type:
    voices = engine.getProperty('voices')
    # engine.setProperty('voice', 'en-us')
    engine.setProperty('voice', voices[1].id)
    # for voice in voices:
    #    print("id ", voice)

    # Print the message:
    engine.say(txt)
    engine.say(txt_1)
    engine.runAndWait()
