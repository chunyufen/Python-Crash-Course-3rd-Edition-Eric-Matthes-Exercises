# Chapter 8/User_Profile.py


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile(
    'yufen', 'chun',
    location='china',
    education='phd',
    field='ai, law, tcm'
    )
print(user_profile)