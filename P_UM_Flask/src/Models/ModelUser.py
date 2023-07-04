from .entities.User import User
from werkzeug.security import check_password_hash

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            strSQL = """SELECT id, email, password, created_at, updated_at 
                        FROM users 
                        WHERE email = '{}'""".format(user.email)
            cursor.execute(strSQL)
            row = cursor.fetchone()
            if row != None:
                 return User(row[0], 
                            row[1],
                            check_password_hash(row[2],user.password),
                            row[3],
                            row[4])
            else:
                return None


        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            strSQL = """SELECT id, email, password, created_at, updated_at 
                        FROM users 
                        WHERE id = {}""".format(id)
            cursor.execute(strSQL)
            row = cursor.fetchone()
            if row != None:
                return  User(row[0], 
                            row[1],
                            row[2],
                            row[3],
                            row[4])
               
            else:
                return None


        except Exception as ex:
            raise Exception(ex)
        
