from models.note_model import Note_model
from presenters.model import Model
from presenters.presenter import Presenter
from presenters.view import View
from views.console_view import Console_view


if __name__ == "__main__":
    model: Model = Note_model()
    view: View = Console_view()
    presenter: Presenter = Presenter(model=model, view=view)

    presenter.start()
