# -*- coding: utf-8 -*- 
from flask import render_template
from flask import Flask
import datetime
app = Flask(__name__)

# Контроллеры, для упрощения собраны в 1 модуле
# Фактически стоит разнести на разные модули/файлы

# Присутствует несколько демо примеров, которые к задаче не относятся
# Служат для упрощения процесса освоения flask

@app.route("/test")
def test():
    return """
    <h1>Hello</h1>
    <h2>Paragraph 1</h2>
    <p>Paragraph 2</p>
    """

@app.route("/")
def hello():
    name = "Eugeny"
    week = ["Понедельник","Вторник","Среда", "Четверг",
     "Пятница","Суббота","Воскресенье"]
    time = datetime.datetime.now()
    return render_template("index.html",
            username=name, time=time,week=week)

from flask import request 
# Импорты расположены перед тем, как понадобтс для последующих
# обработчиков запросов

@app.route("/calc", methods=["GET", "POST"])
def calc():
    a = float(request.form.get("a", default=0))
    b = float(request.form.get("b", default=0))
    summ = a + b
    return render_template("calc.html",summ=summ)

import books as books_lib
@app.route("/books")
def books():
    return render_template("books.html",books=books_lib.books)    

@app.route("/books/<id>")
def book(id):
    book = books_lib.books[int(id)]
    return render_template("book.html",book=book)    

from flask import redirect
@app.route("/books/new",methods=["GET", "POST"])
def book_add():
    name = request.form.get("name", default="")
    title = request.form.get("title", default="")
    year = request.form.get("year", default="")
    id = len(books_lib.books)
    if name:
        book = books_lib.Book(id,name,title,year)
        books_lib.books.append(book)
        return redirect("/books")
    return render_template("new.html")    