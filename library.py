from pkgutil import get_data
import  mysql.connector
from PIL import Image


class db:
    #constrcutor 
    def __init__(self):
        # for mysql connection
        self.__conn=mysql.connector.connect(host="localhost",user="root",password="", database="project")

    # private method For fire the querry
    def __fire(self, qry):
        # import the cursor from connection
        cursor=self.__conn.cursor()
        cursor.execute(qry)
        return cursor
    
    def __where(self, condi={}):
        st=" where "
        i=1
        for key, value in condi.items():
            if(len(condi)==i):
                if(type(value)==int):
                    st=st + key + " = " + str(value) + "  "
                else:
                    st=st + key + " = '" + str(value) + "'  "
            else:
                if(type(value)==int):
                    st=st + key + " = " + str(value) + " and  "
                else:
                    st=st + key + " = '" + str(value) + "' and  "
            i=i+1
        return st

    def getdata(self, table, condi={}):
        if(len(condi)==0):
            qry="select * from " + table
        else:
            qry="select * from " + table + self.__where(condi)
        cur=self.__fire(qry)
        # For multiple data fetching
        data=cur.fetchall()
        mydata={"message":"Successfully get Data","status":True,"data":data,"count":cur.rowcount}
        return mydata

    def getSingleData(self, table, field, value):
        qry="select * from " + table + " where " + field + "='" + value + "'"
        cur=self.__fire(qry)
        # For single data fetching
        data=cur.fetchone()
        mydata={"message":"Successfully get Data","status":True,"data":data,"count":cur.rowcount}
        return mydata


    def deldata(self,table,condi={}):
        if(len(condi)==0):
            qry="delete from " + table
        else:
            qry="delete  from " + table +self.__where(condi)   
        cur=self.__fire(qry)
        if(cur.rowcount>=1):
            mydata={"message":"Delete Success fully","status":True,"count":cur.rowcount}
            return mydata
            
        else:
            return False

    def insertdata(self,table,data={}):
        qry=" insert into " + table + " set "
        i=1
        for key, value in data.items():
            if(len(data)==i):
                if(type(value)==int):
                    qry+= key + " = " + str(value) + " "
                else:
                    qry+= key + " = '" + str(value) + "' "
            else:
                if(type(value)==int):
                    qry+= key + " = " + str(value) + ", "
                else:
                    qry+= key + " = '" + str(value) + "', "
            i+=1
        cur=self.__fire(qry)
        # commit= confirms changes to the database made by user
        self.__conn.commit()

        if(cur.rowcount==1):
            mydata={"message":"Successfully","status":True,"data":data,"count":cur.rowcount}
            return mydata
        else:
            return False

    def update(self,tab,data,condi):
        st="update " + tab +" set "
        i=1
        for key,value in data.items():
            if(len(data)==i):
                if(type(value)==int):
                    st=st + key + " =" + str(value) + " "
                else:
                    st=st + key + " ='" + str(value) + "' "
            else:
                if(type(value)==int):
                    st=st + key + " = " + str(value) + ", "
                else:
                    st=st + key + " ='" + str(value) + "', "
            i=i+1
        st=st + self.__where(condi)
        cur=self.__fire(st)
        self.__conn.commit()
        return st
  
