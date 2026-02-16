"""
user_profile.py

Demonstrates use of arbitrary keyword arguments.
"""

def build_profile(first_name, last_name, **user_info):
    """Return a dictionary representing a user profile."""
    profile = {
        "first_name": first_name,
        "last_name": last_name,
    }

    for key, value in user_info.items():
        profile[key] = value

    return profile


user = build_profile(
    "Ibrahim",
    "Rizk",
    field="Offensive Security",
    university="Faculty of Engineering",
    interest="Penetration Testing",
)

print(user)
