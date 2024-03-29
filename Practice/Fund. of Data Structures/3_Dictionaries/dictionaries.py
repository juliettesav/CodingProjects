dictionary = {
    'Texas':'Austin',
    'New York':'Albany'
}

print(dictionary['New York'])

for key in dictionary.keys():
    print(key)

for key, value in dictionary.items():
    print(f'{value}, {key}')



user_pref = {
    "language":"English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format":"MM/DD/YYY"
}

user_pref["language"] = "Spanish"
user_pref['volume'] = 50
user_pref["highlight_color"] = "yellow"

del user_pref["currency"] #deletes item 
removed_item = user_pref.pop("date_format", "N/A") #pop function retreives item when deleting it

print(user_pref)