from fastapi import APIRouter
from ..controllers import usuario_controller, test_controller

router = APIRouter()
router.include_router(test_controller.router)
#router.include_router(autenticacao_controller.router)
router.include_router(usuario_controller.router)