from fastapi import APIRouter
from src.controllers.v1 import test_controller as  test_controller_v1

router = APIRouter()
router.include_router(test_controller_v1.router)