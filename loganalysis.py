#!/usr/bin/env python2.7
import psycopg2
# tabulate module is used to print the contents in table format
from tabulate import tabulate


def get_query_results(query):
    """This function connects to the database, executes the query and prints
    the results"""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    print tabulate(result, headers=[c.description[0][0], c.description[1][0]])
    print""
    db.close()


def popular_articles():
    """This function returns popular 3 articles of all the time"""
    query = "select * from popular_articles order by access_count desc limit 3"
    print""
    print "******Printing the most popular articles of all the time******"
    posts = get_query_results(query)


def popular_authors():
    """This function returns authors list according to their popularity"""
    query = "select * from popular_authors order by totalaccess_count desc"
    print "******Printing the most popular article authors of all time******"
    posts = get_query_results(query)


def error_percent():
    """This function returns the result of days with more than 1 requests
    leading to errors"""
    query = "select * from error_percent where percentage>1.0"
    print"***printing days with more than 1% of requests leading to errors***"
    posts = get_query_results(query)


if __name__ == "__main__":
    popular_articles()
    popular_authors()
    error_percent()
