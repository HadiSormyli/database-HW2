user = {}
users = []

print("Enter users count:")
n = int(input())

for i in range(0,n):
	print("Enter user.name: ")
	user['name'] = input()
	print("Enter user.age: ")
	user['age'] = int(input())
	users.append(user)

print("Enter name to search: ")

name = input()
flag = False

for u in users:
	if u['name'] == name :
		print(u['age'])
		flag = True
		break

if flag == False :
	print("There is no user with give name!!")
