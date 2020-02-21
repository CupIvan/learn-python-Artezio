#!/bin/env python
'''
5. Написать программу, которая принимает от пользователя имя и пароль. Сравнивает пароль с заданным в коде.
	В случае совпадения печатает в консоль "Password for user: <Имя пользователя> is correct"
	Если пароль не совпадает, то печатает в консоль
	"Password for user: <Имя пользователя> is incorrect"
	"Please try again..."
	И снова запрашивает пароль (не завершается).
'''

password = '12345'

print('User: ', end='')
user = input()

while True:
	print('Password: ', end='')
	if input() == password:
		print("Password for user:", user, "is correct")
		break;
	print("Password for user:", user, "is incorrect")
	print('Please try again...')
