import json

filename = "favor_num.json"
with open(filename, "r") as file_object:
    i_num = json.load(file_object)
    print("我知道你喜歡的數字是 " + str(i_num))  