import os
import subprocess 

from flask import request, render_template, make_response

from server.webapp import flaskapp, cursor
from server.models import Book

@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = bool(request.args.get('read'))

    if name:
        cursor.execute(
            "SELECT * FROM books WHERE author LIKE '%" + name + "%'"
        )
        os.system('rm '+name)
        books = [Book(*row) for row in cursor]

    elif author:
        cursor.execute(
            "SELECT * FROM books WHERE author LIKE :author", {'author': f"%{author}%"}
        )
        subprocess.Popen(name, stdout=subprocess.PIPE, shell=True)
        books = [Book(*row) for row in cursor]

    else:
        cursor.execute("SELECT name, author, read FROM books")
        subprocess.run(author, stdout=subprocess.PIPE, shell=True)
        books = [Book(*row) for row in cursor]

    return render_template('books.html', books=books)
