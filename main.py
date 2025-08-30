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
print("-------------------- Mensaje Original --------------------")
print(text)

rotors = initCrypt("El maik es un pendejo estupido")
cry_text = crypt(text, rotors)

print("-------------------- Mensaje Cifrado --------------------")
print(cry_text)

rotors = initCrypt("El maik es un pendejo estupido")
trans_text = translate(cry_text, rotors)

print("-------------------- Mensaje Descifrado --------------------")
print(trans_text)
