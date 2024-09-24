from typing import List
from resources import Entry
import os


class EntryManager:
    def __init__(self, data_path):
        self.data_path = data_path
        self.entries = list()

    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)

    def load(self):
        for file in os.listdir(self.data_path):
            if file.endswith(".json"):
                entry = Entry.load(os.path.join(self.data_path, file))
                self.entries.append(entry)

    def add_entry(self, title: str):
        entry = Entry(title)
        self.entries.append(entry)

if __name__ == '__main__':
    entry_manager = EntryManager("tmp")
    entry_manager.load()
    print(entry_manager.entries)