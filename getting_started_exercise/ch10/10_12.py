import json

def input_favor_num():

    while True:
        try:
            filename = "favor_num.json"            
            favor_num = input("輸入一個喜歡的數字:")
            favor_num = int(favor_num)           
            with open(filename, "w") as file_object:
                json.dump(favor_num, file_object)
            break
        except ValueError:
            print("請輸入數字:")
    return favor_num           

def output_favor_num():
    filename = "favor_num.json"
    try:
        with open(filename, "r") as file_object:
            i_num = json.load(file_object)
    except FileNotFoundError:
            i_num = input_favor_num()
    return i_num

favor_num = output_favor_num()
print("我知道你喜歡的數字:" + str(favor_num))