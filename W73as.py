import json
import sqlite3
conn = sqlite3.connect('rosterdb.sqlite')

cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);
CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);
CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id))''')

file_name = input('Enter filename: ')
if(len(file_name) < 1):
    file_name = 'roster_data.json'
fh = open(file_name).read()
js = json.loads(fh)
for record in js:
    name = record[0]
    title = record[1]
    role = record[2]
    cur.execute('INSERT OR IGNORE INTO User(name) VALUES(?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Course(title) VALUES(?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]
    cur.execute('INSERT OR REPLACE INTO Member(user_id, course_id, role) VALUES(?,?,?)', (user_id, course_id, role))
cur.execute('''SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 5''')
res = cur.fetchall()
for line in res:
    print(line)
conn.commit()
cur.close()