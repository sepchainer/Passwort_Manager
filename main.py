import sqlite3
import getpass
import os
import database
import menu
import encrypt


print("---Passwort Manager---")

user = str(getpass.getuser())
encrypted_path = "C:\\Users\\" + user + r"\OneDrive\Dokumente\Python\Passwort-Manager\encrypted!pw_manager.db"
decrypted_path = "C:\\Users\\" + user + r"\OneDrive\Dokumente\Python\Passwort-Manager\pw_manager.db"

if os.path.isfile(encrypted_path):
    try:
        master_pw = input("Master Passwort: ")
        encrypt.decrypt(encrypt.get_key(master_pw), encrypted_path)  # Database gets decrypted
        database.test_database_decrypt_correct()  # tests if database was decrypted correctly
        print("Richitg")
        menu.menu()  # opens up the menu
        encrypt.encrypt(encrypt.get_key(master_pw), decrypted_path)  # encrypts Database again
        os.remove(decrypted_path)
    except sqlite3.DatabaseError:  # catches Error if Password was wrong and Database was decrypted wrong
        print("Das Passwort ist falsch")

else:
    master_pw = input("Geben Sie ein Masterpasswort ein: ")
    print("\nSie haben erfolgreich ein Passwort gesetzt! Merken Sie sich dieses gut!")
    print("Ohne dieses Passwort haben Sie keinen Zugriff auf ihre Daten!\n")
    database.create_database()
    menu.menu()
    encrypt.encrypt(encrypt.get_key(master_pw), decrypted_path)
    os.remove(decrypted_path)