from ..repository.context.api_context import ApiContext


class times_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get(self):
        return self._apiContext.times_table.get_all()

    def busca_id_times(self, id):
        return self._apiContext.times_table.get(id)

    def findTeamByGroup(self, idGroup:int):
        times = self.get();

        timesNoGrupo = [];
        for time in times:
            if time.id_group == idGroup:
                timesNoGrupo.append(time)


        return timesNoGrupo

    def post_times(self, objectPost):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.insert(objectPost)
        self._apiContext.times_table.commit()

    def update(self, objectPut):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.update(objectPut)
        self._apiContext.times_table.commit()

    def delete_id_times(self, id: int):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.delete(id)
        self._apiContext.times_table.commit()