import sqlite3


class HandleDB():
  def __init__(self):
    self._con = sqlite3.connect("./users.db")
    self._cur = self._con.cursor()

  def get_all(self):
    data = self._cur.execute("SELECT * FROM users")
    return data.fetchall()

  def get_only(self, data_user):
    data = self._cur.execute("SELECT * FROM users WHERE username = '{}'".format(data_user))
    return data.fetchone()

  def insert(self, data_user):
    self._cur.execute("INSERT INTO users VALUES('{}','{}','{}','{}','{}','{}')".format(
      data_user["id"],
      data_user["firstname"],
      data_user["lastname"],
      data_user["username"],
      data_user["country"],
      data_user["password_user"]
    ))
    self._con.commit()

  def __del__(self):
    self._con.close()

