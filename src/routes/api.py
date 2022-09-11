from fastapi import APIRouter
from ..controllers import test_controller

router = APIRouter()
router.include_router(test_controller.router)