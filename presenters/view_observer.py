from abc import ABC, abstractmethod


class View_observer(ABC):
    @abstractmethod
    def show_all_notes():
        pass
