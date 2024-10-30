
try:
    input_num = input("請輸入數字:")       
    num = int(input_num)

    input_num_2 = input("請輸入第二個數字:")
    num_2 = int(input_num_2)
    
    print(num)
    print(num_2)

except ValueError:
    print("你輸入不是數字")