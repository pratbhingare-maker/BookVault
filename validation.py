def validate_non_empty(value, field_name):
    if not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")

    return value.strip()


def validate_positive_number(value, field_name):
    try:
        number = int(value)

        if number <= 0:
            raise ValueError

        return number

    except ValueError:
        raise ValueError(f"{field_name} must be a positive number.")


def validate_email(email):
    email = email.strip()

    if "@" not in email or "." not in email:
        raise ValueError("Please enter a valid email address.")

    return email