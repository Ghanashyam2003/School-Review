School Review Manager - Flask App
This is a simple Flask web app where users can submit reviews for schools and view them in a table.
It connects with a MySQL database to store and display the data.

Features -
1.Submit a review with school name, reviewer name, rating (1–5), and comment

2.View all submitted reviews in a clean table layout

3.Delete any review

4.Data is stored using MySQL

 Tech Stack - 

Python + Flask
MySQL (via XAMPP)
HTML + Bootstrap
Jinja2 Templates

 How to Run Locally - 

Clone the project or download the ZIP
Run MySQL (from XAMPP Control Panel)
Create database using the reviews.sql file
Setup .env file (sample below):

ini
Copy
Edit
DB_HOST=localhost  
DB_USER=root  
DB_PASSWORD=  
DB_NAME=school_reviews  
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Start the app:

bash
Copy
Edit
python app.py
Open in browser:
 http://127.0.0.1:5000/add-review

File Structure - 

school_review_app/
├── app.py
├── config.py
├── .env
├── reviews.sql
├── templates/
├── static/