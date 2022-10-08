from ..context.json_context import JsonContext 

class ApiContext:
    test_table: JsonContext = JsonContext("test.json")
    user_table: JsonContext = JsonContext("users.json")
    profile_table: JsonContext = JsonContext("profiles.json")
    
    def __init__(self) -> None:
        pass


