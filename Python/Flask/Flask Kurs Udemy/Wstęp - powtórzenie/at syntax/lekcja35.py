from curses import panel
import functools

user = {"username": "jose", "access_level": "guest"}



def make_secure(func):
  # kepps func first name
  @functools.wraps(func)
  def secure_function(*args, **kwargs):
    if user["access_level"] == "admin":
      return func(*args, **kwargs)
    else:
      return f"user {user['username']} have no admin perimsons"
  return secure_function

@make_secure
def get_admin_password(panel):
  if panel == "admin":
    return "1234"
  elif panel == "billing":
    return "Ultra secure password even more than 1234 :)"

print(get_admin_password(), get_admin_password.__name__)