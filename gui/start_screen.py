from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, \
    QPushButton ,QHBoxLayout
from PySide6.QtGui import QPixmap

existing_username = "qwe"
existing_password = "123"
existing_email = "qwe@wp.pl"


class StartScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Cart Master (SCM)")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("images/images.png"))

        #

        username_label_login = QLabel("Username:")
        self.username_input_login = QLineEdit()

        password_label_login = QLabel("Password:")
        self.password_input_login = QLineEdit()
        self.password_input_login.setEchoMode(QLineEdit.Password)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)

        reqister_switch_button = QPushButton("Create an account!")
        # reqister_switch_button.clicked.connect(self.show_register)

        #

        email_label_register = QLabel("Email:")
        self.email_input_register = QLineEdit()

        username_label_register = QLabel("Username:")
        self.username_input_register = QLineEdit()

        password_label_register = QLabel("Password:")
        self.password_input_register = QLineEdit()
        self.password_input_register.setEchoMode(QLineEdit.Password)

        register_button = QPushButton("Sign in")
        register_button.clicked.connect(self.register)

        switch_to_login_button = QPushButton("Login")
        # switch_to_login_button.clicked.connect(self.show_login)

        #

        v_layout_login = QVBoxLayout()
        v_layout_login.addWidget(username_label_login)
        v_layout_login.addWidget(self.username_input_login)
        v_layout_login.addWidget(username_label_login)
        v_layout_login.addWidget(self.username_input_login)
        v_layout_login.addWidget(password_label_login)
        v_layout_login.addWidget(self.password_input_login)

        h_layout_login = QHBoxLayout()
        h_layout_login.addWidget(reqister_switch_button)
        h_layout_login.addWidget(login_button)

        #

        v_layout_register = QVBoxLayout()
        v_layout_register.addWidget(email_label_register)
        v_layout_register.addWidget(self.email_input_register)
        v_layout_register.addWidget(username_label_register)
        v_layout_register.addWidget(self.username_input_register)
        v_layout_register.addWidget(password_label_register)
        v_layout_register.addWidget(self.password_input_register)
        v_layout_register.addWidget(register_button)


        primary_v_layout = QVBoxLayout()
        primary_v_layout.addWidget(image_label)
        primary_v_layout.addWidget(image_label)
        primary_v_layout.addLayout(v_layout_login)
        primary_v_layout.addLayout(h_layout_login)

        self.setLayout(primary_v_layout)




    def login(self):
        username = self.username_input_login.text()
        password = self.password_input_login.text()

        if username == existing_username and password == existing_password:
            print("Login successful!")
        else:
            print("Login failed!")

    def register(self):
        email = self.email_input_register.text()
        username = self.username_input_register.text()
        password = self.password_input_register.text()

        if email != existing_email:
            if username != existing_username:
                print("Successful!")
            else:
                print("Username existing!")
        else:
            print("Eamil existing!")
