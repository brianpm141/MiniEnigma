from typing import List, Tuple
import string

rotor = list(string.ascii_uppercase + string.digits)
rotor.insert(14, 'Ñ')
rotor.insert(0 , ' ')
rotors = [rotor.copy() for _ in range(5)]
shuffleFlag = "2:2"
shuffledRotors_list = []

# Extrae el desplazamiento de los rotores y el hash de mezca de los rotores
def extract ():
    while True:
        #password = input("Ingresa contraseña: ")
        password = "El maik es un pendejo estupido"
        if len(password) < 15:
            print("La contraseña debe tener al menos 15 caracteres.")
            continue
        if len(password) > 32:
            print("La contraseña debe tener como máximo 32 caracteres.")
            continue
        print("Contraseña válida.")
        break
    
    # Valores para mezcar el alfabeto de los rotores
    shuffle = [ord(char) for char in password[5:]] # Valores de mezcla
    shuffleHash = "".join([str(numero) for numero in shuffle])
    if len(shuffleHash) < 256: #Completa el hash si no llega a 256

        auxhash = [shuffleHash for _ in range(( 256 // len(shuffleHash)) + 1 )]
        auxhash = "".join([str(numero) for numero in auxhash])
        shuffleHash = auxhash[:256]

    if len(shuffleHash) < 256: #Recorta el hash si lo exede
        shuffleHash = shuffleHash[:256]

    # Valores de rotacion inicial
    spins = [ord(char) for char in password[:5]] # Valores de rotación
    return shuffleHash, spins


# Desplaza el alfabeto una pocicion hacia adelante
def movRotor(rot : List): 
    rot.insert(0, rot.pop())


# inicializa la posicion de los rotores
def initRotors():
    for i, (rotor, spin_value) in enumerate(zip(rotors, spins)):
        for _ in range(spin_value):
            movRotor(rotor)


def shuffleRotors_ext(password_hash: str, shuffled_rotors: List[List[str]]) -> Tuple[str, List[int]]:
    global shuffleFlag
    if shuffleFlag == "2:2":
        shuffleFlag = "2:1"
        aux = int(password_hash[:2])
        while aux > 38:
            aux = aux // 2
        shuffled_rotors.append(aux)
        aux = int(password_hash[2:4])
        while aux > 38:
            aux = aux // 2
        shuffled_rotors.append(aux)
        password_hash = password_hash[4:]
        return password_hash, shuffled_rotors

    if shuffleFlag == "2:1":
        shuffleFlag = "1:2"
        aux = int(password_hash[:2])
        while aux > 38:
            aux = aux // 2
        shuffled_rotors.append(aux)

        aux = int(password_hash[2:3])
        while aux > 38:
            aux = aux // 2
        shuffled_rotors.append(aux)
        password_hash = password_hash[3:]
        return password_hash, shuffled_rotors

    if shuffleFlag == "1:2":
        shuffleFlag = "1:1"
        aux = int(password_hash[:1])
        while aux > 38:
            aux = aux // 2
        shuffled_rotors.append(aux)

        aux = int(password_hash[1:3])
        while aux > 38:
            aux = aux // 2
        shuffled_rotors.append(aux)
        password_hash = password_hash[3:]
        return password_hash, shuffled_rotors
    
    if shuffleFlag == "1:1":
        shuffleFlag = "2:2"
        aux = int(password_hash[:1])
        while aux > 38:
            aux = aux // 2
        shuffled_rotors.append(aux)

        aux = int(password_hash[1:2])
        while aux > 38:
            aux = aux // 2
        shuffled_rotors.append(aux)
        password_hash = password_hash[2:]
        return password_hash, shuffled_rotors


# Crea la lista de mezcla 
def createShuffleList(shuffleHash: str, shuffled_list: List[int]) -> List[int]:
    global shuffleFlag
    if not shuffleHash or len(shuffleHash) == 1:
        return shuffled_list , ""
    if len(shuffleHash) == 2:
        shuffleFlag = "1:1"
        shuffleHash, shuffled_list = shuffleRotors_ext(shuffleHash, shuffled_list)
        return shuffled_list , ""
    if len(shuffleHash) == 3:
        shuffleFlag = "2:1"
        shuffleHash, shuffled_list = shuffleRotors_ext(shuffleHash, shuffled_list)
        return shuffled_list , ""

    shuffleHash, shuffled_list = shuffleRotors_ext(shuffleHash, shuffled_list)
    createShuffleList(shuffleHash, shuffled_list)
    return "", shuffled_list


shuffleHash, spins = extract()
cadena, shuffledRotors_list = createShuffleList(shuffleHash, shuffledRotors_list)
print(cadena)
print(shuffledRotors_list)