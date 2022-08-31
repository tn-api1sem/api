from src.data.context.api_context import ApiContext


class UserRepository:
    _context = {};

    def __init__(self) -> None:
        self._context = ApiContext("user.json")
        pass

    def get_all(self):
        return self._context.get_all()
