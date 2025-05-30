import requests


class AuthUI:
    session_token = None
    def register(self):
        register_api_url = "http://10.10.3.181:8000/api/v1/auth/register"
        data = {
            "first_name" : input("Ism: "),
            "email" : input("Email: "),
            "password" : input("password: ")
        }
        response = requests.post(register_api_url , json=data)
        if response.status_code == 200:
            print("Registered !")
        else:
            print("\n".join(map(lambda x : x[0],response.json().values())))
        self.main()
    def login(self):
        login_api_url = "http://10.10.3.181:8000/api/v1/auth/login"
        data = {
            "email" : input("Email: "),
            "password" : input("password: "),
        }
        response = requests.post(login_api_url , json=data)
        if response.status_code == 200:
            token = response.json().get("token")
            self.session_token = token
            self.account()
        else:
            print("\n".join(map(lambda x : x[0],response.json().values())))
            self.main()
    def account(self):
        print("Welcome")
        menu = """
            1) + Income
            2) - Expenses
            3) History
            0) back
        """
        key = input(menu)

    def main(self):
        menu = """
            1) Register
            2) Login
            3) Exit
            >>>"""

        key = input(menu)
        match key:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                return

AuthUI().main()