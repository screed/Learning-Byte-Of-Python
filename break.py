# File name: break.py

while True:
	print('Чтобы закончить введите выход')
	s = input('Введите что-нибудь : ')
	if s == 'выход':
		break
	print(s)
	print('Длина строки: ', len(s))
print(s)
print('Завершние')