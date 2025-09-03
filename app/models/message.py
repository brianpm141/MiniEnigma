from pydantic import BaseModel, Field

class InputModel(BaseModel):
    message: str = Field(..., min_length=1, max_length=180)
    password: str = Field(..., min_length=15, max_length=64)

class OutputModel(BaseModel):
    result: str
