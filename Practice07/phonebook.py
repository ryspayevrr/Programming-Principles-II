from connect import get_connection
import csv

# 1. Create table
def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            name VARCHAR(100),
            phone VARCHAR(20)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


# 2. Insert from CSV
def insert_from_csv():
    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row["name"], row["phone"])
            )

    conn.commit()
    cur.close()
    conn.close()


# 3. Insert from user
def insert_user():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


# 4. Show all contacts
def show_all():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# 5. Update phone
def update_phone():
    name = input("Name: ")
    new_phone = input("New phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE name=%s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()


# 6. Delete contact
def delete_contact():
    name = input("Name to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE name=%s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()



create_table()


insert_from_csv()
insert_user()
show_all()
update_phone()
delete_contact()