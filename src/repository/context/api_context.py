from ..context.json_context import JsonContext


class ApiContext:
    test_table: JsonContext = JsonContext("test.json")
    user_table: JsonContext = JsonContext("users.json")
<<<<<<< HEAD
    profile_table: JsonContext = JsonContext("profiles.json")
=======
    sprints_table: JsonContext = JsonContext("sprint.json")
>>>>>>> developfefas
    
    times_table: JsonContext = JsonContext("teams.json")

    def __init__(self) -> None:
        pass
