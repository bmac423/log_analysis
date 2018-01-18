#!/usr/bin/env python3
#
# A simple log analysis script for a newspaper site

import psycopg2

DBNAME = "news"

query_popular_articles = '''select articles.title as "Title", count(log.id) as \
                            "Views" \
                        from articles \
                        join log on log.path =
                            concat('/article/', articles.slug) \
                        group by articles.title \
                        order by "Views" desc \
                        limit 3;'''

query_popular_authors = '''select authors.name as "Author", count(log.path) as
                               "Views" \
                           from authors \
                           join articles on authors.id=articles.author \
                           join log on log.path=concat('/article/',
                               articles.slug) \
                           group by authors.name \
                           order by "Views" desc;'''

query_day_errors = '''select "Day", "Error Rate(%)" \
                      from ( \
                          select TO_CHAR(time, 'MONTHDD, YY') as "Day", \
                              round(100 * ((1.0 * sum(case when \
                              status!='200 OK' then 1 else 0 end)) / \
                              (1.0 * count(status))), 1) as "Error Rate(%)" \
                          from log group by "Day") a \
                      where "Error Rate(%)" > 1.0 \
                      order by "Error Rate(%)" desc;'''

def run_query(query):
    # Return formatted results of query
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close
    return results

def format_data(data):
    # Formats data for console print
    print("\n")
    for x in data:
        if x[1]:
            print("{value_1} -- {value_2}".format(value_1=x[0], value_2=x[1]))

print("\n\n**********\n\n")

print("What are the most popular three articles of all time?")
format_data(run_query(query_popular_articles))

print("\n\n**********\n\n")

print("Who are the most popular article authors of all time?")
format_data(run_query(query_popular_authors))

print("\n\n**********\n\n")

print("On which days did more than 1% of requests lead to errors?")
format_data(run_query(query_day_errors))
