from pytest import mark
from Framework.loginpage import LoginPage
from Framework.homepage import HomePage

headers = "email, password"
data = [("Debashis.Behera@company.com", "Password123"),
        ("sam.biswal@company.com", "Password123")
        ]

@mark.parametrize(headers, data)
def test_Login(_driver, email, password):

    # Click on Login Link
    hp = HomePage(_driver)
    hp.home_click_login()
    lp = LoginPage(_driver)
    # Enter Email
    lp.login_enter_email(email)
    # Enter Password
    lp.login_enter_password(password)
    # Click Login
    lp.login_click_login()

