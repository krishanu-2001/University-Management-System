# University-Management-System
#### This is Course project for CS-258. Project Number - P012 
"University Management System" is a website with main goal to inculcate technology in the process of managing University data and activites. "University Management System" is a platform where the students can access their academic information and interact with faculty in order to streamline the daily activities of an educational institute.<br>
The project consists of multiple subsystems -
1. Academic Information Delivery System
2. Assignment Creation and Submission
3. Grading System
4. Admin Section(For managing students, faculty, courses and departments)

For more information of University-Management-System you can refer to following documents - <br>
Link for SRS: [SRS Document](https://github.com/ronnie-36/University-Management-System/blob/main/documents/SRS-P012_University_Manager_190001011_190001029_190001030_190001049.pdf)  
Link for Design Document: [Design Document](https://github.com/ronnie-36/University-Management-System/blob/main/documents/DesignDoc-P012_University_Manager_190001011_190001029_190001030_190001049.pdf)

This project is developed by-
1. Krishanu Saini 190001029 <br>
2. Rahul Kumar 190001049 <br>
3. Kuldeep Singh 190001030  <br>
4. Deepkamal Singh 190001011    
<hr>

Visit [http://softwarep012.com](http://softwarep012.pythonanywhere.com/) for live demo. Frontend and Backend working.  
<br />
Note for every input field: 

      user-id = 1
      password = 1234
      
Link for Instruction Manual: [Instruction Manual](https://github.com/ronnie-36/University-Management-System/blob/main/documents/Instruction-manual-P012_190001011_190001029_190001030_190001049.pdf)

# Steps To Install 

## Installing Requirements  
      1. Mysql (preferably use Mysql Workbench 8.0)  
      
      2. Python 3.8 / 3.7 / 3.6 ( Not compatible with python 3.9 )  
 <br ><br ><br > 

## STEP 1  (CLONING AND SETTING ENVIRONMENT VARIABLES)
      1. Clone this project 
      
      2. Create a .env file similar to .env.example file and populate variables in it.

      > MAIL_USERNAME and MAIL_PASSWORD fields in .env file should contain a GOOGLE Email ID and its password required for forgot password feature in authentication    
<br ><br ><br >
  
## STEP 2 ( IMPORTING MYSQL DATABASE)
      1. Run DDL commands in university.ddl and SQL commands in populate.sql present in /sql folder  
      
      2. Create a db.yaml file similar to db.yaml.example file and populate MySQL connection parameters in it. Keep 'mysql_db' field equal to university.
      
       Note the above step is necessary to ensure database works on your system 
<br ><br ><br >

## STEP 3  ( STARTING FLASK SERVER )  
### WINDOWS -- EVERYTHING IS AUTOMATED  

      Double click on makefile.bat -> will do all steps below  
        
      Ensure you are using python 3.7 and db.yaml is edited


### MANUAL  

      if possible use venv

      pip install -r requirements.txt

      Ensure you have created db.yaml, .env and imported mysql 

      Run the application by executing the command python app.py

      Use python 3.7 u

      The application runs on localhost:5000
      
### Testing  

#### Libraries used 
  
      unittest
      flask_testing
      
#### For running test file  
#### STEPS: 

    pip install -r requirements.txt
    python test.py

#### FOR DETAILED COVERAGE

    coverage run --source models -m unittest discover && coverage report
    coverage html

----

#### TestCase Details - 
1. Home section - 100%(test.py)
2. Admin section - 97%(test.py)
3. Auth section - 76%(test_auth.py)
4. Student section - 100%(test_student.py)
5. Faculty section - 97%(test_faculty.py)

#### See [Coverage file](/htmlcov)  
Please Download the folder and open index.html
  
<br /><br />
----
### ER Model  
![alt text](https://github.com/ronnie-36/University-Management-System/blob/main/sql/ums_ER.jpg)
      
## Contributions
Contributions are encouraged. If you want to contribute then follow these steps:
1. Fork this repository and make a copy of your own .
2. Follow the steps given in Steps To Install to clone from forked repo and set up the project
3. Make changes to the project
4. Always remember to pull before you commit
5. Commit final changes to forked repository
6. Create a pull request and if contributors agree then your code will be merged with the main repository
