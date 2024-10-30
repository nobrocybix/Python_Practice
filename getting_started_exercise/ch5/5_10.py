current_users = ['admin', 'sally', 'eric', 'George', 'JOE']

new_users = ['peter', 'ken', 'george', 'Joe', 'kim']

for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(new_user + " is already an existing user.")
    else:
        print(new_user + " is a new user.")