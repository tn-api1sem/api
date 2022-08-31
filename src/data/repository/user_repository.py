from src.data.context.api_context import ApiContext


class UserRepository:
    _context = {};

    def __init__(self) -> None:
        self._context = ApiContext("C:/Users/mcfiebig/source/repos/api/src/data/database/user.json")
        pass

    def get_all(self):
        return self._context.get_all()

    def get(self, id):
        return self._context.get(id)

    def insert(self, user):
        self._context.begin_transaction()
        self._context.insert(user)
        self._context.commit()
