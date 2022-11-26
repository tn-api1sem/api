from http.client import BAD_REQUEST, OK
from fastapi import APIRouter

from ..services.dashboard_service import dashboard_services as DashboardService

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["dashboard"],
    responses={404: {"description": "Not found"}},
)
dashboard_services = DashboardService()


@router.get("/{id}")
def get_user_teams_by_user_id(id: int):
    return dashboard_services.get_user_teams_by_user_id(id)

@router.get("/sprint/{id}")
def get_sprint_by_id_team(id: int):
    return dashboard_services.get_sprint_by_id_team(id)

@router.get("/userRates/{id}")
def get_user_rates_by_sprint_id(id: int):
    return dashboard_services.get_user_rates_by_sprint_id(id)
