import time
import random
import mysql.connector

from story import *
#import game

#just some stuff
x = ""
hpbar = 50
mapFlip = "1"
#stats = "Name:",player_name,"HP:",hpbar,"Status effects:",status

#wip:
    # - move
    # - inspect
    # - labor event (story)
    # - fight with rat (story)
    # - 

db = mysql.connector.connect(host="localhost",
                             user = "root",
                             passwd = "poop",
                             db = "sagefemme",
                             buffered = True)

#cur = db.cursor()

#cur.execute("SELECT * FROM ENEMY")

#data = cur.fetchall ()


#add parameters so we don't need  to make a different function for everything

def leave():
    print("Bye")
    db.rollback
    db.close()
    input(">>")
    exit()

#save space
def errorMovement():
    print("ERROR: You can't move there")
    return

def errorInput():
    print("ERROR: Input not recognised")
    return

def errorTake():
    print("ERROR: Item not available")
    return

def moveNorth():
    #if direction == "n" or "north":
    #print("Function: 'move' initiated")
    cur = db.cursor()
    sql = "select locationID from player"
    cur.execute(sql)
    result = cur.fetchone()
    for row in result:
        print(row)
        if row == 103:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=104"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
            cur.close()
        elif row == 104:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=105"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
            cur.close()
        elif row == 105:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=106"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
        elif row == 106:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=107"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
        elif row == 111:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=112"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
        elif row == 112:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=113"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
        #2nd floor
        elif row == 203:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=204"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
            cur.close()
        elif row == 204:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=205"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
            cur.close()
        elif row == 205:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=206"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
        elif row == 206:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=207"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
        elif row == 211:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=212"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
        elif row == 212:
            cur = db.cursor()
            sql = "SELECT locked from tile where locationID=213"
            cur.execute(sql)
            result = cur.fetchone()
            for row in result:
                if row == 0:
                    cur = db.cursor()
                    sql = "UPDATE player SET locationID=213"
                    cur.execute(sql)
                    sql = "commit"
                    cur.execute(sql)
                    print("You move North" +"\n"+ "...")
                    time.sleep(1)
                    chapter2()
                else:
                    print("You don't want to go there")
            cur.close()
        #3rd floor
        elif row == 303:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=204"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
            cur.close()
        elif row == 304:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=205"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
            cur.close()
        elif row == 305:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=206"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
        elif row == 306:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=207"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
        elif row == 310:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=311"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
        elif row == 311:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=312"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move North")
        else:
            errorMovement()
        return

def moveEast():
    #print("Function: 'move' initiated")
    cur = db.cursor()
    sql = "select locationID from player"
    cur.execute(sql)
    result = cur.fetchone()
    for row in result:
        print(row)
        if row == 101:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=104"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
            cur.close()
        elif row == 102:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=106"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
            cur.close()
        elif row == 104:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=108"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
        elif row == 105:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=109"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
        elif row == 106:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=110"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
        elif row == 109:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=112"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
        #2nd floor
        elif row == 201:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=204"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
            cur.close()
        elif row == 202:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=206"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
            cur.close()
        elif row == 204:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=208"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
        elif row == 205:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=209"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
        elif row == 206:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=210"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
        elif row == 209:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=212"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
        #floor3
        elif row == 301:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=304"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
            cur.close()
        elif row == 302:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=306"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
            cur.close()
        elif row == 304:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=308"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
        elif row == 305:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=309"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
        elif row == 309:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=311"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move East")
        else:
            errorMovement()
    return

def moveSouth():
    #print("Function: 'move' initiated")
    cur = db.cursor()
    sql = "select locationID from player"
    cur.execute(sql)
    result = cur.fetchone()
    for row in result:
        print(row)
        if row == 104:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=103"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
            cur.close()
        elif row == 105:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=104"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
            cur.close()
        elif row == 106:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=105"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        elif row == 107:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=106"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        elif row == 112:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=111"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        elif row == 113:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=112"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        #floor2
        elif row == 204:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=203"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
            cur.close()
        elif row == 205:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=204"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
            cur.close()
        elif row == 206:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=205"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        elif row == 207:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=206"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        elif row == 212:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=211"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        elif row == 213:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=212"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        #floor3
        elif row == 304:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=303"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
            cur.close()
        elif row == 305:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=304"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
            cur.close()
        elif row == 306:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=305"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        elif row == 307:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=306"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        elif row == 311:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=310"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        elif row == 312:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=311"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move South")
        else:
            errorMovement()

