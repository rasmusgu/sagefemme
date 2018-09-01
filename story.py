import time
import random
import mysql.connector

from modules import *
#from game import *

db = mysql.connector.connect(host="localhost",
                             user = "root",
                             passwd = "poop",
                             db = "sagefemme",
                             buffered = True)


def errorInput():
    print("EROR: Input not recognised")
    return

def print_pause(lines):
    for line, pause in lines:
        print(line)
        time.sleep(pause)
    return

def chapter1():
    print_pause([
    ("...", 2),
    ("'Charlotte.'", 2),
    ("'Charlotte!'", 2),
    ("'CHARLOTTE!'", 0)
    ])
    x = input(">> ")
    print("...")
    time.sleep(1)
    print("You wake up, your head throbbing like after being bludgeoned with a hammer.")
    input(">> ")
    print("'What the hell are you doing here? You had an appointment with a very angry pregnant customer an hour ago.'" +"\n"+ "...") 
    time.sleep(3)
    print("(1) ..." +"\n"+ "(2) Haven't you learned to knock?" +"\n"+ "(3) *go back to sleep*")
    xy=5
    while xy!="1" or xy!="2" or xy!="3":
        xy = input("> ")
        if xy=="3":
            print("Marissa: 'Charlotte. Are you seriously going straight back to sleep in front of your boss while she is berating you?'"  +"\n"+ "(1) Yes."  +"\n"+ "(2) Fine. What is it?" +"\n"+ "(3) *make forced snoring sound*")
            input("> ")
            break
        elif xy=="2":
            print("Marissa: 'You think this is funny?'")
            x=input("(1) Yes." +"\n"+ "(2) I think you think I think this is funny" +"\n"+ "(3) Look, Marissa. I've had a bad day. I just needed to recharge a bit, and this is the only place where I until now thought I would be left alone for five seconds." +"\n"+ "> ")
            break
        elif xy==1:
            print("Marissa: 'You've got nothing to say for yourself?'" + "\n" + "(1) I'm sorry, m'am. This won't happen again." +"\n"+ "(2) Fine. What is it?" +"\n"+ "(3) *stare*")
            input("> ")
            break
        else:
            print("ERROR: input not recognised")
    print("Marissa: 'Whatever. Another one of our midwives called in sick, so I'm going to have to have you report to delivery room 213 immediately. And Charlotte... I covered for you this time, but do this again and don't expect any more special treatment.'"  +"\n"+ "*she walks out and closes the door behind her*")
    print("You know she is right. She is your boss after all.")
    input(">> ")
    print("Remember to 'look' around yourself!")
    return
    
