from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, \
    QPushButton, QHBoxLayout, QStackedWidget, QMessageBox
from PySide6.QtGui import QPixmap
from core.auth_logic import log_in, register


class StartScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Cart Master (SCM)")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("images/images.png"))

        self.login_screen = LoginScreen(self)
        self.register_screen = RegisterScreen(self)

        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.register_screen)

        primary_v_layout = QVBoxLayout()
        primary_v_layout.addWidget(image_label)
        primary_v_layout.addWidget(self.stack)

        self.setLayout(primary_v_layout)


class LoginScreen(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        username_label_login = QLabel("Username:")
        self.username_input_login = QLineEdit()

        password_label_login = QLabel("Password:")
        self.password_input_login = QLineEdit()
        self.password_input_login.setEchoMode(QLineEdit.Password)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)

        reqister_switch_button = QPushButton("Create an account!")
        reqister_switch_button.clicked.connect(self.switch_to_register)

        v_layout_login = QVBoxLayout()
        v_layout_login.addWidget(username_label_login)
        v_layout_login.addWidget(self.username_input_login)
        v_layout_login.addWidget(password_label_login)
        v_layout_login.addWidget(self.password_input_login)

        h_layout_login = QHBoxLayout()
        h_layout_login.addWidget(reqister_switch_button)
        h_layout_login.addWidget(login_button)

        v_layout_login.addLayout(h_layout_login)

        self.setLayout(v_layout_login)

    def login(self):
        login = self.username_input_login.text()
        password = self.password_input_login.text()

        if log_in(login, password):
            QMessageBox.information(self, "Success", "Login Successful!")
        else:
            QMessageBox.warning(self, "Error", "Login failed!")

    def switch_to_register(self):
        self.parent.stack.setCurrentWidget(self.parent.register_screen)


class RegisterScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        email_label_register = QLabel("Email:")
        self.email_input_register = QLineEdit()

        username_label_register = QLabel("Username:")
        self.username_input_register = QLineEdit()

        password_label_register = QLabel("Password:")
        self.password_input_register = QLineEdit()
        self.password_input_register.setEchoMode(QLineEdit.Password)

        register_button = QPushButton("Register")
        register_button.clicked.connect(self.register)

        switch_to_login_button = QPushButton("Back to Login")
        switch_to_login_button.clicked.connect(self.switch_to_login)

        v_layout_register = QVBoxLayout()
        v_layout_register.addWidget(email_label_register)
        v_layout_register.addWidget(self.email_input_register)
        v_layout_register.addWidget(username_label_register)
        v_layout_register.addWidget(self.username_input_register)
        v_layout_register.addWidget(password_label_register)
        v_layout_register.addWidget(self.password_input_register)

        h_layout_register = QHBoxLayout()
        h_layout_register.addWidget(switch_to_login_button)
        h_layout_register.addWidget(register_button)

        v_layout_register.addLayout(h_layout_register)

        self.setLayout(v_layout_register)

    def register(self):
        email = self.email_input_register.text()
        login = self.username_input_register.text()
        password = self.password_input_register.text()
        title, message, success = register(email, login, password)

        if success:
            QMessageBox.information(self, title, message)
            self.switch_to_login()

        QMessageBox.information(self, title, message)

    def switch_to_login(self):
        self.parent.stack.setCurrentWidget(self.parent.login_screen)
