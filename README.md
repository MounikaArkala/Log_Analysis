####### Mounika Arkala ######
###### Project_LogAnalysis######

# Description of the project:
The Project LogAnalysis aims to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.
                                
                               
# The database includes three tables:
The authors table includes information about the authors of articles.

The articles table includes the articles themselves.

The log table includes one entry for each time a user has accessed the site.



# The reporting tool answers the following questions:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. 


# Design of the code for question 1:
To generate the report for question 1, I created a view as title of the article and no.of times it is accessed

          create view popular_articles as 
          select a.title,count(l.path) as access_count 
          from articles a, log l 
          where l.path like  '%' || a.slug || '%'  and l.status ='200 OK'
          group by a.title;
          
From the resulted view popular_articles, popular three articles with the no.of times each article is accessed are selected as result.

# Design of the code for question 2:
To generate the report for question 2, I created a  view as authorName and no.of views of total articles for each author

          create view popular_authors as 
          select au.name, sum(p.access_count) as totalaccess_count 
          from articles a, popular_articles p, authors au 
          where a.title=p.title and a.author=au.id 
          group by au.name;
          
From the resulted view popular_authors,authorNames and no.of views of total articles for each author in decreasing order is selcted as result.

# Design of the code for question 3 
I did following four steps:
step 1: created a view as date and no.of requests led to error on that particular date 

          create view request_errorlog as 
          select time, count(time) as error_occurencecount from 
          (select time :: date from log 
          where status='404 NOT FOUND') as foo 
          group by time 
          order by time;
          
step 2: created a view as date and no.of  requests handled on that particular date 
          
          create view request_log as 
          select time, count(time) as total_occurencecount from
          (select time :: date from log) as foo1 
          group by time 
          order by time;
          
step 3: created a view as date and % of requests leading to errors

          create view error_percent as 
          select r1.time,
          ((r1.error_occurencecount / r2.total_occurencecount :: decimal)* 100) 
          as percentage from request_errorlog r1, request_log r2
          where r1.time=r2.time""")
          
step 4: From the created view error_percent of requests of value more than 1% leading to errors is selcted as a result.

# How to run the code: 
The components needed to run this project are: Python, PostgreSQL, psycopg2 library 

step 1: To install psycopg2 library use the following command:

pip install psycopg2


step 2: The data is present at newsdata.sql file and can be downloaded at https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

step 3:After downloading newsdata.sql file use the follwing commands

psql -d news — To connect to the database named news 

psql -f newsdata.sql — To run the SQL statements in the file newsdata.sql


step 4: Run the python file

Through command line: python loganalysis.py

Through an IDE: open "loganalysis.py" file from python shell and go to run-> run module.

Either way using command line or IDE, the result will be diplayed in console.

