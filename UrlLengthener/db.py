import psycopg2
import config
from . import randomURL

def connect():
    return psycopg2.connect("dbname='UrlLongTest' host='localhost' user='postgres' password=%s" % config.DEV_DB_PW)

def getNewUrl(destination):
    generated = randomURL.generate()
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO urls (generated_url, destination_url) VALUES ('%s', '%s');" % (generated, destination))
    conn.commit()
    cur.close()
    conn.close()

def getRowByDestination(destination_url):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT generated_url, destination_url FROM urls WHERE destination_url = '%s';" % destination_url)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def getRowByGenerated(generated_url):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT destination_url, generated_url FROM urls WHERE generated_url = '%s';" % generated_url)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows