from fastapi import APIRouter

from src.data.repository.user_repository import UserRepository

router = APIRouter(
    prefix="/api/v1/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)

userRepository = UserRepository()

@router.get("/")
def test_route():
    return userRepository.insert(1)