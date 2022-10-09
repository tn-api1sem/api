from ..context.json_context import JsonContext 

class ApiContext:
    test_table: JsonContext = JsonContext("test.json")
    user_table: JsonContext = JsonContext("users.json")
    sprints_table: JsonContext = JsonContext("sprint.json")
    
    def __init__(self) -> None:
        pass