def chapter2():
    print("You arrive into the labor room, still breaking a cold sweat from your earlier hit. It's not easy balancing a drug addiction and work, but it's not like you have a choice, you remind yourself. The 'customer' is already waiting for you on the delivery table, her legs spread and shaking. You ascertain yourself with a fist clench before promptly walking over to her and introducing yourself." +"\n"+ "(1) Hello, my name is Charlotte. Don't worry; you are in very capable hands." +"\n"+ "(2) Is this your first?" +"\n"+ "(3) PUSH! ...just kidding. Please don't push yet lest you want a birth complication.")
    xy=5
    x=5
    while xy!="1" or xy!="2" or xy!="3":
        xy = input("> ")
        if xy=="1":
            print("Pregnant woman: 'Are you a doctor? I need a doctor. I can feel my baby coming out!'" +"\n"+ "(1) Yes, I'm a doctor."  +"\n"+ "(2) I'm better than a doctor for cases like these, dear. I'm a midwife." +"\n"+ "(3) I am a certified midwife specialised in childbirth with over 10 years of experience in the field. You have nothing to worry about.")
            while x!="1" or x!="2" or x!="3":
                x=input("> ")
                if x=="1" or x=="2" or x=="3":
                    break
                else:
                    errorInput()
            break
        elif xy=="2":
            print("Marissa: 'Wha- yes. I'm a littler nervous. The father isn't here yet.'")
            while x!="1" or x!="2" or x!="3":
                x=input("(1) It's perfectly natural to be nervous." +"\n"+ "(2) Well, father or no father, I swear I am bringing this child into your arms. Safe and sound." +"\n"+ "(3) If it's any consolation, men tend to be less courageous than women in labour rooms anyway." +"\n"+ "> ")
                if x=="1" or x=="2" or x=="3":
                    break
                else:
                    errorInput()
            break
        elif xy=="3":
            print("Pregnant woman: 'Wait, what? Is my baby in danger?'" + "\n" + "(1) I'm sure your baby is fine." +"\n"+ "(2) That's what I'm here to find out." +"\n"+ "(3) Trust me. I'm doing everything I can to make sure that you will be able to hold your baby and that both of you will be healthy.")
            while x!="1" or x!="2" or x!="3":
                x=input("> ")
                if x=="1" or x=="2" or x=="3":
                    break
                else:
                    errorInput()
            break
        else:
            print("ERROR: input not recognised")
    print("Just as you're about to ask her for her name, she suddenly lets out a deafening shriek and before you realise, your body is working in autopilot mode through muscle memory alone. When your mind finally catches up, you find the baby's head poking out of her groin. You remind her to breath and to prepare for a big push...")
    input(">> ")
    print_pause([
    ("...", 1),
    ("......", 1),
    ("Baby: 'Äääääääääääääääh!'", 0),
	("...",1)
    ])
    x=""
    while x!="1" or x!="2":
        x=input("(1) Congratulations, it's a boy!" +"\n"+ "(2) Congratulations, it's a girl!" +"\n"+ "> ")
        if x=="1":
            babyGender="xy"
            babyPronoun="He's"
            babyName="Hannibal"
            break
        elif x=="2":
            babyGender="xx"
            babyPronoun="She's"
            babyName="Cleopatra"
            break
        else:
            errorInput()
    print("The door flies open and a man in his thirties stumbles inside. His unkempt hair, dark eye circles and the musky odour suggest that he has been up for a while. He goes straight to the new mother and gets on his knees: 'Oh, Jasmine!",babyPronoun,"beautiful! You both are. I couldn't be happier right now. I'm so sorry I wasn't able to make it.'" +"\n"+ "Jasmine: 'Don't be silly, Marco. We did just fine,",babyName,"and I." +"\n"+ "Marco: 'You chose a name already?",babyName+". I like it.'")
    input(">> ")
    print("As you come to after the adrenaline rush, you look at the baby you just helped into this world and can't help seeing your own child in its crying red face. You start to get lost in your memories, in a sort of trans, but snap out of it as the parents direct your attention to the baby's umbilical cord." +"\n"+ "'Would the father like the honour?', you ask." +"\n"+ "Marco: 'I'm quite alright, thank you. I'm not that good with blood" +"\n"+ "It was apparent from the paleness of his face, but you thought it worth a short to ask.")
    #fix pl0x
    while x!="take scissors":
        x=input("The scissors are on the medical table next to you."  +"\n"+ "> ")
        if x=="take scissors":
            break
        elif x=="take":
            while x!="1":
                x=input("Take: (1) Scissors" +"\n"+ "> ")
            break
        else:
            errorInput()
    print("You take the scissors and prepare yourself to cut the umbilical cord.")
    while x!="cut umbilical cord" or x!="cut the umbilical cord" or x!="cut cord":
        x=input("> ")
        if x=="cut umbilical cord" or x=="cut the umbilical cord" or x=="cut cord":
            break
        elif x=="cut":
            while x!="1":
                x=input("Cut: (1) Umbilical cord"  +"\n"+ "> ")
            break
        else:
            errorInput()
    print("You've done this a thousand times, yet perhaps it was due to your little morphine assisted siesta earlier -- or maybe thoughts of your own child clouded your mind. Whatever the case is, the rest is a blur, but as you come to, the hysterical parents are holding their profusely bleeding baby and screaming for help.") 
    input(">> ")
    print("You drop the scissors and dash out of the room. You glide down the hallways, leaving bloody handprints behind on the walls. Running fully on instinct, you let your feet guide the way, and surely enough, you eventually find yourself at the door of the 2nd floor medicinal supply room...")

    #moves player to room 208
    cur = db.cursor()
    sql = "UPDATE player set locationID = 208"
    cur.execute(sql)
    sql = "commit"
    cur.execute(sql)
    cur.close()

    #locks room 213
    cur = db.cursor()
    sql = "UPDATE tile SET locked = 1 WHERE locationID = 213"
    cur.execute(sql)
    sql = "commit"
    cur.execute(sql)
    cur.close()

    #update all corridors and patient rooms to dark corridors and dark patient rooms
    cur = db.cursor()
    sql = "UPDATE tile SET tiletypeID=10 WHERE tiletypeID=1"
    cur.execute(sql)
    sql = "commit"
    cur.execute(sql)
    cur.close()
    #development/testing purposes
    print("The lights suddenly go out")
    return

