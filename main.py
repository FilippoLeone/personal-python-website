from bottle import template
import MySQLdb as sql
from os import getcwd
from platform import system

class Tools:
    """
    The Tools class is a wrapper for alternative website function.
    """

    def GetVersion(filename):
        """
        Get current website version. default filename: 'version'
        """
        if (system == "Linux" or system == "OSX"):
            delimiter = "/"
        else:
            delimiter = "\\"
        with open("{}{}{}".format(getcwd(),delimiter,filename), 'r') as ver:
            return ver.readline()

class Database:
    
    """
    // TODO: Improve overall code quality.
       Example MySQL Usage:
        db = ServerConnect(attributes)
        QuerySelect(db.cursor(), table, field) 
        
        You can also QuerySelect(db.cursor(), table, '*')
        
        WritePost(db.cursor(), Title, Text, Username, Tags)
        db.commit()
    """

    def ServerConnect(Ip, Username, Pwd, Database, Port):
        """
        Enstablish DB connection
        """
        return sql.connect(host=Ip,user=Username,passwd=Pwd,db=Database,port=Port)

    def QuerySelect(cursor, table, field):
        """ 
        Fetching information from a table.
        """
        try:
            cursor.execute("""SELECT {} FROM {}""".format(field,table))
            return cursor.fetchall()
        except:
            return "Nothing found."

    def WritePost(cursor, Title, Text, WrittenBy, imagelink, Tags):
        """
        Writing records to blog.blog_post
        """
        try:
            cursor.execute("""INSERT INTO blog_post (title, text, username, imagelink, tags) VALUES (%s,%s,%s,%s,%s)""", (Title,Text,WrittenBy,imagelink,Tags))
        except:
            return ("Error. I can't write a post with these info.")

    def WriteComment(cursor, BlogId, Username, Text):
        pass

