import psycopg2


def fetch_query(query):
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


def top_3_article():
    result = fetch_query("""select articles.title, count(log.path)
    from articles, log
    where log.path = '/article/' || articles.slug
    group by articles.title
    order by count(log.path) desc limit 3;""")
    print("\n The three most popular article of all time are: \n")
    for result in result:
        print('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


def most_popular_authors():
    result = fetch_query("""select authors.name, count(*) as views
    from articles inner join
    authors on articles.author = authors.id inner join
    log on concat('/article/', articles.slug) = log.path
    group by authors.name
    order by views desc;""")
    print("\n The most pupular Authors of all time are: \n")
    for result in result:
        print('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


def error_days():
    result = fetch_query("""select *
    from (select date(time),round(100.0*sum(case log.status
    when '200 OK'  then 0 else 1 end)/count(log.status),3) as error from log
    group by date(time) order
    by error desc) as subq where error > 1;""")
    print("\n Days with more than 1% requests error are: \n")
    for result in result:
        print('\t' + str(result[0]) + ' - ' + str(result[1]) + ' %')


if __name__ == '__main__':
    top_3_article()
    most_popular_authors()
    error_days()
