from src.repository.softskills_repository import SoftSkillsRepository


class SoftSkillsService(object):
    _repository = SoftSkillsRepository()

    def __init__(self) -> None:
        pass

    def get_all(self):
        return self._repository.get_all();

