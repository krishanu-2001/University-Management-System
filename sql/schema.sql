-- DDL File

-- drop database university;
-- create database university;
use university;

CREATE TABLE program (
	name VARCHAR(100) NOT NULL,
    duration INT NOT NULL,
    PRIMARY KEY(name)
);

CREATE TABLE faculty (
  `faculty_id` VARCHAR(45) NOT NULL,
  `first_name` VARCHAR(90) NOT NULL,
  `last_name` VARCHAR(90) DEFAULT '',
  `address` VARCHAR(200),
  `phone` VARCHAR(10),
  `gender` VARCHAR(10) DEFAULT 'Male',
  `DOB` DATE DEFAULT '2001-08-28',
  `emailid` VARCHAR(90) NOT NULL,
  `password` VARCHAR(90) NOT NULL,
  salary INT NOT NULL,
  research_interests VARCHAR(200) NULL,
  position VARCHAR(90) NOT NULL,
  PRIMARY KEY (`faculty_id`));

CREATE TABLE department (
	dept_id VARCHAR(45) NOT NULL,
    name VARCHAR(200) NOT NULL,
    budget INT DEFAULT 0,
    hod_id VARCHAR(45),
    contact_no VARCHAR(45) NOT NULL,
    foreign key department(hod_id) references faculty(faculty_id) on update cascade on delete set null,
    PRIMARY KEY(dept_id)
); 

CREATE TABLE course (
	c_id VARCHAR(45) NOT NULL,
    name VARCHAR(90) NOT NULL,
    description VARCHAR(200) NULL,
    syllabus VARCHAR(700) NULL,
    credits FLOAT DEFAULT 0.00,
    hours VARCHAR(45) default '3-1-0',
    year DATE NOT NULL,
    notes VARCHAR(200),
    PRIMARY KEY(c_id));


-- this is the current years courses, stores years
CREATE TABLE section (
	sec_id INT NOT NULL auto_increment,
	c_id VARCHAR(45) NOT NULL,
    year VARCHAR(11) DEFAULT '2021',
    sem INT NOT NULL,
    notes VARCHAR(200),
    FOREIGN KEY section(c_id) references course(c_id) on update cascade on delete cascade,
    constraint unique(c_id, sem),
    PRIMARY KEY(sec_id));

CREATE TABLE student (
  `student_id` VARCHAR(45) NOT NULL,
  `first_name` VARCHAR(90) NOT NULL,
  `last_name` VARCHAR(90) DEFAULT '',
  `emailid` VARCHAR(90),
  `address` VARCHAR(200),
  `gender` VARCHAR(10) DEFAULT 'Male',
  `phone` VARCHAR(10),
  `DOB` DATE DEFAULT '2001-08-28',
  `password` VARCHAR(90) NOT NULL,
  sem INT DEFAULT 1,
  cpi FLOAT DEFAULT 0.00,
  branch VARCHAR(45) NOT NULL,
  program VARCHAR(100) DEFAULT 'btech',
  advisor_id VARCHAR(45),
  TAsec_id INT,
  CONSTRAINT advisor foreign key student(advisor_id) references faculty(faculty_id) on update cascade on delete set null,
  CONSTRAINT stud_prog foreign key student(program) references program(name) on update cascade on delete cascade,
  CONSTRAINT stud_dept foreign key student(branch) references department(dept_id) on update cascade on delete cascade,
  CONSTRAINT sec_ta foreign key student(TAsec_id) references section(sec_id) on update cascade on delete set null,
  PRIMARY KEY (`student_id`));

