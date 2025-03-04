alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shift(how_many, char):
    if char.upper() in alphabet:
        new_index = (alphabet.index(char.upper()) + how_many) % len(alphabet)
        if char.isupper():
            return alphabet[new_index]
        else:
            return alphabet[new_index].lower()
    return char


def vigenere_crypt(input_file, output_file, key):
    with open(input_file, 'r', encoding='utf-8') as f:
        plain_text = f.read()
    
    key = key.upper()
    result = ''
    key_index = 0
    
    for char in plain_text:
        if char.upper() in alphabet:
            shift_amount = alphabet.index(key[key_index % len(key)])
            result += shift(shift_amount, char)
            key_index += 1
        else:
            result += char
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)

def vigenere_decrypt(input_file, output_file, key):
    with open(input_file, 'r', encoding='utf-8') as f:
        cipher_text = f.read()
    
    key = key.upper()
    result = ''
    key_index = 0
    
    for char in cipher_text:
        if char.upper() in alphabet:
            shift_amount = alphabet.index(key[key_index % len(key)])
            result += shift(-shift_amount, char)
            key_index += 1
        else:
            result += char
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)


def caesar_crypt(how_many, input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    result = ''.join(shift(how_many, char) for char in text)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
def caesar_decrypt(how_many, input_file, output_file):
    caesar_crypt(-how_many, input_file, output_file)

def playfair_crypt():
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = (str(input("Anahtar? "))).upper()
    playfair_matrix = list(key)
    print(key)
    
    for char in alphabet:
        if char not in playfair_matrix:
            playfair_matrix.append(char)
    print(playfair_matrix)          
    text = input("Şifrelenecek metin? ").upper().replace("J", "I")
    print(text)

    divided_text = []
    for i in range(0, len(text), 2):
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                divided_text.append(text[i] + "X")
            else:
                divided_text.append(text[i] + text[i + 1])
        else:
            divided_text.append(text[i] + "X")
    print(divided_text)

    encrypted_text = []
    
    for pair in divided_text:
        first_letter = pair[0]
        second_letter = pair[1]

        #İlk ve ikinci harfin playfair dizisindeki indeksini bul
        first_index = playfair_matrix.index(first_letter)
        second_index = playfair_matrix.index(second_letter)

        #Satır ve sütun hesaplama
        first_row, first_col = first_index // 5, first_index % 5
        second_row, second_col = second_index // 5, second_index % 5

        #Aynı satırda ise sağa kaydır
        if first_row == second_row:
            first_index = first_row * 5 + (first_col + 1) % 5
            second_index = second_row * 5 + (second_col + 1) % 5

        #Aynı sütunda ise aşağı kaydır
        elif first_col == second_col:
            first_index = ((first_row + 1) % 5) * 5 + first_col
            second_index = ((second_row + 1) % 5) * 5 + second_col

        #Farklı satır ve sütunda ise dikdörtgen oluştur
        else:
            first_index = first_row * 5 + second_col
            second_index = second_row * 5 + first_col

        #Şifrelenmiş harfleri ekle
        encrypted_text.append(playfair_matrix[first_index] + playfair_matrix[second_index])

    print("".join(encrypted_text))
    

def playfair_decrypt():
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = (str(input("Anahtar? "))).upper()
    playfair_matrix = list(key)

    for char in alphabet:
        if char not in playfair_matrix:
            playfair_matrix.append(char)
    
    text = input("Şifreli metin? ").upper().replace("J", "I")
    
    divided_text = []
    for i in range(0, len(text), 2):
        if i + 1 < len(text):
            divided_text.append(text[i] + text[i + 1])
        else:
            divided_text.append(text[i] + "X")
    
    decrypted_text = []
    
    for pair in divided_text:
        first_letter = pair[0]
        second_letter = pair[1]

        first_index = playfair_matrix.index(first_letter)
        second_index = playfair_matrix.index(second_letter)

        first_row, first_col = first_index // 5, first_index % 5
        second_row, second_col = second_index // 5, second_index % 5

        if first_row == second_row:
            first_index = first_row * 5 + (first_col - 1) % 5
            second_index = second_row * 5 + (second_col - 1) % 5

        elif first_col == second_col:
            first_index = ((first_row - 1) % 5) * 5 + first_col
            second_index = ((second_row - 1) % 5) * 5 + second_col

        else:
            first_index = first_row * 5 + second_col
            second_index = second_row * 5 + first_col

        decrypted_text.append(playfair_matrix[first_index] + playfair_matrix[second_index])

    print("".join(decrypted_text))
