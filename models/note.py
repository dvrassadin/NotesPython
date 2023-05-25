from datetime import datetime


class Note():
    def __init__(self, id: int, date: datetime, title: str, body: str) -> None:
        self.id = id
        self.date = date
        self.title = title
        self.body = body


    def __str__(self) -> str:
        return f"{self.id}\t{self.date}\n{self.title}\n{self.body}\n"
