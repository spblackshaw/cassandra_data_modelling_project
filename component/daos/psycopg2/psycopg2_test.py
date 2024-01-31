import psycopg2

conn = psycopg2.connect(database="udacity", user="simonblackshaw", password="Amanda@1", host="localhost", port=5432)
cur = conn.cursor()
test = cur.execute("SELECT * FROM information_schema.tables WHERE table_schema = 'udacity'")
# SELECT * FROM information_schema.schemata;
print("here")
# row = cur.fetchone()
# while row:
#    print(row)
#    row = cur".fetchone()