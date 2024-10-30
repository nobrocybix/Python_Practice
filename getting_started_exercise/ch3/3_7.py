names = ['Ace', 'Brady', 'Charlie', 'Darcy', 'Elwin']
unable_names = names[0]
names[0] = 'Alex'
message = "and I have dinner together."

print(names[0] + " " + message)
print(names[1] + " " + message)
print(names[2] + " " + message)
print(names[3] + " " + message)
print(names[4] + " " + message) 

print(unable_names + " " + "can't come")

print("so I found a bigger dining table")

names.insert(0, 'Helen')
names.insert(3, 'Judy')
names.append('Kathy')

new_message = ", I would like to invite you to dinner"

print(names[0] + new_message)
print(names[1] + new_message)
print(names[2] + new_message)
print(names[3] + new_message)
print(names[4] + new_message)
print(names[5] + new_message)
print(names[6] + new_message)
print(names[7] + new_message)

print(names)

print("I can only invite two guests to dinner")

news_names = names.pop(0)
print(news_names + " " + "Sorry, I can't invite you to dinner")

news_names = names.pop(0)
print(news_names + " " + "Sorry, I can't invite you to dinner")

news_names = names.pop(0)
print(news_names + " " + "Sorry, I can't invite you to dinner")

news_names = names.pop(0)
print(news_names + " " + "Sorry, I can't invite you to dinner")

news_names = names.pop(0)
print(news_names + " " + "Sorry, I can't invite you to dinner")

news_names = names.pop(0)
print(news_names + " " + "Sorry, I can't invite you to dinner")

print(names[0] + " " + "I still can invite you to dinner")

print(names[1] + " " + "I still can invite you to dinner")

del names[0]
del names[0]

print(names)