def check_email(email: str) -> bool:
    if not email or email == "":
        return False
    else:
        if "@" not in email or "." not in email:
            return False
        else:
            return True
