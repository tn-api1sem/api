from .context.api_context import ApiContext

class user_repository(object):
    _apiContext: ApiContext

    def __init__(self) -> None:
        self._apiContext = ApiContext()
        pass

    def get(self):
        return self._apiContext.user_table.get_all()
