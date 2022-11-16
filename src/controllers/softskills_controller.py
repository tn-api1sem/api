from fastapi import APIRouter
from src.services.softskills_service import SoftSkillsService


router = APIRouter(
    prefix="/api/v1/softskills",
    tags=["profile"],
    responses={404: {"description": "Not found"}},
)
softSkillsService = SoftSkillsService()


@router.get("/")
def get_all():
    return  softSkillsService.get_all()




