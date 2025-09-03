from fastapi import APIRouter, HTTPException
from ..models.message import InputModel, OutputModel
from .enigmain.methods import crypt_text, translate_text

router = APIRouter(prefix="/minienigma", tags=["process"])


@router.post("/encrypt", response_model=OutputModel)
def encrypt_message(input_data: InputModel):
    """
    Encrypts a message using the provided password.
    """
    try:
        encrypted_message = crypt_text(input_data.message, input_data.password)
        return {"result": encrypted_message}
    except ValueError as e:
        # Error específico de validación de contraseña (longitud, etc.)
        raise HTTPException(status_code=400, detail=f"Invalid password: {e}")
    except (IndexError, TypeError) as e:
        raise HTTPException(status_code=500, detail=f"Internal processing error: {e}")
 
@router.post("/decrypt", response_model=OutputModel)
def decrypt_message(input_data: InputModel):
    """
    Decrypts a message using the provided password.
    """
    try:
        decrypted_message = translate_text(input_data.message, input_data.password)
        return {"result": decrypted_message}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid password or corrupt message: {e}")
    except (IndexError, TypeError) as e:
        # Error inesperado durante el proceso de desencriptación.
        raise HTTPException(status_code=500, detail=f"Internal processing error: {e}")
