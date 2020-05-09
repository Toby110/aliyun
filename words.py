import tornado.web
import tornado.ioloop
import asyncio
import sqlite3
import json

settings={
    "template_path":"template",
    "static_path":"static",
    "dubug":"true",
}

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        conn=sqlite3.connect('template/words.db')
        conn.row_factory=sqlite3.Row
        cur=conn.cursor()
        sql='''select * from whlxx'''
        data=cur.execute(sql).fetchall()
        data=[dict(row) for row in data]
        self.write(json.dumps(data))

def make_app():
    return tornado.web.Application([
        (r'/',IndexHandler),
        (r'/admin', AdminHandler)
    ],**settings)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app=make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

    
    

