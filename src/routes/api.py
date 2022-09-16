from fastapi import APIRouter
from ..controllers import usuario_controler, test_controller, autenticacao_controller

router = APIRouter()
router.include_router(test_controller.router)
router.include_router(autenticacao_controller.router)
router.include_router(usuario_controler.router)
  