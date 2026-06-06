The purpose of this project is to be able to log and track what books and other physical media
I have in my personal library. 

June 4, 2026(Initial commit): 
- This is the first commit of the project, will be adding more later.
- Progress: initial commit contains books.py file, a csv file to log entries, and an html file for a minimal frontend 

Eventual goal: small-scale web application that allows users to log their books, connect with friends, request materials, and set their own
pickup and return dates. 

Functions and their purpose
- def get_user_books: displays the books the user has already entered
- def save_to_csv: saves new user entries into the csv file
- def add_book(): user inputs new entries into their collection

Setting up the database(for future reference) 
- Using SQLite and/or SQLAlchemy since most of the data is relational 

Requirement Analysis
- I don't want to have to enable MySQL to use the app.
- I don't want my computer to be hit with traffic

Tools
- Lucidchart
- Jira
- Python
- Flask
- SQLAlchemy
- SQLite


Next Steps
- Adding requirements.txt file so users can download it
- Setting up the database using SQLAlchemy and SQLite
- Designing the UI

Long-term next steps
- Finish application and host it on cloud service 
