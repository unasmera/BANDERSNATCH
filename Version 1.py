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

#print ("You are sitting in front of the screen, reading a text. The letters are written in COURIER NEW and built a nice contrast to the black background. Today is a boring day. You stood up at the same time as usual, had a non remarkable breakfast and up until now you cannot recall having done anything actually productive. The text you are reading is about obvious stuff and also not very interesting. Fed up, you think about what to do next, as suddenly something unexpected happens.")
Ang = {"yes":"good", "no":"Ready Player One?"}
Nae = {"tabea":"Hello Tabea, Here's your first decision: would you like to take the red pill or the blue pill?"}
Pie = producedictionary ("Pie.txt")
I_Ad = producedictionary ("I_Ad.txt")


def generate (variable,prompt="",invalid=""):
    while True:
        x = input(prompt).lower()
        for word in variable:
            if word == x:
                print (variable[word])
                return word
        else:
            print(invalid)

def Anfang ():
    print ("Ready Player One?")
    while "no" == generate (Ang,"","Try again"):
        pass

def Name ():
    print ("Welcome to BANDERSNATCH")
    print ("Insert your name to play")
    generate (Nae,"","No, your real name.")

def Pille ():
    generate(Pie,"","Choose a pill")

def I_A ():
    while "c" == generate(I_Ad,"",I_Ad["c"]):
        pass

def Anfang1 (x):
    while True:
        if x == "no" or x == "No":
            print ("Ready Player One?")
        elif  x== "yes" or x == "Yes":
            print ("good")
            return True
            break
        else:
            print ("Try again")
            print ("Ready Player One?")
        x = input().lower()

def Name1 (name):
    while True:
        if name == "Yubin" or name == "Quirin Prummer" or name == "quirin":
            print ("Hello Yubin, here's your first decision: Would you like the red pill, or the blue pill?")
            return True
            break
        else:
            print ("No, your real name")
            name = input()

def Pille1 (colour):
    while True:
        if colour == "red" or colour == "Red" or colour == "red pill" or colour == "Red Pill":
            print ("You are now in the BANDERSNATCH. A never ending system of decisions.")
            print ("Nothing you say or do is of your own free will. Your fate has long been")
            print ("decided before you even thought about acting. There are people like you,")
            print ("who are aware of the situation, and then there are people who are not.")
            print ("Sleepwalkers unable to wake up if not for their own revelation.")
            print ("Your mission, if you take it, is to terminate the decision maker") 
            print ("The Sleepwalkers will do anything to stop you in doing so.")
            print ("Choose how you would like to proceed:")
            print ("A: Who is the decision maker")
            print ("B: Who Am I?")
            print ("C: I do not take the mission")
            return True
            break
        elif colour == "blue" or colour == "Blue" or colour == "blue pill" or colour == "Blue Pill":
            print ("As you wake up in your bed, everything seems normal at first. Dark orange light is")
            print ("shimmering through your curtain covered window and sprinkles the matress with light yellow spots.")
            print ("You get rid of the far too tiny piece of fabric that you used as a blanket")
            print ("and roll over, off the grubby mattress and onto the concrete floor. Your head hurts")
            print ("as though an elefant tried to dance Cha-Cha inside of it and you can't remember")
            print ("how you got into your bed last night. Frantically you get up and start searching for")
            print ("the mug of cold coffee that you must have left somewhere here yesterday evening.")
            print ("A: Look on the construction you'd like to call desk")
            print ("B: Look in the toilett")
            return False
            break
        else:
            print ("Choose a pill")
            colour = input()

def I_A1 (answer):
    if answer == "A" or answer == "a":
        print ("The decision maker is here and yet is not. It is a construct, an illusion if you will.")
        print ("Unable to fully wrap ones mind about its existance, one can yet find its traces in")
        print ("everything one does. It is almighty and yet has no power whatsoever. Take on the mission")
        print ("and you will surely stumble upon its controversies.")
        print ("Choose how you would like to proceed:")
        print ("A: Who am I?")
        print ("B: Start the mission!")
        return False
    elif answer == "B" or answer == "b":
        print ("You are Player One")
        print ("A: Who is the decision maker?")
        print ("B: Start the mission!")
        return True
    else:
        print ("ERROR 404")
        print ("A: Who is the decision maker?")
        print ("B: Who am I?")
        print ("C: I do not take the mission")
        answer = input()

Anfang()
Name ()
Pille ()
I_A()

#print ("Ready Player One?")
#a = input().lower()
#if Anfang (a) == True:
 #   print ("Welcome to BANDERSNATCH")
 #   print ("Insert your name to play")
 #   b=input()
 #   if Name(b) == True:
 #       c=input()
 #       Pille(c)



#print ("Ready Player One?")
#a = input()
#if [(a == ("yes")) or (a == ("Yes"))]:
 #   print ("good")
#elif [(a == ("no")) or (a == ("No"))]:
 #   print ("Ready Player One?")
           # else:
            #    print ("Try again")
