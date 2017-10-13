import psycopg2
# tabulate module is used to print the contents in table format
from tabulate import tabulate

DBNAME = "news"
# connection of database
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
    

def popular_articles():
    """This function returns popular 3 articles of all the time"""
    c.execute("""select * from popular_articles 
                 order by access_count desc limit 3""")
    posts = c.fetchall()
    print""
    print "******Printing the most popular articles of all the time******"
    print_table(posts)


def popular_authors():
    """This function returns authors list according to their popularity"""
    c.execute("select * from popular_authors order by totalaccess_count desc")
    posts = c.fetchall()
    print "******Printing the most popular article authors of all time******"
    print_table(posts)


def error_percent():
    """This function returns the result of days with more than 
    1 requests leading to errors"""
    c.execute("select * from error_percent where percentage>1.0")
    posts = c.fetchall()
    print"***printing days with more than 1% of requests leading to errors***"
    print_table(posts)


def print_table(table_name):
    """prints the table contents"""
    print tabulate(table_name, 
                   headers=[c.description[0][0], c.description[1][0]])
    print""
    
popular_articles()
popular_authors()
error_percent()   
