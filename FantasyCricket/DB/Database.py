import sqlite3

def connectDB(db):
    CricketDB = sqlite3.connect(db)
    dbCursor =CricketDB.cursor()
    return dbCursor

def selectPlayers(category,db):
    print('selectplayers')
    playerlist=[]
    try:
        cursor=connectDB(db)
        cursor.execute('Select * from stats where ctg ="'+str(category)+'"')
        record=cursor.fetchall()
        for i in record:
            print(i[0])
            playerlist.append(i[0])

    except:
            print("some problem in DB")
    return playerlist
#selectPlayers('BAT')
    
