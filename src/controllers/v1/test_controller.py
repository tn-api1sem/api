from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def test_route():
    return `{"response":"OK"}