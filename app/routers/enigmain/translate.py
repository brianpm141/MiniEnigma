import string


dictionary = list(string.ascii_uppercase + string.digits)
dictionary.insert(14, 'Ñ')
dictionary.insert(0 , ' ')

rotor_reference = ''


def movRotor(rot : list): 
    rot.insert(0, rot.pop())
    return rot


def rotorSpin(rotors : list) -> list:
    global rotor_reference
    if rotor_reference == rotors[0][0]: 
        rotors[0] = movRotor(rotors[0])
        rotors[1] = movRotor(rotors[1])
        rotors[2] = movRotor(rotors[2])
        rotors[3] = movRotor(rotors[3])
        rotors[4] = movRotor(rotors[4])
    else:
        rotors[0] = movRotor(rotors[0])
        rotors[4] = movRotor(rotors[4])
    return rotors   


def init_ref (rotor):
    global rotor_reference
    rotor_reference = rotor[0]

def crypt(text, rotors) -> str:
    global dictionary
    init_ref(rotors[0])
    crypt_text = []
    aux_pos = 0

    for char in text:
        if char.upper() in dictionary:
            position = int(dictionary.index(char.upper()))
            crypt_text.append(rotors[aux_pos][position])
            rotors = rotorSpin(rotors)
            if aux_pos == 4:
                aux_pos = 0
            else: 
                aux_pos += 1
        else:
            crypt_text.append(char)

    return ''.join(crypt_text)

def translate(text, rotors) -> str:
    global dictionary
    init_ref(rotors[0])
    translate_text = []
    aux_pos = 0

    for char in text:
        if char.upper() in dictionary:
            position = int(rotors[aux_pos].index(char.upper()))
            translate_text.append(dictionary[position])
            rotors = rotorSpin(rotors)
            if aux_pos == 4:
                aux_pos = 0
            else:
                aux_pos += 1
        else:
            translate_text.append(char)

    return ''.join(translate_text)
