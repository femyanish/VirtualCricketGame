import sqlite3
from sqlite3 import Error


class CricketDB(object):
    
##        ConnectDB = sqlite3.connect('FantasyCricket.db')
##        self.dbCursor = ConnectDB.cursor()
##        print(self.dbCursor)
    def __init__(self,db):
        self.batList=[]
        self.conn = sqlite3.connect(db)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    ##    def connectDB():
    ##        CricketDB = sqlite3.connect('FantasyCricket.db')
    ##        dbCursor =CricketDB.cursor()
    ##        return dbCursor
    def query(self, arg):
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def selectPlayers(self, category):
        try:
                dbmgr = CricketDB("FantasyCricket.db")
                print(category)
                for row in dbmgr.query("Select * from books WHERE Title='"+category+"';"):
                    print(row)
                    self.batList.append(row)
        except sqlite3.Error as e:
            print("databade error")
        except Exception as e:
            print("query error")
        finally:
            if con:
                con.close()
        return self.batList
        
##        print('select players',category)
##        role = str(category)
##        sql= 'Select * from stats where ctg ="' + role + '"'
##        print('sql assigned')
##        self.dbCursor.execute(sql)        
##        print('executed select')
##        record = self.dbCursor.fetchall()
##        print('here')
##        if record != None:
##            print('record not none')
##            self.batList = record
            
        # print(len(record))
        # for i in record:
        #     print(i)
        #     print('\n')

#print(CricketDB().selectPlayers('BAT'))

