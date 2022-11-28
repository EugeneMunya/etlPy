import psycopg2

connect = psycopg2.connect(
    host="localhost",
    database='mydb',
    user='myuser',
    password='mypass',
    port='5432'
)
if __name__ == '__main__':
    print(connect)
