from flask import Flask, render_template, request, redirect
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route('/add-review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        school = request.form['school_name']
        reviewer = request.form['reviewer_name']
        rating = int(request.form['rating'])
        comment = request.form['comment']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reviews (school_name, reviewer_name, rating, comment) VALUES (%s, %s, %s, %s)",
                       (school, reviewer, rating, comment))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/reviews')
    return render_template('add_review.html')


@app.route('/')
def home():
    return redirect('/add-review')   # or '/reviews'


@app.route('/reviews')
def reviews():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('reviews.html', reviews=data)

if __name__ == '__main__':
    app.run(debug=True)