CREATE TABLE `admin` (
  `admin_id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(90) NOT NULL,
  `emailid` VARCHAR(90) NOT NULL,
  `password` VARCHAR(90) NOT NULL,
  `role` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`admin_id`));
  
CREATE TABLE enroll (
	sec_id INT NOT NULL,
    student_id VARCHAR(90) NOT NULL,
    grade FLOAT default 0.00,
    notes VARCHAR(200),
    FOREIGN KEY enroll(sec_id) references section(sec_id) on update cascade on delete cascade,
    FOREIGN KEY enroll(student_id) references student(student_id) on update cascade on delete cascade,
    PRIMARY KEY(student_id, sec_id));

CREATE TABLE teaches (
	sec_id INT NOT NULL,
    faculty_id VARCHAR(90) NOT NULL,
    year DATE NOT NULL,
    notes VARCHAR(200) NOT NULL,
    FOREIGN KEY teaches(sec_id) references section(sec_id) on update cascade on delete cascade,
    FOREIGN KEY teaches(faculty_id) references faculty(faculty_id) on update cascade on delete cascade,
    PRIMARY KEY(faculty_id, sec_id));
    
CREATE TABLE assignment (
	a_id INT UNIQUE NOT NULL auto_increment,
    faculty_id VARCHAR(90) NOT NULL,
	sec_id INT NOT NULL,
    created_at DATETIME,
    start_at DATETIME,
    end_at DATETIME,
    text VARCHAR(1000),
	marks_total INT,
    files_link VARCHAR(150),
    notes VARCHAR(200),
    FOREIGN KEY (faculty_id) references faculty(faculty_id) on update cascade on delete cascade,
    FOREIGN KEY (sec_id) references section(sec_id) on update cascade on delete cascade,
    PRIMARY KEY(a_id));
    
-- This is student assg in ER
CREATE TABLE submission (
	a_id INT NOT NULL,
    student_id VARCHAR(90) NOT NULL,
    submission_id INT UNIQUE NOT NULL auto_increment,
    submitted_at DATETIME ,
    text VARCHAR(1000) ,
    files_link VARCHAR(150) ,
	marks_got INT ,
    notes VARCHAR(200) ,
    FOREIGN KEY (a_id) references assignment(a_id) on update cascade on delete cascade,
    FOREIGN KEY (student_id) references student(student_id) on update cascade on delete cascade,
    PRIMARY KEY(submission_id));

CREATE TABLE has_course(
	program VARCHAR(100),
	c_id VARCHAR(45) NOT NULL,
    sem INT DEFAULT 1,
    branch VARCHAR(100) DEFAULT 'cse',
    foreign key has_course(program) references program(name) on update cascade on delete cascade,
    foreign key has_course(c_id) references course(c_id) on update cascade on delete cascade,
    PRIMARY KEY(program, c_id)
);

CREATE TABLE final_grade(
	student_id VARCHAR(90) NOT NULL,
    c_id VARCHAR(45) NOT NULL,
    grades FLOAT DEFAULT 0.00,
    foreign key final_course(student_id) references student(student_id) on update cascade on delete cascade,
    foreign key final_course(c_id) references course(c_id) on update cascade on delete cascade,
    PRIMARY KEY(student_id, c_id)
);

CREATE TABLE classroom(
	class_id varchar(45) NOT NULL,
    building varchar(90) NOT NULL,
    capacity INT NOT NULL,
    roomno VARCHAR(45) NOT NULL,
    PRIMARY KEY (class_id)
);

CREATE TABLE section_room(
	sec_id INT NOT NULL,
    class_id VARCHAR(45) NOT NULL,
    start_time INT NOT NULL,
    end_time INT NOT NULL,
    day INT NOT NULL,
	foreign key section_room(sec_id) references section(sec_id) on update cascade on delete cascade,
    foreign key section_room(class_id) references classroom(class_id) on update cascade on delete cascade,
    PRIMARY KEY (sec_id, class_id)
);

CREATE TABLE works(
	faculty_id VARCHAR(90) NOT NULL,
    dept_id VARCHAR(45) NOT NULL,
    role VARCHAR(200) DEFAULT "faculty",
	foreign key works(faculty_id) references faculty(faculty_id) on update cascade on delete cascade,
    foreign key works(dept_id) references department(dept_id) on update cascade on delete cascade,
    PRIMARY KEY(faculty_id, dept_id)
);

CREATE TABLE offer_course (
	c_id VARCHAR(45) NOT NULL,
    dept_id VARCHAR(45) NOT NULL,
    notes VARCHAR(45),
    foreign key offer_course(c_id) references course(c_id) on update cascade on delete cascade,
    foreign key offer_course(dept_id) references department(dept_id) on update cascade on delete cascade,
    PRIMARY KEY(c_id, dept_id)
);

CREATE TABLE has_program (
	program VARCHAR(100) NOT NULL,
    dept_id VARCHAR(45) NOT NULL,
    notes VARCHAR(45),
    foreign key has_program(program) references program(name) on update cascade on delete cascade,
    foreign key has_program(dept_id) references department(dept_id) on update cascade on delete cascade,
    PRIMARY KEY(program, dept_id)
);

CREATE TABLE requires (
	prereq_id VARCHAR(45) NOT NULL,
    maincourse_id VARCHAR(45) NOT NULL,
    notes VARCHAR(45),
    foreign key requires(prereq_id) references course(c_id) on update cascade on delete cascade,
    foreign key requires(maincourse_id) references course(c_id) on update cascade on delete cascade,
    PRIMARY KEY(prereq_id, maincourse_id)
);

CREATE TABLE requests (
	r_id INT UNIQUE AUTO_INCREMENT,
	name VARCHAR(45) NOT NULL,
    id VARCHAR(45) NOT NULL,
    notes VARCHAR(200),
    dob datetime,
    status VARCHAR(10) DEFAULT 'pending',
    PRIMARY KEY(r_id)
);

CREATE TABLE notifications (
    n_id INT UNIQUE AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    id VARCHAR(45) NOT NULL,
    notes VARCHAR(200),
    dob datetime,
    status VARCHAR(10) DEFAULT 'unseen',
    PRIMARY KEY(n_id)
);




-- Insert valid emails accordingly for testing forgot password

INSERT INTO program (name,duration) VALUES ('btech',4);
INSERT INTO program (name,duration) VALUES ('mtech',2);
INSERT INTO program (name,duration) VALUES ('ms',2);
INSERT INTO program (name,duration) VALUES ('phd',6);
INSERT INTO program (name,duration) VALUES ('bsc',4);
INSERT INTO program (name,duration) VALUES ('msc',2);
INSERT INTO program (name,duration) VALUES ('mba',2);

INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('1', 'Shaan Sharma', 'sh@sh.com', '81dc9bdb52d04dc20036dbd8313ed055', '02-gandhi-marg new-delhi', '1980-12-30', 80000, 'Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('2', 'Rohan Verma', 'rr@trr.com', '81dc9bdb52d04dc20036dbd8313ed055', '02-Hauz-Khas new-delhi', '1965-12-30', 85000, 'Assistant Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('3', 'Mohan Kumar', 'sha@sh.com', '81dc9bdb52d04dc20036dbd8313ed055', '082-gandhi-marg new-delhi', '1990-12-30', 90000, 'Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('4', 'Kuldeep Singh', 'rar@trr.com', '81dc9bdb52d04dc20036dbd8313ed055', '012-Hauz-Khas new-delhi', '1975-12-07', 80000, 'Associate Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('5', 'Soham Singh', 'shm@trr.com', '81dc9bdb52d04dc134236dbd8313ed055', '21-ranjit-nagar new-delhi', '1995-12-07', 60000, 'Associate Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('6', 'Rahul Kumar', 'rm@trr.com', '81dc9bdb52d023424bd8313ed055', '211-dugri- new-delhi', '1976-12-07', 80000, 'Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('7', 'Krishannu Saini', 'dnsh@trr.com', '81dc9bdb234244dc20036dbd8313ed055', '32-old-delhi new-delhi', '1985-12-07', 85000, 'Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('8', 'Deepkamal Singh', 'rch@trr.com', '81dc9bdb5223424dc20036dbd8313ed055', '221-ansal-plaze new-delhi', '1978-12-07', 65000, 'Associate Professor');

INSERT INTO department (dept_id, name, budget, hod_id, contact_no) VALUES ('cse','Computer Science and Engineering',120000,'1','98765');
INSERT INTO department (dept_id, name, budget, hod_id, contact_no) VALUES ('mech','Mechanical Engineering',120000,'2','98765');
INSERT INTO department (dept_id, name, budget, hod_id, contact_no) VALUES ('ee','Electrical Engineering',120000,'3','98765');
INSERT INTO department (dept_id, name, budget, hod_id, contact_no) VALUES ('ce','Civil Engineering',120000,'4','98765');

INSERT INTO course (c_id, name, year, notes, credits, hours) VALUES ('1','MATHS',"2001-12-30","",3,'3-1-0');
INSERT INTO course (c_id, name, year, notes, credits, hours) VALUES ('2','OS',"2006-06-24","",3,'2-1-0');
INSERT INTO course (c_id, name, year, notes, credits, hours) VALUES ('3','DSA',"2006-06-24","",4,'4-0-0');
INSERT INTO course (c_id, name, year, notes, credits, hours) VALUES ('4','Software Engg',"2009-01-30","",1.50,'3-1-0');
INSERT INTO course (c_id, name, year, notes, credits, hours) VALUES ('5','IC211',"2009-01-01","",3,'3-0-0');

INSERT INTO section (c_id, year, notes, sem) VALUES ('1',"2009","",'4');
INSERT INTO section (c_id, year, notes, sem) VALUES ('1',"2021","",'2');
INSERT INTO section (c_id, year, notes, sem) VALUES ('2',"2020","",'4');
INSERT INTO section (c_id, year, notes, sem) VALUES ('3',"2009","",'4');
INSERT INTO section (c_id, year, notes, sem) VALUES ('4',"2009","",'1');
INSERT INTO section (c_id, year, notes, sem) VALUES ('3',"2009","",'1');
INSERT INTO section (c_id, year, notes, sem) VALUES ('4',"2009","",'2');

INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('1', 'ron', 'ron@ron.com', '81dc9bdb52d04dc20036dbd8313ed055', '100-england', '2001-01-01', 'cse', '4', '9.80','btech','1');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('2', 'Ganguly', 'Ganguly@Ganguly.com', '81dc9bdb52d04dc20036dbd8313ed055', '100-london', '2004-02-21', 'cse', '2', '7.80','btech','2');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('3', 'sachin', 'sachin@sachin.com', '81dc2343rffergd433vgrsf13ed055', '100-london', '2004-02-01', 'mech', '2', '7.85','btech','2');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('4', 'virat', 'virat@virat.com', '81dcfdghdfhrertewrtv6dbd8313ed055', '103-avon', '2005-04-21', 'ee', '3', '9.80','btech','3');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('5', 'sundar', 'sundar@sundar.com', '8dsghdfghfghc20036dbd8313ed055', '6-ropar', '2004-06-23', 'cse', '3', '8.80','btech','3');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('6', 'hina', 'hina@hina.com', '81dc9bdb52d0rwqerwdbd8313ed055', '69-delhi', '2003-09-26', 'cse', '2', '7.81','btech','4');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('7', 'ritu', 'ritu@Gritu.com', '81dc9bdb52d04dc2gdgdf6dbd8313ed055', '71-ldh', '2003-01-27', 'ce', '2', '7.00','btech','4');


INSERT INTO `admin` (`admin_id`, `name`, `emailid`, `password`, role) VALUES ('1', 'sqyw', 'sqyw@sqyw.com', '81dc9bdb52d04dc20036dbd8313ed055', 'acad');
INSERT INTO `admin` (`admin_id`, `name`, `emailid`, `password`, role) VALUES ('2', 'qwsr', 'qwsr@qwsr.com', '81dc9bdb52d04dc20036dbd8313ed055', 'acad');
INSERT INTO `admin` (`admin_id`, `name`, `emailid`, `password`, role) VALUES ('3', 'qsdr', 'qsdr@qsdr.com', '81dc9bdb52d04dc2443ffefeg3545gge', 'acad');
INSERT INTO `admin` (`admin_id`, `name`, `emailid`, `password`, role) VALUES ('4', 'sdfr', 'sdfr@sdfr.com', '81dc9bdb52d0dfgdfgdfgfg8313ed055', 'acad');
INSERT INTO `admin` (`admin_id`, `name`, `emailid`, `password`, role) VALUES ('5', 'qbmg', 'qbmg@qbmg.com', 'gddfgfg8313ed0550036dbd8313ed055', 'acad');


INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('1','1',9.50,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('1','2',8.50,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('3','1',4.00,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('2','1',10.00,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('3','2',9.00,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('2','3',7.85,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('2','4',9.80,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('3','5',8.80,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('4','6',7.81,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('1','7',7.80,"");

INSERT INTO teaches (faculty_id, sec_id, year, notes) VALUES ('1','1',"2006-06-01","");
INSERT INTO teaches (faculty_id, sec_id, year, notes) VALUES ('1','2',"2006-07-28","");
INSERT INTO teaches (faculty_id, sec_id, year, notes) VALUES ('2','3',"2006-06-01","");
INSERT INTO teaches (faculty_id, sec_id, year, notes) VALUES ('1','4',"2009-12-30","");
INSERT INTO teaches (faculty_id, sec_id, year, notes) VALUES ('2','2',"2010-01-30","");

INSERT INTO assignment (sec_id, faculty_id, created_at, start_at, end_at, text, marks_total, notes) VALUES ('1','1',NOW(),DATE_ADD(NOW(), INTERVAL 3 HOUR), NOW() + INTERVAL 1 DAY, 'Sort an array in O(n) using radix sort', '30','Assg1');
INSERT INTO assignment (sec_id, faculty_id, created_at, start_at, end_at, text, marks_total, notes) VALUES ('2','1',NOW() - INTERVAL 3 DAY, NOW() - INTERVAL 2 DAY,NOW() - INTERVAL 1 DAY, 'reverse an array in O(n)', '10','Assg2');
INSERT INTO assignment (sec_id, faculty_id, created_at, start_at, end_at, text, marks_total, notes) VALUES ('2','1',NOW()- INTERVAL 2 DAY,DATE_ADD(NOW(), INTERVAL 1 HOUR), DATE_ADD(NOW(), INTERVAL 3 HOUR), 'End semester exam', '60','Assg3');
INSERT INTO assignment (sec_id, faculty_id, created_at, start_at, end_at, text, marks_total, notes) VALUES ('3','2',NOW()- INTERVAL 1 DAY,DATE_ADD(NOW(), INTERVAL 0 HOUR), DATE_ADD(NOW(), INTERVAL 3 HOUR), 'End semester exam', '100','Assg4');

INSERT INTO submission (a_id, student_id, submitted_at, text, marks_got) VALUES ('1','1', DATE_ADD(NOW(), INTERVAL 3 HOUR),'answer 1 text', '30');
INSERT INTO submission (a_id, student_id, submitted_at, text, marks_got) VALUES ('2','1', DATE_ADD(NOW(), INTERVAL 1 HOUR),'answer 2 text', '10');
INSERT INTO submission (a_id, student_id, submitted_at, text, marks_got) VALUES ('2','2', DATE_ADD(NOW(), INTERVAL 3 HOUR),'answer 2 text', '5');

INSERT INTO has_course (program, c_id, sem, branch) VALUES ('btech','1',4,'cse');
INSERT INTO has_course (program, c_id, sem, branch) VALUES ('btech','2',2,'cse');
INSERT INTO has_course (program, c_id, sem, branch) VALUES ('btech','3',4,'cse');
INSERT INTO has_course (program, c_id, sem, branch) VALUES ('phd','2',4,'cse');
INSERT INTO has_course (program, c_id, sem, branch) VALUES ('mtech','2',2,'cse');

INSERT INTO final_grade (student_id, c_id, grades) VALUES ('1','1','8.00');
INSERT INTO final_grade (student_id, c_id, grades) VALUES ('1','2','4.00');
INSERT INTO final_grade (student_id, c_id, grades) VALUES ('2','3','5.00');
INSERT INTO final_grade (student_id, c_id, grades) VALUES ('2','1','10.00');

INSERT INTO classroom (class_id, roomno, building, capacity) VALUES ('1','L01','a',200);
INSERT INTO classroom (class_id, roomno, building, capacity) VALUES ('2','C03','b',80);
INSERT INTO classroom (class_id, roomno, building, capacity) VALUES ('3','L04','c',100);
INSERT INTO classroom (class_id, roomno, building, capacity) VALUES ('4','L02','d',90);

INSERT INTO section_room(sec_id, class_id, start_time, end_time, day) VALUES ('1','1',7,8,1);
INSERT INTO section_room(sec_id, class_id, start_time, end_time, day) VALUES ('1','2',13,14,5);
INSERT INTO section_room(sec_id, class_id, start_time, end_time, day) VALUES ('2','2',7,9,2);
INSERT INTO section_room(sec_id, class_id, start_time, end_time, day) VALUES ('3','3',10,12,4);

INSERT INTO works (faculty_id, dept_id) VALUES ('1','cse');
INSERT INTO works (faculty_id, dept_id) VALUES ('2','ee');
INSERT INTO works (faculty_id, dept_id) VALUES ('3','ce');
INSERT INTO works (faculty_id, dept_id) VALUES ('4','cse');

INSERT INTO offer_course (dept_id, c_id) VALUES ('cse','1');
INSERT INTO offer_course (dept_id, c_id) VALUES ('cse','2');
INSERT INTO offer_course (dept_id, c_id) VALUES ('cse','3');
INSERT INTO offer_course (dept_id, c_id) VALUES ('ee','3');

INSERT INTO has_program (program, dept_id) VALUES ('btech','cse');
INSERT INTO has_program (program, dept_id) VALUES ('btech','ee');
INSERT INTO has_program (program, dept_id) VALUES ('btech','ce');
INSERT INTO has_program (program, dept_id) VALUES ('mtech','ce');

INSERT INTO requires (prereq_id, maincourse_id) VALUES ('1','3');

INSERT INTO requests (id, name, dob, notes) VALUES ('1','ron','2021-02-20 12:00:00', 'request for OS course.');
INSERT INTO requests (id, name, dob, notes) VALUES ('1','ron','2020-02-20 13:00:00', 'request dropping MATHS course.');
INSERT INTO requests (id, name, dob, notes) VALUES ('2','Shyam','2021-02-20 12:00:00', 'request for login access admin.');