def ratSequence():
    print("Should I fight the giant rat? I guess I have no choice.")
    x=input
    while x!="equip scissors":
        print("You need to equip something to fight the giant rat.")
        x=input("> ")
        if x=="look":
            look()
    print("FIGHT!")
    print("(1) Fight the giant rat. (2) Try to run away.")

    x="5"
    while x!="1" or x!="2":
        x = input("> ")
        if x=="2":
            print("You try to run away. But the rat pins you down, bringing its fangs closer and closer... GAME OVER")
            #restart()
            input(">> ")
            exit()
            break     
        elif x=="1":
            print("You equip the scissors" + "\n" + "(1) Stab the rat. " +"\n"+ "(2) Run away. ")
            while x!="1" or x!="2":
                x=input("> ")
                if x=="1":
                    print_pause([
                    ("You stab the giant rat.", 2),
                    ("You see his blood trails on the ground and you can hear the rat just getting angrier.", 2),
                    ("It looks like he is trying to attack you.", 0)
                    ])
                    break
                elif x=="2":
                    print("You try to run away. But the rat pins you down, bringing its fangs closer and closer... GAME OVER")
                    #restart()
                    input(">> ")
                    exit()
                    break
            print("(1) Stab the rat again. (2) Try to dodge his attack. ")
            while x!="1" or x!="2":
                x = input("> ")
                if x=="2":
                    print("You successfully dodged the rat. The rat hit his head on the wall. He looks like he is unconscious")
                    print("The rat seems to be sobering up. (1) FINISH HIM! (2) Stare at its unconscious body.")
                    while x!="1" or x!="2":
                        x = input("> ")
                        if x=="2":
                            print("The rat wakes up. He stares at and and bites your head off.")
                            restart()
                        elif x=="1":
                            print("You successfully killed the rat. Congratulations.")
                            break     
                        else:
                            errorInput()
                elif x=="1":
                    print("OH NO! The rat killed you. GAME OVER")
                    #restart()
                    input(">> ")
                    exit()
                    break     
                else:
                    errorInput()
            break
    
        else:
            errorInput()
    return

def scissorSequence():
    print_pause([
    ("You see a patient wandering around mumbling incoherently.", 2),
    ("It appears they have scissors in their hand. Covered in blood.", 2),
    ("OH MY GOD! They are sucking the blood, resting their tongue on the blades.", 2),
    ("The scissors might come in handy. Doesn't seem like your friend has much use for them. Might as well take them.", 2),
    ("Much to your disgust, you decide to get close to them and try to communicate.", 2),
    ("(1) Take them with force.(2) Take them gently. (3) Ignore.",0),
    ])

    xy="5"
    while xy!="1" or xy!="2" or xy!="3":
        xy = input("> ")
        if xy=="3":
            print("You feel bad for him. You can not ignore him." + "\n" + "(1) Take the scissors? " +"\n"+ "(2) Take the scissors! " +"\n"+ "(3) Tale the scissors. ")
            input("> ")
            break
        elif xy=="2":
            print("Patient::'????!?!????'. He makes a creepy smile."+ "\n" + "(1) Smile back at him ;). " +"\n"+ "(2) Try to reach the scissors carefully. " +"\n"+ "(3) I'm confused. ")
            input("> ")
            break       
        elif xy=="1":
            print("Patient:'Nein, nein! Scheisse verpiss dich!'" + "\n" + "(1) Smile at him " +"\n"+ "(2) Kick him " +"\n"+ "(3) Slap him ")
            input("> ")
            break
        else:
            print("ERROR: input not recognised")
    print("You take the scissors.")
    return
    
