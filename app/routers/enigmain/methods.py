from .init import initCrypt
import copy
from .translate import crypt
from .translate import translate


#Metodo para encriptar un mensaje
def crypt_text(message: str , password : str) -> str:
    rotors = initCrypt(password)
    return crypt(message, rotors)


#metodo para desencriptar mensaje
def translate_text(message: str , password : str) -> str:
    rotors = initCrypt(password)
    return translate(message,rotors)

