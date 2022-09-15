from ..repository.usuario_repository import user_repository


class usuario_services(object):
    _user_repository:user_repository = user_repository()
    def __init__(self):
        pass;

    def buscar_usuario(self):
        return self._user_repository.get()
