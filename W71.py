import sqlite3
#inport the library we're going to use to talk to the SQL database


#we're going to use a database in this application
#and we're going to store that database in the file emaildb.sqllite
conn = sqlite3.connect('HiteshDatabase.sqlite')
cur = conn.cursor()
#this cursor variable now has the cursor object in it

cur.execute('''
DROP TABLE IF EXISTS Counts''')
#we have the cursor object and we call the execute method

#original code:
#cur.execute('''
#CREATE TABLE Counts (email TEXT, count INTEGER)''')

#code for assignment:
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#convert txt into table
fname = input('Enter file name: ')#file name
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:#for lien in file handler
    if not line.startswith('From: ') : continue
    pieces = line.split('@')
    #email = pieces[1]#1 means what happens after the @
    org = pieces[1]
    org = org.rstrip() #remove blank spaces
    #print email
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    #?means this is going to be somthing
    #(email,)is a tuple, and the 1st thing in the tuple is what will be substituted
    #for the question mark

    try:
        count = cur.fetchone()[0] #get current count
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
            (org, ))
    except:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )

    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()