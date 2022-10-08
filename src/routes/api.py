from fastapi import APIRouter
from src.controllers import test_controller, autenticacao_controller, usuario_controller

router = APIRouter()
router.include_router(test_controller.router)
router.include_router(autenticacao_controller.router)
router.include_router(usuario_controller.router)
router.include_router(profile_controler)
