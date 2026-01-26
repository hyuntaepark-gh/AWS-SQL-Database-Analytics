#!/usr/bin/env python3

import cgi
import mysql.connector

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
date_value = form.getvalue("date")
close_value = form.getvalue("close")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bdmhyuntae",
    database="homework2"
)
cursor = conn.cursor()

query = """
    SELECT ticker, date, close, exchange
    FROM price
    WHERE date = %s AND close <= %s
"""
cursor.execute(query, (date_value, close_value))
rows = cursor.fetchall()

print("<h2>Price Query Results</h2>")
print("<table border='1'>")
print("<tr><th>Ticker</th><th>Date</th><th>Close</th><th>Exchange</th></tr>")

for r in rows:
    print(f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>")

print("</table>")

cursor.close()
conn.close()
