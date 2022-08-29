from fastapi import APIRouter
from src.controllers import test_controller #provavelmente tem que corrigir isso

router = APIRouter()
router.include_router(test_controller.router)