questionnaire = "questionnaire.txt"

while True:
    reasons = input("為什麼喜歡編程?\n")

    with open(questionnaire, 'a', encoding='utf-8') as q_list:
        q_list.write(reasons + "\n")