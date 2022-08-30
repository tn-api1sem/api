from asyncio.windows_events import NULL
from fileinput import close, filename
import json

class ApiContext:
    _file_name = "";
    _file = {};
    _context = [];

    def __init__(self, filename):
        _file_name = filename

    def _open_connection(self):
        self._file = open(self._file_name);
        self._context = json.loads(self._file)

    def get(self):
        return self._context

    def get(self, id):
        index =  self._get_registry_index(id)
        
        if index == -1:
            return {};
        
        return self._context[index];

    def insert(self,data):
        self._open_connection()
        #TODO - Id sequencial
        self._context.append(data);
        self._close_connection()

    def update(self, data):
        index = self._get_registry_index(data.id)
        
        if index == -1:
            raise Exception("Registry not found")

        self._context[index] = data
        return data;

    def delete(self, id):
        index = self._get_registry_index(data.id)
        
        if index == -1:
            raise Exception("Registry not found")

        del self._context[id]

    def commit(self):
        self._file.clear();
        self._file.write(self._context)

    def _close_connection(self):
        close()

    def _get_registry_index(self, id):
        for i in range(self._context.__len__):
              if self._context[i].id == id:
                  return i

        return -1

    
    

