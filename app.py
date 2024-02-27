from flask import Flask, url_for, render_template

app = Flask(__name__)

# Define a global variable to store the added books
library = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/library')
def library_page():
    return render_template('library.html', library=library)


@app.route('/add_to_library/<book_title>')
def add_to_library(book_title):
    global library
    if book_title not in library:
        library.append(book_title)
    return render_template('index.html')


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  