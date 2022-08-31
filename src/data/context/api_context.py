import json
from types import SimpleNamespace

from src.models.default_queryable_entity import DefaultQueryableEntity

class ApiContext:
    _filename = "";
    _file = {};
    _context = DefaultQueryableEntity();
    _is_transaction_opened = False

    def __init__(self, filename) -> None:
        self._filename = filename;
        self.begin_transaction();

    def begin_transaction(self) -> None:
        if(self._is_transaction_opened):
            return;

        with open('C:/Users/mcfiebig/source/repos/api/src/data/database/user.json', 'r') as f:
            data = f.read()
            self._context = json.loads(data, object_hook=lambda d: SimpleNamespace(**d)) 
            f.detach()
            f.close()
        
        self._is_transaction_opened = True

    def get_all(self):
        return self._context.dataset

    def get(self, id):
        index =  self._get_registry_index(id)
        
        if index == -1:
            return {};
        
        return self._context.dataset[index];

    def insert(self,data):
        self._context.last_index += 1
        self._context.dataset.append(data);
        
    def update(self, data):
        index = self._get_registry_index(data.id)
        
        if index == -1:
            raise Exception("Registry not found")

        self._context.dataset[index] = data
        return data;

    def delete(self, id):
        index = self._get_registry_index(id)
        
        if index == -1:
            raise Exception("Registry not found")

        del self._context.dataset[index]

    def commit(self):
        with open('C:/Users/mcfiebig/source/repos/api/src/data/database/user.json', 'r+') as f:
            f.seek(0)
            f.truncate()
            
            database = json.dumps(self._context, default=lambda o: o.__dict__)
            f.write(database)
            
            f.detach()
            f.close()

        self._is_transaction_opened = False

        

    def _get_registry_index(self, id):
        i = 0

        for item in self._context.dataset:
            if item.id == id:
                return i
            i+=1 

        return -1

    
    

