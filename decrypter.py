import os
import pyaes

try:
    # abrir e ler arquivo criptografado
    file_name = "teste.txt.p4wned"
    with open(file_name, 'rb') as file:
        file_data = file.read()
        file.close()

except Exception as e:
    print(e)

else:
    # criar chave pra descriptografia
    key = b'myransomware1337'
    aes = pyaes.AESModeOfOperationCTR(key)

    # descriptografando
    decrypt_data = aes.decrypt(file_data)

    # removendo arquivo criptografado
    os.remove(file_name)

    # criando arquivo descriptografado
    new_file = "teste.txt"
    new_file = open(f'{new_file}', 'wb')
    new_file.write(decrypt_data)
    new_file.close()
