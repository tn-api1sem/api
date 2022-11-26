from ..context.json_context import JsonContext


class ApiContext:
    user_table: JsonContext = JsonContext("users.json")
    profile_table: JsonContext = JsonContext("profiles.json")
    sprints_table: JsonContext = JsonContext("sprint.json")
    times_table: JsonContext = JsonContext("teams.json")
    grupo_table: JsonContext = JsonContext("groups.json")
    userTeam_table: JsonContext = JsonContext("user_team.json")
    avaliacaoUsuario_table: JsonContext = JsonContext("user_rate.json")
    softSkills_table: JsonContext = JsonContext("softskills.json")

    def __init__(self) -> None:
        pass
