import pymysql

def connectDb():
    db_settings = {
      "host": "127.0.0.1",
      "port": 3306,
      "user": "kjy",
      "password": "1234",
      "db": "ec2",
      "charset": "utf8"
    }
    conn = None
    try:    
        conn = pymysql.connect(**db_settings)
    except Exception as ex:
        print(ex)
    finally:    
        return conn  
      
def getPasswd(conn, name):
    passwd=''
    try:    
        with conn.cursor() as cursor:
            command = 'select passwd from customer where name=%s'
            cursor.execute(command,name)
            result = cursor.fetchall()
            passwd=result[0][0]        
    except Exception as ex:
        print(ex)
    finally:
        return passwd

def check(conn, iname, passwd):
    name=''
    try:    
        with conn.cursor() as cursor:
            command = 'select name from customer where name=%s and passwd=%s'
            cursor.execute(command,(iname, passwd))
            print(passwd)
            result = cursor.fetchall()
            print(result)
            if (len(result)>=1):
                name=result[0][0]        
    except Exception as ex:
        print(ex)
    finally:
        return name

def testGetPaawd():
    name = input('name:')  
    conn = connectDb()
    passwd=getPasswd(conn, name)     
    print(passwd)
   
def main():
    name = input('name:')  
    passwd = input('passwd:')  
    conn = connectDb()
    okName=check(conn, name, passwd)     
    print(okName)

main()  