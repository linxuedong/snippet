class User:
    name = 'Dawn'
    sex = 1


user = User()

info = {'name': 'Tom', 'sex': 2}

for key, value in info.items():
    setattr(user, key, value)
