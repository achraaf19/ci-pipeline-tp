from app.user_manager import UserManager

def test_add_user():
    um = UserManager()
    um.add_user("ali")
    assert um.count_users() == 1