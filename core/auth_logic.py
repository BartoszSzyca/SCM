from database.users import Users
from database.config import users_session
import re


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def is_valid_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>]).{12,64}$'
    return re.match(pattern, password)


def log_in(login, password):
    existing_user = users_session.query(Users).filter_by(login=login,
                                                         password=password
                                                         ).first()
    users_session.close()
    return existing_user is not None


def register(email, login, password):
    if not email or not login or not password:
        return "Error", "Please complete all fields.", False

    if not is_valid_email(email):
        return "Error", "Invalid email format.", False

    if not is_valid_password(password):
        return "Error", (
            'The password must be between 12 and 64 characters long, '
            'including one lowercase letter, one uppercase letter, one number, and '
            'one special character: "!@#$%^&*(),.?":{}|<>".'), False

    existing_user = ((users_session.query(Users).filter_by(login=login) |
                      users_session.query(Users).filter_by(
                          email=email)).first())
    users_session.close()
    if existing_user.email == email:
        return "Error", "This email is already in use.", False
    elif existing_user.login == login:
        return "Error", "A user with this name already exists.", False
    else:
        new_user = Users(email=email, user_name=login,
                         password=password)
        users_session.add(new_user)
        users_session.commit()
        return "Success", "Registration successful!", True
