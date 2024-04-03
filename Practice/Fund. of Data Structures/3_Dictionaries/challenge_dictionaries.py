user_pref = {

    "timezone": "GMT",
    "language":"English",
    "notifications": None,
    "currency": "USD",
    "theme": None,
}

'''HARD CODED
def update(user_pref):
    updated_user_pref = user_pref
    del updated_user_pref["notifications"]
    del updated_user_pref["theme"]
    return updated_user_pref

print(update(user_pref))
'''

def update(user_pref):
    updated_user_pref = {}
    for key, value in user_pref.items():
        if value is not None: 
            updated_user_pref[key] = value
    return updated_user_pref

print(update(user_pref))