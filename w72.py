import sqlite3
import xml.etree.ElementTree as ET
conn = sqlite3.connect('Tracksxm.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;''')
#如果存在就先删除表
# 执行多条查询需要 executescript
cur.executescript('''CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')  # 执行多行时注意使用三个引号
file_name = 'Library.xml'
fh = open(file_name)
tree = ET.fromstring(fh.read())
dicts = tree.findall('./dict/dict/dict')
# 查看xml文件，分析目录树结构 需要在/dict/dict/dict内查找字段
# 定义查找函数
def lookup(pare, aim):
    flag = False
    for child in pare:
        if flag:
            return child.text
        if child.tag == 'key' and child.text == aim:
            flag = True
    return None
# 通过构建的数据库情况，需要查找的字段为
# Track ID   Name    Artist     Album   Play Count  Rating  Total Time
for entry in dicts:
    if(lookup(entry, 'Track ID') is None):  continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')
    if name is None or artist is None or album is None or genre is None:
        continue
    print(name, artist, album, count, rating, length)
    # 根据建立数据库的顺序进行插入，并获取外键对应的id值
    # 注意对于唯一元素插入时使用ignore
    cur.execute('''INSERT OR IGNORE INTO Artist(name) VALUES(?)''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]   # 查询返回的是数组
    cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES(?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Album(artist_id, title) VALUES(?, ?)',(artist_id, album))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]
    # 至于这里为什么要用replace原因不知
    cur.execute('''INSERT OR REPLACE INTO Track(title, album_id, genre_id, len, rating, count) 
    VALUES(?, ?, ?, ?, ?, ?)''',(name, album_id, genre_id, length, rating, count))
conn.commit()
cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')
res = cur.fetchall()
for line in res:
    print(line)
cur.close()