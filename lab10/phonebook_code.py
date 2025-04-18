import psycopg2
import csv

# connect to csv
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="player"
)
cur = conn.cursor()

# table creating
cur.execute('''
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        phone VARCHAR(15)
    );
''')
conn.commit()

# option menu
print("choose the action:")
print("1 - insert data by hand")
print("2 - insert data from csv")
print("3 - update existing data")
print("4 - search the phonebook")
print("5 - delete someone")

choice = input("your choice: ")

# insert data by hand
if choice == "1":
    username = input("input name: ")
    phone = input("input number: ")
    cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (username, phone))
    print("user added")


# insert data from csv
elif choice == "2":
    csv_path = input("insert way of csv")
    try:
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (row['username'], row['phone']))
        print("data from csv is inserted")
    except FileNotFoundError:
        print("404")

# update someone
elif choice == "3":
    field = input("update name/phone: ").lower()
    if field == "name":
        old_name = input("old name: ")
        new_name = input("new name: ")
        cur.execute("UPDATE PhoneBook SET username = %s WHERE username = %s", (new_name, old_name))
        print("name changed")
    elif field == "phone":
        username = input("whose number need to change: ")
        new_phone = input("new number: ")
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE username = %s", (new_phone, username))
        print("number changed")
    else:
        print("wrong")

# search someone
elif choice == "4":
    how = input("search by name/phone: ").lower()
    if how == "name":
        name = input("enter the name: ")
        cur.execute("SELECT * FROM PhoneBook WHERE username ILIKE %s", ('%' + name + '%',))
    elif how == "phone":
        phone = input("enter the number: ")
        cur.execute("SELECT * FROM PhoneBook WHERE phone LIKE %s", ('%' + phone + '%',))
    else:
        print("wrong")
        cur.close()
        conn.close()
        exit()

    results = cur.fetchall()
    if results:
        print("found these:")
        for row in results:
            print(row)
    else:
        print("nothing found")

# delete someone
elif choice == "5":
    way = input("delete name/phone: ").lower()
    if way == "name":
        name = input("who to delete: ")
        cur.execute("DELETE FROM PhoneBook WHERE username = %s", (name,))
        print("done")
    elif way == "phone":
        phone = input("which number to delete: ")
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
        print("done")
    else:
        print("wrong")


else:
    print("wrong choice")

conn.commit()
cur.close()
conn.close()