def moveWest():
    #print("Function: 'move' initiated")
    cur = db.cursor()
    sql = "select locationID from player"
    cur.execute(sql)
    result = cur.fetchone()
    for row in result:
        print(row)
        if row == 104:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=101"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
            cur.close()
        elif row == 106:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=102"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
            cur.close()
        elif row == 108:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=104"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
        elif row == 109:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=105"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
        elif row == 110:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=106"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
        elif row == 112:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=109"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
        #floor2
        elif row == 204:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=201"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
            cur.close()
        elif row == 206:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=202"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
            cur.close()
        elif row == 208:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=204"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
        elif row == 209:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=205"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
        elif row == 210:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=206"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
        elif row == 212:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=209"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
        #floor3
        elif row == 304:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=301"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
            cur.close()
        elif row == 306:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=302"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
            cur.close()
        elif row == 308:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=304"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
        elif row == 309:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=305"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
        elif row == 311:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=309"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move West")
        else:
            errorMovement()
    return

def move():
    #print("Function: 'move' initiated")
    cur = db.cursor()
    sql = "select locationID from player"
    cur.execute(sql)
    result = cur.fetchone()
    #cur.execute(sql)
    for row in result:
        print(row)
        #first floor
        if row == 101:
            x = input("Move to: East" +"\n"+ "> ")
            if x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=104"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            else:
                errorMovement()
        if row == 102:
            x = input("Move to: East" +"\n"+ "> ")
            if x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=106"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            else:
                errorMovement()
        if row == 103:
            x = input("Move to: North - Up" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=104"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x=="up" or x=="UP":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=203"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move up the stairs")
                cur.close()
            else:
                errorMovement()
        if row == 104:
            x = input("Move to: North/West/East/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=105"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=108"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=103"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=101"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        if row == 105:
            x = input("Move to: North/West/East/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=106"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=109"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=104"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            else:
                errorMovement()
        if row == 106:
            x = input("Move to: North/West/East/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=107"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=110"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=105"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=102"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        if row == 107:
            x = input("Move to: South - Up" +"\n"+ "> ")
            if x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=106"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            elif x=="up" or x=="UP":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=207"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move up the stairs")
                cur.close()
            else:
                errorMovement()
        if row == 108:
            x = input("Move to: West" +"\n"+ "> ")
            if x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=104"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        if row == 109:
            x = input("Move to: West/East" +"\n"+ "> ")
            if x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=112"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=105"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        if row == 110:
            x = input("Move to: West" +"\n"+ "> ")
            if x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=106"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        if row == 111:
            x = input("Move to: North" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=112"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            else:
                errorMovement()
        if row == 112:
            x = input("Move to: North/West/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=113"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=111"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=109"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
            else:
                errorMovement()
        if row == 113:
            x = input("Move to: South" +"\n"+ "> ")
            if x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=112"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
            else:
                errorMovement()
        #floor2
        elif row == 201:
            x = input("Move to: East" +"\n"+ "> ")
            if x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=204"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            else:
                errorMovement()
        elif row == 202:
            x = input("Move to: East" +"\n"+ "> ")
            if x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=206"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            else:
                errorMovement()
        elif row == 203:
            x = input("Move: North - Up/Down" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=204"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x=="up" or x=="UP":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=303"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move up the stairs")
                cur.close()
            elif x=="down" or x=="Down":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=103"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move down the stairs")
                cur.close()
            else:
                errorMovement()
        elif row == 204:
            x = input("Move to: North/West/East/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=205"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=208"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=203"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=201"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        elif row == 205:
            x = input("Move to: North/West/East/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=206"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=209"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=204"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            else:
                errorMovement()
        elif row == 206:
            x = input("Move to: North/West/East/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=207"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=210"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=205"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=202"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        elif row == 207:
            x = input("Move to: South - Up/Down" +"\n"+ "> ")
            if x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=206"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            elif x=="up" or x=="UP":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=307"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move up the stairs")
                cur.close()
            elif x=="down" or x=="Down":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=107"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move down the stairs")
                cur.close()
            else:
                errorMovement()
        elif row == 208:
            x = input("Move to: West" +"\n"+ "> ")
            if x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=204"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        elif row == 209:
            x = input("Move to: West/East" +"\n"+ "> ")
            if x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=212"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=205"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        elif row == 210:
            x = input("Move to: West" +"\n"+ "> ")
            if x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=206"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        elif row == 211:
            x = input("Move to: North" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=212"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            else:
                errorMovement()
        elif row == 212:
            x = input("Move to: North/West/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "SELECT locked from tile where locationID=213"
                cur.execute(sql)
                result = cur.fetchone()
                for row in result:
                    if row == 0:
                        cur = db.cursor()
                        sql = "UPDATE player SET locationID=213"
                        cur.execute(sql)
                        sql = "commit"
                        cur.execute(sql)
                        print("You move North" +"\n"+ "...")
                        time.sleep(1)
                        chapter2()
                    else:
                        print("You don't want to go there")
                cur.close()
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=211"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=209"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
            else:
                errorMovement()
        elif row == 213:
            x = input("Move to: South" +"\n"+ "> ")
            if x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=212"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
            else:
                errorMovement()

        #floor3
        elif row == 301:
            x = input("Move to: East" +"\n"+ "> ")
            if x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=304"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            else:
                errorMovement()
        elif row == 302:
            x = input("Move to: East" +"\n"+ "> ")
            if x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=306"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            else:
                errorMovement()
        elif row == 303:
            x = input("Move to: North - Down" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=304"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x=="down" or x=="Down":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=107"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move down the stairs")
                cur.close()
            else:
                errorMovement()
        elif row == 304:
            x = input("Move to: North/West/East/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=305"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=308"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=303"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=301"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        elif row == 305:
            x = input("Move to: North/West/East/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=306"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=309"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=304"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            else:
                errorMovement()
        elif row == 306:
            x = input("Move to: North/West/East/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=307"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=310"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=305"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=302"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        elif row == 307:
            x = input("Move to: South - Down" +"\n"+ "> ")
            if x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=306"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
                cur.close()
            elif x=="down" or x=="Down":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=207"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move down the stairs")
                cur.close()
            else:
                errorMovement()
        elif row == 308:
            x = input("Move to: West" +"\n"+ "> ")
            if x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=304"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        elif row == 309:
            x = input("Move to: West/East" +"\n"+ "> ")
            if x == "East" or x=="east" or x=="E" or x=="e":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=311"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move East")
                cur.close()
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=305"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
                cur.close()
            else:
                errorMovement()
        elif row == 310:
            x = input("Move to: North" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=311"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            else:
                errorMovement()
        elif row == 311:
            x = input("Move to: North/West/South" +"\n"+ "> ")
            if x == "North" or x=="north" or x=="N" or x=="n":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=312"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move North")
                cur.close()
            elif x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=310"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
            elif x == "West" or x=="west" or x=="W" or x=="w":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=309"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move West")
            else:
                errorMovement()
        elif row == 312:
            x = input("Move to: South" +"\n"+ "> ")
            if x == "South" or x=="south" or x=="S" or x=="s":
                cur = db.cursor()
                sql = "UPDATE player SET locationID=311"
                cur.execute(sql)
                sql = "commit"
                cur.execute(sql)
                print("You move South")
            else:
                errorMovement()
    return

#Aliohjelma, joka muuttaa eastOpen arvon auki sillan ja linnanpihan välissä
def openBossOfficeDoor():
     cur = db.cursor()
     sql = "update map set eastOpen = 1 where curRoom = 38;"
     cur.execute(sql)
     print("You hear The door to your boss's office ")

def lookTiletypeName():
    cur = db.cursor()
    sql = "select tiletype.name from tiletype left outer join tile on tile.tiletypeID=tiletype.tiletypeID left outer join player on player.locationID=tile.locationID where player.locationID=tile.locationID"
    cur.execute(sql)
    result = cur.fetchone()
    for row in result:
        #development and testing purposes
        print(row)
    cur.close()
    return

def take():
    x=input("What to take?" +"\n"+ "> ")
    if x=="morphine bottle" or x=="bottle":
        take_morphinebottle()
    else:
        print("Item is not available")
    return

def take_morphinebottle():
    cur = db.cursor()
    sql = "SELECT locationID from player"
    cur.execute(sql)
    result =  cur.fetchone()
    cur.execute(sql)
    for row in result:
        #print(row)
        if row == 208:
            sql = "UPDATE object SET locationID=null, playerID=1 WHERE objecttypeID=3"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You pick up the morphine bottle.")
        else:
            errorTake()
        cur.close()
    return

def look():
    lookTiletypeName()

    #tiletype description
    cur = db.cursor()
    sql = "select tiletype.description from tiletype left outer join tile on tile.tiletypeID=tiletype.tiletypeID left outer join player on player.locationID=tile.locationID where player.locationID=tile.locationID"
    cur.execute(sql)
    result = cur.fetchone()
    cur.execute(sql)
    for row in result:
        print(row)
    cur.close()

    #tile specific directions
    cur = db.cursor()
    sql = "select tile.roominfo from tiletype left outer join tile on tile.tiletypeID=tiletype.tiletypeID left outer join player on player.locationID=tile.locationID where player.locationID=tile.locationID"
    cur.execute(sql)
    result = cur.fetchone()
    cur.execute(sql)
    for row in result:
        print(row)
    cur.close

    #shows locationID as well for development purposes
    cur = db.cursor()
    sql = "select locationID from player"
    cur.execute(sql)
    result = cur.fetchone()
    for row in result:
        print(row)
    cur.close()

def inventory():
    cur = db.cursor()
    sql = "SELECT name FROM object LEFT OUTER JOIN objecttype ON object.objecttypeID = objecttype.objecttypeID WHERE playerID = 1"
    cur.execute(sql)
    result = cur.fetchall()
    if cur.rowcount>=1:
        print ("Inventory:")
        cur.execute(sql)
        for row in result:
            print(row)
    else:
        print("You are not carrying anything")
    cur.close()
    return

def x_scissors():
    cur = db.cursor()
    sql = "select description from objecttype where objecttypeID = 1"
    cur.execute(sql)
    result = cur.fetchall()
    print ("Description:")
    cur.execute(sql)
    for row in result:
        print(row)
    cur.close()
    return

def x_giantrat():
    cur = db.cursor()
    sql = "select description from enemytype where enemytypeID = 2"
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    return

def x_boss():
    cur = db.cursor()
    sql = "select description from enemytype where enemytypeID = 1"
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    return
    return

def x_patients():
    print("Drooling, screaming and bleeding. Where’s the morphine when you need it?")
    return

def x_self():
    cur = db.cursor()
    sql = "select description from player"
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    return

def useMap1():
    print("                stairs                   1st Floor")
    print("              +-------+                  PR = Patient Room")
    print("              | |---| |                  CR = Cleaning Room")
    print("              | |---| |")
    print("       +------+  107  +------+")
    print("       |          UP         |         +-------+-------+")
    print("+------+                     |+------+ |               |")
    print("|      |                     /Toilet | |     Patient   |")
    print("|  PR  /         106         /  110  | |      Room     |")
    print("| 102  /                     |+------+ |       113     |")
    print("|      |                     |+--------+--//---+--//---+------+")
    print("+------+                                                      |+------+")
    print("       |                                                      /       |")
    print("Door   /                                                      /       |")
    print("Main   /         105 Hallway     109           112            |+------+")
    print("       /                                                      /       |")
    print("       |                                                      /       |")
    print("+------+                                                      |+------+")
    print("|      |                      +--------+--//---+---//--+------+")
    print("|  PR  /                      |+-----+ |               |")
    print("| 101  /         104          /  CR  | |     Patient   |")
    print("|      |                      /  108 | |      Room     |")
    print("+------+                      |+-----+ |       111     |")
    print("       |        (UP)          |        +-------+-------+")
    print("       +------+  103  +------+")
    print("              | |---| |")
    print("              | |---| |")
    print("              +-------+")
    print("                stairs")
    return

def useMap2():
    print("                stairs                   1st Floor")
    print("              +-------+                  PR = Patient Room")
    print("              | |---| |                  CR = Cleaning Room")
    print("              | |---| |")
    print("       +------+  207  +------+")
    print("       |          UP         |         +-------+-------+")
    print("+------+                     |+------+ |               |")
    print("|      |                     /Toilet | |    Delivery   |")
    print("|  PR  /         206         /  210  | |      Room     |")
    print("| 202  /                     |+------+ |       213     |")
    print("|      |                     |+--------+--//---+--//---+------+")
    print("+------+                                                      |+------+")
    print("       |			      			         /       |")
    print("Door   /                                                      /       |")
    print("Main   /         105 Hallway     209           212            |+------+")
    print("       /                                                      /       |")
    print("       |                                                      /       |")
    print("+------+                                                      |+------+")
    print("|      |                      +--------+--//---+---//--+------+")
    print("|  PR  /                      |+-----+ |               |")
    print("| 201  /         204          /  MR  | |     Patient   |")
    print("|      |                      /  208 | |      Room     |")
    print("+------+                      |+-----+ |       211     |")
    print("       |        (UP)          |        +-------+-------+")
    print("       +------+  203  +------+")
    print("              | |---| |")
    print("              | |---| |")
    print("              +-------+")
    print("                stairs")
    return

def useMap3():
    print("                stairs                   1st Floor")
    print("              +-------+                  PR = Patient Room")
    print("              | |---| |                  CR = Cleaning Room")
    print("              | |---| |")
    print("       +------+  307  +------+")
    print("       |          UP         | +-------+-------------+-------+")
    print("+------+                     | |                             |")
    print("|      |                     | |            Boss             |")
    print("|  PR  /         306         | |            Room             |")
    print("| 302  /                     | |             312             |")
    print("|      |                     |+--------+--///--+--///--+------+")
    print("+------+                                                      |+------+")
    print("       |			      			         /       |")
    print("       /                                                      /       |")
    print("       /         305 Hallway     309           311            |+------+")
    print("       /                                                      /       |")
    print("       |                                                      /       |")
    print("+------+                                                      |+------+")
    print("|      |                      +--------+--//---+---//--+------+")
    print("|  PR  /                      |+-----+ |               |")
    print("| 301  /         304          /  CR  | |     Patient   |")
    print("|      |                      /  308 | |      Room     |")
    print("+------+                      |+-----+ |       310     |")
    print("       |        (UP)          |        +-------+-------+")
    print("       +------+  303  +------+")
    print("              | |---| |")
    print("              | |---| |")
    print("              +-------+")
    print("                stairs")
    return


#for row in data:
    #print (row[0],row[1],row[2],row[3])


#for row in cur.fetchall():
    #print row[0]

def print_pause(lines):
    for line, pause in lines:
        print(line)
        time.sleep(pause)

def save():
    return

#parser
def commands():
    mapFlip="1"
    x = input("> ")

    if x == "help":
        print("help, info, look, inventory, use, inspect, move, quit")

    #info
    elif x == "info":
        print("Follow this command with another command for more information")
    elif x == "info help":
        print("type 'help' for list of commands")
    elif x == "info info":
        print("Some water bound turtles can reach upwards of 100 years of age")
    elif x == "info look":
        print("'look(l)': use to look around")
    elif x == "info inventory":
        print("'inventory(i)': lists all items in your inventory")
    elif x== "info use":
        print("'use(u)': use to interact with the world")
    elif x == "info inspect":
        print("'inspect(x)': use to gain information about items, people and pretty much anything you please")
    elif x == "info move":
        print("'move (m)': use to move to another room or area")
    elif x == "info quit":
        print("'quit'/'exit': quit the game")

    #move - really works now!
    elif x=="move" or x=="m":
        move()
    elif x=="n" or x=="north" or x=="North" or x=="N":
        moveNorth()
    elif x=="e" or x=="east" or x=="East" or x=="E":
        moveEast()
    elif x=="s" or x=="south" or x=="South" or x=="S":
        moveSouth()
    elif x=="w" or x=="west" or x=="West" or x=="W":
        moveWest()

    #staircase up
    elif x=="up" or x=="Up" or x=="u" or x=="U":
        cur = db.cursor()
        sql = "select locationID from player"
        cur.execute(sql)
        result = cur.fetchone()
        cur.execute(sql)
        for row in result:
            print(row)
        cur.close
        if row == 103:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=203"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move up the stairs")
            cur.close()
        elif row == 203:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=303"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move up the stairs")
            cur.close()
        elif row == 107:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=207"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move up the stairs")
            cur.close()
        elif row == 207:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=307"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move up the stairs")
            cur.close()
        else:
            errorMovement()
            
    #staircase down
    elif x=="down" or x=="Down" or x=="d" or x=="D":
        cur = db.cursor()
        sql = "select locationID from player"
        cur.execute(sql)
        result = cur.fetchone()
        cur.execute(sql)
        for row in result:
            print(row)
        cur.close
        if row == 203:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=103"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move down the stairs")
            cur.close()
        elif row == 303:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=203"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move down the stairs")
            cur.close()
        elif row == 207:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=107"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move down the stairs")
            cur.close()
        elif row == 307:
            cur = db.cursor()
            sql = "UPDATE player SET locationID=207"
            cur.execute(sql)
            sql = "commit"
            cur.execute(sql)
            print("You move down the stairs")
            cur.close()
        else:
            errorMovement()

    #work in progress
    elif x == "look" or x=="l":
        look()

    elif x == "inspect" or x=="x":
        #import mysql data
        x = input("Options: (1) scissors, (2) self, (3) patients, (4) boss, (5) giantrat" + "\n" + "> ")
        if  x == "1" or x=="scissors":
            x_scissors()
        elif x == "2" or x=="self":
            x_self()
        elif x == "3" or x=="patients":
            x_patients()
        elif x == "4" or x=="boss":
            x_boss()
        elif x == "5" or x=="giantrat":
            x_giantrat()
        else:
            print("ERROR: Inspectable item/person not found")
            
    elif x=="x scissors" or x=="inspect scissors":
        x_scissors()
    elif x=="x self" or x=="inspect self":
        x_self()
    elif x=="x patients" or x=="inspect patients":
        x_patients()
    elif x=="x boss" or x=="inspect boss" or x=="x Clarissa" or x=="x clarissa":
        x_boss()
    elif x=="x map" or x=="inspect map":
        x_map()
    elif x=="x giantrat" or x=="inspect giantrat":
        x_giantrat()

    elif x=="take":
        take()

    elif x=="take morphile bottle" or x=="take bottle":
        take_morphinebottle()  

    elif x == "use":
        #import mysql data
        x = int(input("What to use?" + "\n" + "inventory from mysql" + "\n" + "> "))
        if  x == 1:
            x_scissors()
        elif x == 2:
            x_self()
        elif x == 3:
            x_patients()
        else:
            print("Try again and choose a number")

    elif x=="inventory" or x=="i":
        inventory()

    #testing purposes
    elif x=="rat test":
        ratSequence()

#for testing purposes
    elif x=="map1":
        useMap1()
    elif x=="map2":
        useMap2()
    elif x=="map3":
        useMap3()
        
    elif x=="map" or x=="use map" or x=="map use":
        #if mapFlip=="1":
            #useMap1()
            #print("Map1")
        #elif mapFlip=="2":
            #useMap2()
            #print("Map2")
        #print("The map can be flipped")
        useMap1()
        
    elif x=="flip map" or x=="map flip":
        print("Map flipped")
        if mapFlip=="1":
            mapFlip="2"
        elif mapFlip=="2":
            mapFlip="1"

    #elif x=="pokemon music":
    #    os.system("start C:\Users\thebu\Desktop\Sage-femme pronto\files\pokemon music.mp3")

    elif x=="quit" or x=="exit":
        leave()

    elif x=="restart":
        print("Restarting game...")
        db.rollback()
        chapter1()

    else:
        print("Command not understood; check spelling or type 'help'")
