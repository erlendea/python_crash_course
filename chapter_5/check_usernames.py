current_users = ['admin', 'erlend', 'Eivind', 'ingrid', 'arne']
print(current_users)

current_users_lower = []

for current_user in current_users:
    current_users_lower.append(current_user.lower())

print(current_users_lower)

new_users = ['Admin', 'Ingrid', 'Dexter', 'eivind']

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"The username {user} is already used. Find a new one!")
    else:
        print(f"The username {user} is available.")