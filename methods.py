from init import initCrypt
import copy
from translate import crypt
from translate import translate

def entrada():
    try:
        with open("entrada.txt", 'r', encoding = 'utf-8' ) as entrada:
            text = entrada.read()
            return text 
    except FileNotFoundError:
        return("El archivo 'entrada.txt' no fue encontrado.")
    except Exception as e:
        return f"Error: {e}"

text = entrada()


#Metodo para encriptar un mensaje
def crypt_text(message: str , password : str) -> str:
    rotors = initCrypt(password)
    return crypt(message, rotors)


def translate_text(message: str , password : str) -> str:
    rotors = initCrypt(password)
    return translate(message,rotors)
