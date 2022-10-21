from ..models.profile_model import profile_model
from ..repository.profile_repository import profille_repository


class profile_services(object):
    _profille_repository:profille_repository = profille_repository()
    def __init__(self):
        pass;

    def get_profile(self):
        return self._profille_repository.get()

    def get_profile_by_id(self,id):
        return self._profille_repository.find(id)

    def create(self, model: profile_model):
        self._validate(model)
        return self._profile_repository.create(model)

    def update(self, model: profile_model):
        self._validate(model)
        return self._profile_repository.update(model)

    def delete(self, id:int):
       return self ._profile_repository.delete(id)

    def _validate(self, model:profile_model):
        return;