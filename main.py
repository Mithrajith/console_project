from vault_manager import VaultManager
from entries import NoteEntry, PasswordEntry
#print("Welcome to the Vault Manager!")
vault = VaultManager()

while True:
    cmd = input("Vault > ").strip().lower()

    if cmd.startswith("add note"):
        title = input("Title: ")
        content = input("Content: ")
        vault.add_entry(NoteEntry(title, content))

    elif cmd.startswith("add password"):
        title = input("Service: ")
        username = input("Username: ")
        password = input("Password: ")
        vault.add_entry(PasswordEntry(title, username, password))

    elif cmd.startswith("list notes"):
        notes = vault.get_notes()
        if not notes:
            print("No notes found.")
        else:
            print("Notes:")
            for note in notes:
                print(f"- {note.title}")

    elif cmd.startswith("list service"):
        parts = cmd.split()
        if len(parts) == 2:
            # List all services
            services = vault.get_passwords()
            if not services:
                print("No passwords found.")
            else:
                print("Services:")
                for pw in services:
                    print(f"- {pw.title}")
        elif len(parts) == 3:
            # List username/password for a specific service
            service_name = parts[2]
            pw = vault.get_password_by_service(service_name)
            if pw:
                print(f"Service: {pw.title}\nUsername: {pw.username}\nPassword: {pw.password}")
            else:
                print("Service not found.")

    elif cmd.startswith("list "):
        # List note content by title
        parts = cmd.split()
        if len(parts) == 2:
            note_title = parts[1]
            note = vault.get_note_by_title(note_title)
            if note:
                print(f"Title: {note.title}\nContent: {note.content}")
            else:
                print("Note not found.")

    elif cmd.startswith("del note"):
        parts = cmd.split(maxsplit=2)
        if len(parts) == 3:
            title = parts[2]
            if vault.delete_note_by_title(title):
                print("Note deleted.")
            else:
                print("Note not found.")
        else:
            print("Usage: del note <title>")

    elif cmd.startswith("del password"):
        parts = cmd.split(maxsplit=2)
        if len(parts) == 3:
            service = parts[2]
            if vault.delete_password_by_service(service):
                print("Password deleted.")
            else:
                print("Service not found.")
        else:
            print("Usage: del password <service>")

    elif cmd.startswith("exit"):
        break

    else:
        print("Unknown command.")
