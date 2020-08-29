# import database libary
import MySQLdb

# define class Database
class Database:
    # constructor of the class
    def __init__(self, **kwargs):
        self.__host = str(kwargs.get('host'))
        self.__user = str(kwargs.get('user'))
        self.__password = str(kwargs.get('password'))
        self.__database = str(kwargs.get('database'))

    # private method to connect the programm to the database
    def __connect(self):
        try:
            self.__db = MySQLdb.connect(host = self.__host, user = self.__user, passwd = self.__password, db = self.__database)
            self.__cur = self.__db.cursor()
        except:
            print("Couldn't connect to the Database!")

    # private method to disconnect the programm from the database
    def __disconnect(self):
        try:
            self.__db.commit()
            self.__cur.close()
            self.__db.close()
        except:
            print("Couldn't disconnect! Something went wrong!")

    # public method to execute a statement -> returns if the statement has worked
    def execDML(self, statement):
        self.__connect()
        result = False
        try:
            self.__cur.execute(str(statement))
            result = True
        except:
            print("Couldn't execute this statement! Check your syntax!")
        self.__disconnect()
        return result

    # public method to execute a select statement -> returns a 2 dimentional result array
    def execSelect(self, statement):
        self.__connect()
        result = ()
        try:
            self.__cur.execute(str(statement))
            result = self.__cur.fetchall()
        except:
            print("Couldn't execute this statement! Check your syntax!")
        self.__disconnect()
        return result