textfile = "guest_book.txt"

while True:
    guest_name = input("請輸入你的名稱:") 
    print(guest_name + " ，你好")

    if guest_name != "":
        with open(textfile, "a") as file:
         file.write(guest_name + "\n")

    stop_input = input("還要輸入其他名稱[y/n]:")

    if stop_input.lower() == "n":
        break
    elif stop_input.lower() != "y":
        print("請輸入 'y' 或 'n'。")
