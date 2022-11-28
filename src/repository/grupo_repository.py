from .context.api_context import ApiContext

class grupo_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get(self):
        return self._apiContext.grupo_table.get_all()

    def busca_id_grupo(self, id):
        return self._apiContext.grupo_table.get(id)

    def post_grupo(self, objectPost):
        self._apiContext.grupo_table.begin_transaction()
        insertedItem = self._apiContext.grupo_table.insert(objectPost)
        self._apiContext.grupo_table.commit()
        return insertedItem;

    def put_grupo(self, objectPut):
        self._apiContext.grupo_table.begin_transaction()
        self._apiContext.grupo_table.update(objectPut)
        self._apiContext.grupo_table.commit()

    def delete_id_grupo(self, id: int):
        self._apiContext.grupo_table.begin_transaction()
        self._apiContext.grupo_table.delete(id)
        self._apiContext.grupo_table.commit()

    def get_groups_by_leaders_id(self, userId):
        allGroups = self.get();

        groupWithLeaderFound = [];
        for group in allGroups:
            if group.leader_id == userId or group.client_id == userId:
                groupWithLeaderFound.append(group);

        return groupWithLeaderFound;