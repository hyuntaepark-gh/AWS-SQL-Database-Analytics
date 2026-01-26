#!/usr/bin/env python3

import cgi
import mysql.connector

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
ticker = form.getvalue("ticker")
start_date = form.getvalue("start_date")
end_date = form.getvalue("end_date")

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
    WHERE ticker = %s AND date BETWEEN %s AND %s
"""
cursor.execute(query, (ticker, start_date, end_date))
rows = cursor.fetchall()

print("<h2>Query Results</h2>")
print("<table border='1'>")
print("<tr><th>Ticker</th><th>Date</th><th>Close</th><th>Exchange</th></tr>")

for r in rows:
    print(f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>")

print("</table>")

cursor.close()
conn.close()
