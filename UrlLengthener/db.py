import psycopg2
import config
from . import randomURL

def connect():
    try:
        return psycopg2.connect("dbname='UrlLongTest' host='localhost' user='postgres' password=%s" % config.DEV_DB_PW)
    except:
        return 'Cannot connect to Database'
    

def getNewUrl(destination):
    generated = randomURL.generate()
    conn = connect()
    if conn == 'Cannot connect to Database':
        return conn
    else:
        cur = conn.cursor()
        cur.execute("INSERT INTO urls (generated_url, destination_url) VALUES ('%s', '%s');" % (generated, destination))
        conn.commit()
        cur.close()
        conn.close()

def getRowByDestination(destination_url):
    conn = connect()
    if conn == 'Cannot connect to Database':
        return conn
    else:
        cur = conn.cursor()
        cur.execute("SELECT generated_url, destination_url FROM urls WHERE destination_url = '%s';" % destination_url)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

def getRowByGenerated(generated_url):
    conn = connect()
    if conn == 'Cannot connect to Database':
        return conn
    else:
        cur = conn.cursor()
        cur.execute("SELECT destination_url, generated_url FROM urls WHERE generated_url = '%s';" % generated_url)
        rows = cur.fetchall()
        cur.close()
        conn.close()

        if(len(rows) > 0):
            return rows
        else:
            return 'URL not found'
