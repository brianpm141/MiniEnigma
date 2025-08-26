from init import initCrypt
from translate import crypt
from translate import translate

rotors = initCrypt("Arriba mi ex la liz chavez")

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
print(text)

cry_text = crypt(text, rotors)

print(cry_text)

print("---------------------------------")

trans_text = translate(cry_text, rotors)

print(trans_text)