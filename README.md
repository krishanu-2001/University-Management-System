# University-Management-System
#### This is Course project for CS-258. Project Number - P012 
  
Krishanu Saini 190001029 <br>
Rahul Kumar 190001049 <br>
Kuldeep Singh 190001030  <br>
Deepkamal Singh 190001011    
<hr>

Visit [http://softwarep012.com](http://softwarep012.pythonanywhere.com/) for live demo. Frontend and Backend working.  
<br />
Note for every input field: 

      user-id = 1
      password = 1234
      
  
Clone this project  
  
## Installing Requirements  
      1. Mysql (preferably use Mysql Workbench 8.0)  
      
      2. Python 3.8 / 3.7 / 3.6 ( Not compatible with python 3.9 )  
 <br ><br ><br > 
  
## STEP 1  ( IMPORTING MYSQL DATABASE)
      1. Run DDL commands in university.ddl and SQL commands populate.sql in /sql folder  
      
      2. Put host / port / password / database name in db.yaml  
      
       Note the above step is necessary to ensure database works on your system 
<br ><br ><br >

## STEP 2  ( STARTING FLASK SERVER )  
### WINDOWS -- EVERYTHING IS AUTOMATED  

      Double click on makefile.bat -> will do all steps below  
        
      Ensure you are using python 3.7 and db.yaml is edited


### MANUAL  

      if possible use venv

      pip install -r requirements.txt

      Ensure you have edited db.yaml and imported mysql  

      Run the application by executing the command python app.py

      Use python 3.7 u

      The application runs on localhost:5000
      
### Testing  

Library used - unittest, flask_testing  
For running test file
STEPS: 

    pip install -r requirements.txt
    python test.py

FOR DETAILED COVERAGE

    coverage run --source models -m unittest discover && coverage report
    coverage html


TestCase Details - 
1. Auth section - 100%(test.py)
2. Admin section - 97%(test.py)
3. Student section - 100%(test_student.py)
4. Faculty section - 97%(test_faculty.py)

#### See [Coverage file](/htmlcov)  
Please Download the folder and open index.html
  
<br /><br />
### ER Model  
![alt text](https://github.com/ronnie-36/University-Management-System/blob/main/sql/ums_ER.jpg)
      

