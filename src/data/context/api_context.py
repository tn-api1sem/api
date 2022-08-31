import json
from fileinput import close
from types import SimpleNamespace

from src.models.default_queryable_entity import DefaultQueryableEntity

class ApiContext:
    _filename = "";
    _file = {};
    _context = DefaultQueryableEntity();

    def __init__(self, filename) -> None:
        self._filename = filename;
        self.begin_transaction();

    def begin_transaction(self) -> None:
        self._file = open('C:/Users/mcfiebig/source/repos/api/src/data/database/user.json', "a+")
        self._file.seek(0);
        self._context = json.loads(self._file.read(), object_hook=lambda d: SimpleNamespace(**d)) 
        return

    def get_all(self):
        return self._context.dataset

    def get(self, id):
        index =  self._get_registry_index(id)
        
        if index == -1:
            return {};
        
        return self._context.dataset[index];

    def insert(self,data):
        self._open_connection()
        self._context.last_index += 1
        self._context.dataset.append(data);
        self._close_connection()

    def update(self, data):
        index = self._get_registry_index(data.id)
        
        if index == -1:
            raise Exception("Registry not found")

        self._context.dataset[index] = data
        return data;

    def delete(self, id):
        index = self._get_registry_index(data.id)
        
        if index == -1:
            raise Exception("Registry not found")

        del self._context.dataset[id]

    def commit(self):
        self._file.clear();
        self._file.write(self._context)
        close()

    def _get_registry_index(self, id):
        for i in range(self._context.__len__):
              if self._context.dataset[i].id == id:
                  return i

        return -1

    
    

