import mysql.connector
from mysql.connector import errorcode

class Connection:
    try:
        db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='db_sistemaBasico'
        )
        print("Database connection made!")

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Base de dados não existe")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuário ou senha incorretos")
        else:
            print(error)

    else:
        db_connection.close()

     
     
     
   
     
       
       
    
       
       
       
   
 
 
       
       
   
	
       
   

  