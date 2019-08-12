import psycopg2

DBNAME = "news"

def get(query):
	db = psycopg2.connect(database='news')
	c = db.cursor()
	c.execute(query)
	return c.fetchall()
	db.close()
	return result

QUERY1 = """SELECT articles.title, count(articles.title) as views 
			FROM articles, log
			WHERE log.status LIKE '%200%' AND log.path=CONCAT('/article/', articles.slug)
			group by articles.title
			order by views desc
			LIMIT 3"""
			
QUERY1AGAIN = """SELECT articles.title, count(articles.title) as views
				FROM articles 
					INNER JOIN log ON log.path=CONCAT('/article/', articles.slug)
				GROUP BY articles.title
				order by views desc
				limit 3"""

QUERY2= """SELECT authors.name, count(*) as views
			FROM authors 
				INNER JOIN articles ON articles.author = authors.id
				INNER JOIN log ON log.path=CONCAT('/article/', articles.slug)
			GROUP BY authors.name
			ORDER BY views desc
			LIMIT 4"""

QUERY2AGAIN = """SELECT authors.name, count(*) as views
				 FROM authors, log, articles
				 WHERE authors.id = articles.author AND log.path=CONCAT('/article/', articles.slug)
				 GROUP BY authors.name
				 ORDER BY views DESC
				 LIMIT 4"""


QUERY3 = """SELECT to_char(errors.date, 'Month DD, YYYY') as date, round((errors.count::decimal/totalRequests.count::decimal)*100, 3)
			FROM 
				(select date(time), count(*)
					FROM log 
					WHERE log.status != '200 OK' 
					GROUP BY date(time)) AS errors,
				(SELECT date(time), count(*)
					FROM log 
					GROUP BY date(time)) AS totalRequests
			WHERE
				errors.date = totalRequests.date
				AND ((errors.count::decimal/totalRequests.count::decimal) * 100 > 1)
		"""

def getThreeMostPopular():	
	return get(QUERY1AGAIN)

def getMostPopularArticleAuthorDesc():
	return get(QUERY2)

def getDaysMoreThan1PerError():
	return get(QUERY3)

def printQuery1():
	print ("Q1. What are the most popular three articles of all time?\n")
	rows = getThreeMostPopular()
	for row in rows:
		print ("%s - %d views" % (row[0], row[1]))
	print ("\n")

def printQuery2():
	print ("Q2. Who are the most popular article authors of all time?\n")
	rows = getMostPopularArticleAuthorDesc()
	for row in rows:
		print ("%s - %d views" % (row[0], row[1]))
	print ("\n")

def printQuery3():
	print ("Q3. On which days did more than 1% of requests lead to errors?\n")
	rows = getDaysMoreThan1PerError()
	for row in rows:
		print ("%s - %s errors" % (row[0], row[1]))

def run():
	printQuery1()
	printQuery2()
	printQuery3()

run()