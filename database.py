import sqlite3


def create_database():
    conn = sqlite3.connect("pw_manager.db")
    #create cursor
    c = conn.cursor()
    # Create Database
    c.execute("""CREATE TABLE IF NOT EXISTS pw_manager(
        distro_name text,
        username text,
        password text
        )""")
    # commit out command
    conn.commit()
    # close connection
    conn.close()


def test_database_decrypt_correct():
    conn = sqlite3.connect("pw_manager.db")
    #create cursor
    c = conn.cursor()
    c.execute("SELECT * FROM pw_manager")
    items = c.fetchall()
    # commit out command
    conn.commit()
    # close connection
    conn.close()


def show_all():
    conn = sqlite3.connect("pw_manager.db")
    #create cursor
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM pw_manager")
    items = c.fetchall()
    for i in items:
        print(i)

    # commit out command
    conn.commit()
    # close connection
    conn.close()


def insert_new_account(site, name, pw):
    conn = sqlite3.connect("pw_manager.db")
    #create cursor
    c = conn.cursor()
    item = [site, name, pw]
    c.execute("INSERT INTO pw_manager VALUES (?,?,?)", item)
    # commit out command
    conn.commit()
    # close connection
    conn.close()


def delete_account(site):
    conn = sqlite3.connect("pw_manager.db")
    # create cursor
    c = conn.cursor()
    c.execute("DELETE from pw_manager WHERE distro_name=?", (site,))
    # commit out command
    conn.commit()
    # close connection
    conn.close()


def show_pw(site):
    conn = sqlite3.connect("pw_manager.db")
    #create cursor
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM pw_manager")
    items = c.fetchall()
    found = False
    for i in items:
        if site == i[1]:
            print("\n Passwort zu " + i[1] + ": " + i[3])
            found = True

    # commit out command
    conn.commit()
    # close connection
    conn.close()
    return found


def show_distro_names():
    conn = sqlite3.connect("pw_manager.db")
    #create cursor
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM pw_manager")
    items = c.fetchall()
    print("\n\t")
    for i in items:
        print(i[0], i[1])

    # commit out command
    conn.commit()
    # close connection
    conn.close()
