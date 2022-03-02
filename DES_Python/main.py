from Crypto.Cipher import DES

# Получение чистого ключа из пароля
def clear_key(key):
	if len(key) < 8:
		while len(key) < 8:
			key += 'd'
		key = key.encode('UTF-8')
	else:
		key = ''.join(list(key)[0:8]).encode('UTF-8')
	return key

# Шифрование
def encrypt(key, data):
	def pad(data):
		while len(data) % 8 != 0:
			data += b' '
		return data

	key = clear_key(key)
	des = DES.new(key, DES.MODE_ECB)
	padded_data = pad(data.encode('UTF-8'))
	encrypted_data = des.encrypt(padded_data)
	return encrypted_data

# Дешифровка
def decrypt(key, encrypted_data):
	key = clear_key(key)
	des = DES.new(key, DES.MODE_ECB)
	decrypted_data = des.decrypt(encrypted_data)
	return decrypted_data.decode('UTF-8').strip()

# Тест
if __name__ == '__main__':
	data = 'Это строка для теста!'
	password = 'test'

	encrypted_data = encrypt(password, data)
	print(encrypted_data)

	decrypted_data = decrypt(password, encrypted_data)
	print(decrypted_data)