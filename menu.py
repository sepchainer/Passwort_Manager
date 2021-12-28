import string
import secrets
import database


def generate_pw(num):
    passwort = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(num))
    return passwort


def menu():
    choice = ''
    while choice != 'q':
        print("\n[1] Neues Konto + eigenes Passwort hinzufuegen")
        print("[2] Neues Konto + generiertes Passwort hinzufuegen")
        print("[3] Konto entfernen")
        print("[4] Passwort zu bestimmten Konto anzeigen")
        print("[q] Beenden")

        choice = input("Was wollen Sie machen? ")
        if choice == '1':
            print("\nGeben Sie ihre Daten ein!")
            distro_name = input("Name der Distribution: ")
            username = input("Username oder Email: ")
            password = input("Eigenes Passwort: ")
            database.insert_new_account(distro_name, username, password)

        if choice == '2':
            print("\nGeben Sie ihre Daten ein!")
            distro_name = input("Name der Distribution: ")
            username = input("Username oder Email: ")
            eingabe = int(input("Wie lang soll das Passwort sein? "))
            password = generate_pw(eingabe)
            database.insert_new_account(distro_name, username, password)
            print("Ihr generiertes Passwort: " + password)

        if choice == '3':
            delete = input("\nWelches Konto möchten Sie entfernen? ")
            database.delete_account(delete)

        if choice == '4':
            pw_needed = input("\nZu welchem Konto benötigen Sie das Passwort? ")
            found = database.show_pw(pw_needed)
            if not found:
                show = input("Wollen Sie sich ihre Konten anzeigen lassen, um den richtigen Namen zu finden?(j/n) ")
                if show == 'j':
                    database.show_distro_names()