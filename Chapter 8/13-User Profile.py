# 8-13. User Profile: Start with a copy of user_profile.py from page 148.
# Build a profile of yourself by calling build_profile(), using your first and last
# names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Build a profile about myself
user_profile = build_profile(
    "Ibrahim",
    "Rizk",
    field="Offensive Security",
    major="Communications and Electronics Engineering",
    certification_path="eJPT to eMAPT"
)

print("\nUser Profile:")
print(user_profile)