from collections import OrderedDict

vocabularys = OrderedDict()

vocabularys['variable'] = '用於儲存資料的命名儲存位置，可以在程序中隨時訪問和修改。'
vocabularys['dictionary'] = '是一種內建的資料類型，用於以鍵值對（key-value pairs）的方式儲存資料。。'
vocabularys['function'] = '用於將程式碼包裝成為一個單獨的檔案，可以讓程式碼重複使用。'
vocabularys['list'] = '用於儲存相同類型的資料的集合'

for key, value in vocabularys.items():
    print(key, value)
