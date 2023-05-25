from abc import ABC, abstractmethod


class View_observer(ABC):
    @abstractmethod
    def on_show_all_notes(self):
        pass

    @abstractmethod
    def on_add_note(self):
        pass

    @abstractmethod
    def on_edit_note(self):
        pass

    @abstractmethod
    def on_delete_note(self):
        pass

    @abstractmethod
    def on_find_by_date(self):
        pass