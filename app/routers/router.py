from fastapi import APIRouter
from ..models.message import InputModel, OutputModel

router = APIRouter(prefix="/minienigma", tags=["process"])

@router.post("/", response_model=OutputModel)
def process_texts(input_data: InputModel):
    processed_result = f"test mensaje"
    return {"result": processed_result}
