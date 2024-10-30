favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

invinvestigation_list = ['jen', 'chris', 'edward', 'phil', 'sarah']

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")

for name in invinvestigation_list:
    if name in favorite_languages.keys():
        print(name.title() + ", thank you for taking the poll.")
    else:
        print(name.title() + ", please take our poll.")

