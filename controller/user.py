from model.handle_db import HandleDB
from werkzeug.security import generate_password_hash


class User():
  data_user = {}

  def __init__(self, data_user):
    self.db = HandleDB()
    self.data_user = data_user

  def create_user(self):
    # add id
    self._add_id()
    # encrypt password
    self._passw_encrypt()
    # write new user
    self.db.insert(self.data_user)

  def _add_id(self):
    user = self.db.get_all()
    one_user = user[-1]
    id_user = int(one_user[0])
    self.data_user["id"] = str(id_user + 1)

  def _passw_encrypt(self):
    self.data_user["password_user"] = generate_password_hash(self.data_user["password_user"], "pbkdf2:sha256:30", 30)

