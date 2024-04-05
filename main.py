def vigenere_decrypt(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted = ''
    key_index = 0

    for char in ciphertext:
        if char in alphabet:
            # Tìm vị trí của ký tự trong bảng chữ cái và thực hiện phép trừ
            index = (alphabet.index(char) - alphabet.index(key[key_index])) % len(alphabet)
            decrypted += alphabet[index]
            key_index = (key_index + 1) % len(key)
        else:
            decrypted += char

    return decrypted


# Cụm từ mã hóa cần giải mã
ciphertext = 'ZVSU CMDS JLHL W'
# Khóa Vigenère
key = 'THERE'

# Giải mã cụm từ
decrypted_text = vigenere_decrypt(ciphertext.replace(" ", ""), key)
print("Cụm từ sau khi giải mã:", decrypted_text)
