def test_login_with_wrong_password(login_page):
    login_page.open()
    login_page.login("standard_user", "wrong_password")

    assert "Epic sadface" in login_page.get_error_message()

    