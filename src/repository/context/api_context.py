from ..context.json_context import JsonContext 

class ApiContext:
    test_table: JsonContext = JsonContext("test.json")
    
    def __init__(self) -> None:
        pass


