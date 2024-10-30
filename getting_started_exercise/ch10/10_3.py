filename = "user.txt"
users = input("請輸入用戶名稱:")

with open(filename, 'a') as users_data:
    users_data.write(users + "\n")