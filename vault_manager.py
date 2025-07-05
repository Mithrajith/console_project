import json
from encryptor import Encryptor
from entries import NoteEntry, PasswordEntry
import os


class VaultManager:
    def __init__(self, vault_file='data/vault.enc'):
        self.vault_file = vault_file
        self.encryptor = Encryptor()
        self.entries = []
        os.makedirs(os.path.dirname(self.vault_file), exist_ok=True)
        self.load()

    def add_entry(self, entry):
        self.entries.append(entry)
        self.save()

    def save(self):
        raw = json.dumps([e.to_dict() for e in self.entries]).encode()
        encrypted = self.encryptor.encrypt(raw)
        with open(self.vault_file, 'wb') as f:
            f.write(encrypted)

    def load(self):
        try:
            with open(self.vault_file, 'rb') as f:
                decrypted = self.encryptor.decrypt(f.read())
                raw_entries = json.loads(decrypted)

                self.entries = []
                for e in raw_entries:
                    if e['type'] == 'NoteEntry':
                        self.entries.append(NoteEntry(
                            title=e['title'],
                            content=e['content'],
                            tags=e.get('tags', [])
                        ))
                    elif e['type'] == 'PasswordEntry':
                        self.entries.append(PasswordEntry(
                            title=e['title'],
                            username=e['username'],
                            password=e['password'],
                            tags=e.get('tags', [])
                        ))
                    else:
                        print(f"⚠️ Unknown type: {e['type']} — skipping")
        except FileNotFoundError:
            self.entries = []
        except Exception as e:
            print(f"⚠️ Decryption failed or corrupted file: {e}")
            self.entries = []

    def list_entries(self, type_filter=None):
        for e in self.entries:
            if not type_filter or e.get("type") == type_filter:
                print(e)

    def get_notes(self):
        return [e for e in self.entries if type(e).__name__ == 'NoteEntry']

    def get_passwords(self):
        return [e for e in self.entries if type(e).__name__ == 'PasswordEntry']

    def get_note_by_title(self, title):
        for e in self.entries:
            if type(e).__name__ == 'NoteEntry' and e.title.lower() == title.lower():
                return e
        return None

    def get_password_by_service(self, service):
        for e in self.entries:
            if type(e).__name__ == 'PasswordEntry' and e.title.lower() == service.lower():
                return e
        return None

    def delete_note_by_title(self, title):
        for i, e in enumerate(self.entries):
            if type(e).__name__ == 'NoteEntry' and e.title.lower() == title.lower():
                del self.entries[i]
                self.save()
                return True
        return False

    def delete_password_by_service(self, service):
        for i, e in enumerate(self.entries):
            if type(e).__name__ == 'PasswordEntry' and e.title.lower() == service.lower():
                del self.entries[i]
                self.save()
                return True
        return False
