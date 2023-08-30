Installing Required Libraries

1.Open Terminal
2.Navigate to the project directory.
cd online_exam
3.Install the required packages using pip.
pip install -r requirements.txt


Running the Server

1.Open Terminal
2.Navigate to the project directory.
cd online_exam
3. Check Project Integrity
python manage.py check
4. Make Migrations for Database Schema
python manage.py makemigrations
5.Implement Database Schema
python manage.py migrate
6.Run the Django development server using the following command:
python manage.py runserver
7.Open your web browser and navigate to http://localhost:8000/ or http://127.0.0.1:8000/. 