# File name: continue.py

while True:
	print('Чтобы закончить введите выход')
	s = input('Введите что-нибудь : ')
	if s == 'выход':
		break
	if len(s) < 3:
		print('Слишком мало')
		continue
	print('Введенная строка достатончой длины')