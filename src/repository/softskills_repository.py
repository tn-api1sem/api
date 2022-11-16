from  src.repository.context.api_context import ApiContext

class SoftSkillsRepository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get_all(self):
        return self._apiContext.softSkills_table.get_all()
