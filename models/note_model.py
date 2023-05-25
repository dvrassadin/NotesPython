from datetime import datetime
from typing import List
from models.note import Note
from presenters.model import Model
import json


class Note_model(Model):
    __dateFormat = "%d.%m.%Y %H:%M:%S"
    __path = "notes.json"
    lastID = 0

    def load_data(self) -> List[Note]:
        notes: List[Note] = []

        with open(self.__path, "r", encoding="UTF-8") as file:
            data = json.loads(file.read())
            if "notes" not in data:
                return []
            for note in data["notes"]:
                date = datetime.strptime(note["date"], self.__dateFormat)
                self.lastID += 1
                notes.append(Note(id=self.lastID,
                                  date=date,
                                  title=note["title"],
                                  body=note["body"]))

        return notes

    def save_data(self, notes: List[Note]):
        data = {"notes": []}

        for note in notes:
            data["notes"].append({"id": note.id,
                                  "date": datetime.strftime(note.date, self.__dateFormat),
                                  "title": note.title,
                                  "body": note.body})

        with open(self.__path, "w", encoding="UTF-8") as file:
            json.dump(data,  file, indent=4)

    def add_note(self, notes: List[Note], title: str, body: str):
        self.lastID += 1
        notes.append(
            Note(id=self.lastID, date=datetime.now(), title=title, body=body))
        self.save_data(notes)

    def delete_note(self, notes: List[Note], index):
        if index >= 0 and index < len(notes):
            notes.pop(index)
            self.lastID = index
            for i in range(index, len(notes)):
                self.lastID += 1
                notes[i].id = self.lastID
            self.save_data(notes)
        
