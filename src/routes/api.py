from fastapi import APIRouter
from src.controllers import sprint_controller,autenticacao_controller, usuario_controller, times_controller, profile_controler

router = APIRouter()
router.include_router(autenticacao_controller.router)
router.include_router(sprint_controller.router)
router.include_router(usuario_controller.router)
router.include_router(profile_controler.router)
router.include_router(times_controller.router)
router.include_router(avaliacao_controller.router)