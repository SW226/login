#登入程式
a = 0
while a < 3:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		a = a + 1
		b = 3 - a
		if b > 0:
			print('密碼錯誤,還剩', b, '次機會')
		else :
			print('帳號已鎖定')
