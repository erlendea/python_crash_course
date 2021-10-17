def build_profile(first, last, **user_info):
    """Build a dictionary for a user."""
    user_info['first'] = first
    user_info['last'] = last
    return user_info
# Create two users with different kinds
# of information.
user_0 = build_profile('albert', 'einstein',
location='princeton')
user_1 = build_profile('marie', 'curie',
location='paris', field='chemistry')
print(user_0)
print(user_1)