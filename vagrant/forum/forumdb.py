#
# Database access functions for the web forum.
# 

import time
import psycopg2

def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect("dbname=forum")
    # Make cursor, query, then execute query
    c = DB.cursor()
    query = "SELECT time, content FROM posts ORDER BY time DESC"
    c.execute(query)
    # Posts already sorted from SQL query
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in c.fetchall()]
    DB.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    DB = psycopg2.connect("dbname=forum") 
    c = DB.cursor()
    sql = "INSERT INTO posts (content) VALUES (%s)"
    data = (content,)
    c.execute(sql, data)
    DB.commit()
    DB.close()
