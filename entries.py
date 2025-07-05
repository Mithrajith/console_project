
from datetime import datetime

class VaultEntry:
    def __init__(self, title, tags=[]):
        self.title = title
        self.tags = tags
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "title": self.title,
            "tags": self.tags,
            "created_at": self.created_at.isoformat()  # 👈 FIX HERE
        }

class NoteEntry(VaultEntry):
    def __init__(self, title, content, tags=[]):
        super().__init__(title, tags)
        self.content = content

    def to_dict(self):
        data = super().to_dict()
        data["content"] = self.content
        return data



class PasswordEntry(VaultEntry):
    def __init__(self, title, username, password, tags=[]):
        super().__init__(title, tags)
        self.username = username
        self.password = password

# Similarly add: BankEntry, TaskEntry
