import os
import json


def print_with_indent(value, indent=0):
    print("\t" * indent, str(value), sep="")


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    @classmethod
    def from_json(cls, value):
        new_entry = cls(value["title"])
        for item in value.get("entries", []):
            new_entry.add_entry(cls.from_json(item))
        return new_entry

    def add_entry(self, entry):
        entry.parent = self
        self.entries.append(entry)

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def json(self):
        d = dict()
        d["title"] = self.title
        d["entries"] = list()
        for entry in self.entries:
            if isinstance(entry, Entry):
                d['entries'].append(entry.json())
        return d

    def save(self, path):
        folder = os.path.join(path, f"{self.title}.json")
        with open(folder, "w", encoding="utf-8") as file:
            json.dump(self.json(), file)

    @classmethod
    def load(cls, filename):
        with open(filename, "r", encoding="utf-8") as file:
            content = json.load(file)
        return cls.from_json(content)


if __name__ == '__main__':
    new = Entry("Продукты")
    new.print_entries()
    new_new = Entry("Колбасы", [Entry("Таллинская"), Entry("Брауншвейская")])
    new.add_entry(new_new)
    new.save("tmp")
    entr = Entry.load("tmp/Продукты.json")
    print(entr.print_entries())




