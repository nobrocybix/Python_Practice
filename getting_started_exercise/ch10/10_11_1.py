import json

favor_num = input("輸入一個喜歡的數字:")
filename = "favor_num.json"
with open(filename, "w") as file_object:
    json.dump(int(favor_num), file_object)
