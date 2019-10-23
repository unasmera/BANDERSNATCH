#Diese Funktion ermöglicht dir txt Dokumente die du in diesen Ordner legst als
#Dictionary für die unteren Funktionen zu verwenden.
def producedictionary (file):
    with open (file, "r") as t:
        x = t.read ()
    result = {}
    for absatz in x.split ("\\"):
        position = absatz.find (":")
        key = absatz[:position]
        inhalt = absatz[position+2:].strip()
        result[key] = inhalt
    return result

#Das sind die Dictionaries in denen entweder der Text für die Funktionen steht
#oder sie verweisen auf den Text in den jeweils abgelegten Dateien.
Ang = {"yes":"good", "no":"Ready Player One?"}
Nae = {"tabea":"Hello Tabea, Here's your first decision: would you like to take the red pill or the blue pill?"}
Pie = producedictionary ("Pie.txt")
I_Ad = producedictionary ("I_Ad.txt")

#Das ist die Generische Funktion für die Antwortfunktionen.
def generate (variable,prompt="",invalid=""):
    while True:
        x = input(prompt).lower()
        for word in variable:
            if word == x:
                print (variable[word])
                return word
        else:
            print(invalid)

#Der Spieler gibt an ob er bereit ist
def Anfang ():
    print ("Ready Player One?")
    while "no" == generate (Ang,"","Try again"):
        pass

#Der Spieler gibt seinen Namen ein
def Name ():
    print ("Welcome to BANDERSNATCH")
    print ("Insert your name to play")
    generate (Nae,"","No, your real name.")

#Der Spieler entscheidet sich für die Rote oder Blaue Pille und erhält den
#jeweiligen Antworttext
def Pille ():
    generate(Pie,"","Choose a pill")

#A: Es wird erklärt wer der Spielemacher ist
def I_A ():
    while "d" != generate(I_Ad,"",I_Ad["c"]):
        while "c" == generate(I_Ad,"",I_Ad["c"]):
            pass
        if "d" == generate(I_Ad,"",I_Ad["c"]):
            break



Anfang()
Name ()
Pille ()
I_A()

