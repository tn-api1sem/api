from ..context.json_context import JsonContext


class ApiContext:
    user_table: JsonContext = JsonContext("users.json")
    profile_table: JsonContext = JsonContext("profiles.json")
    sprints_table: JsonContext = JsonContext("sprint.json")
    times_table: JsonContext = JsonContext("teams.json")
    grupo_table: JsonContext = JsonContext("groups.json")

    def __init__(self) -> None:
        pass
