from flask import *
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_mail import Mail
from flask_mail import Message
from werkzeug.utils import html

# models
import models.student as student
import models.admin as admin
import models.faculty as faculty
import models.auth as auth

app = Flask(__name__)
CORS(app)

app.config.from_object('config.DevConfig')

mysql = MySQL(app)
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/getStarted', methods=['GET', 'POST'])
def getStarted():
    return render_template('getStarted.html')

# auth start
app.add_url_rule('/login/<user>', view_func=auth.login, methods=['GET','POST'])
app.add_url_rule('/logout', view_func=auth.logout, methods=['GET','POST'])
app.add_url_rule('/resetpassword/<user>', view_func=auth.resetpassword, methods=['GET','POST'])
app.add_url_rule('/reset_password/<user>/<token>', view_func=auth.reset_token,  methods=['GET','POST'])
# auth end



# department start

@app.route('/department', methods=['GET', 'POST'])
def department():
    return render_template('department/dashboard.html')

@app.route('/department/cse', methods=['GET', 'POST'])
def cse():
    return render_template('department/cse.html')

@app.route('/department/cse/program_offered', methods=['GET', 'POST'])
def cse_program_offered():
    return render_template('department/cse_program_offered.html')

@app.route('/department/cse/course_offered', methods=['GET', 'POST'])
def cse_course_offered():
    return render_template('department/cse_course_offered.html')

@app.route('/department/cse/faculty_list', methods=['GET', 'POST'])
def cse_faculty_list():
    return render_template('department/cse_faculty_list.html')
    
@app.route('/department/cse/student_list', methods=['GET', 'POST'])
def cse_student_list():
    return render_template('department/cse_student_list.html')

@app.route('/department/instructor_profile_view', methods=['GET', 'POST'])
def faculty_profile_view():
    return render_template('department/my_instructor_profile_view.html')
# department end


# student start
app.add_url_rule('/student/dashboard', view_func=student.student_dashboard, methods=['GET','POST'])
app.add_url_rule('/student/profile', view_func=student.student_profile, methods=['GET','POST'])
app.add_url_rule('/student/setting', view_func=student.student_setting, methods=['GET','POST'])
app.add_url_rule('/student/enrolled-courses', view_func=student.student_enrolled_courses, methods=['GET','POST'])
app.add_url_rule('/student/my-courses', view_func=student.student_my_courses, methods=['GET','POST'])
app.add_url_rule('/student/grades', view_func=student.student_grades, methods=['GET','POST'])
app.add_url_rule('/student/gradesheet', view_func=student.student_gradesheet, methods=['GET','POST'])
app.add_url_rule('/student/placement-offers', view_func=student.student_placement_offers, methods=['GET','POST'])
app.add_url_rule('/student/submit-assignment', view_func=student.student_submit_assignment, methods=['GET','POST'])
app.add_url_rule('/student/submit-assign/<a_id>', view_func=student.student_submit_assign, methods=['GET','POST'])

# student end

# faculty start
app.add_url_rule('/faculty/dashboard', view_func=faculty.faculty_dashboard, methods=['GET','POST'])
app.add_url_rule('/faculty/setting', view_func=faculty.faculty_setting, methods=['GET','POST'])
app.add_url_rule('/faculty/profile', view_func=faculty.faculty_profile, methods=['GET','POST'])
app.add_url_rule('/faculty/changepassword', view_func=faculty.faculty_change_password, methods=['POST'])
app.add_url_rule('/faculty/courses', view_func=faculty.faculty_course, methods=['GET','POST'])
app.add_url_rule('/faculty/create_new_assignment', view_func=faculty.faculty_create_new_assignment, methods=['GET','POST'])
app.add_url_rule('/faculty/grade_assignment', view_func=faculty.select_section_for_assignment, methods=['GET','POST'])
app.add_url_rule('/faculty/grade_assignment/<sec_id>', view_func=faculty.select_assignment_for_grade, methods=['GET','POST'])
app.add_url_rule('/faculty/grade_assignment/<sec_id>/<a_id>', view_func=faculty.select_student_for_grade, methods=['GET','POST'])
app.add_url_rule('/faculty/grade_assignment/submission/<submission_id>', view_func=faculty.faculty_assignment_grade_submission, methods=['GET','POST'])
# faculty end

# admin start
app.add_url_rule('/admin/dashboard', view_func=admin.admin_dashboard, methods=['GET','POST'])
app.add_url_rule('/admin/profile', view_func=admin.admin_profile, methods=['GET','POST'])

# admin student start
app.add_url_rule('/admin/add_student', view_func=admin.admin_add_student, methods=['GET','POST'])
app.add_url_rule('/admin/student_list', view_func=admin.admin_student_list, methods=['GET','POST'])
app.add_url_rule('/admin/edit-student/<student_id>', view_func=admin.admin_student_edit, methods=['GET','POST'])
app.add_url_rule('/admin/student_view/<student_id>', view_func=admin.admin_student_view, methods=['GET','POST'])
app.add_url_rule('/admin/delete-student/<student_id>', view_func=admin.admin_student_delete, methods=['GET','POST'])
app.add_url_rule('/admin/student_list_edit', view_func=admin.admin_student_list_edit, methods=['GET','POST'])
app.add_url_rule('/admin/student_excel', view_func=admin.ExcelDownload_student, methods=['GET','POST'])
app.add_url_rule('/admin/modal_update', view_func=admin.admin_modal_update, methods=['GET','POST'])
# admin student end

# admin faculty start 
app.add_url_rule('/admin/add_faculty', view_func=admin.admin_add_faculty, methods=['GET','POST'])
app.add_url_rule('/admin/faculty_list', view_func=admin.admin_faculty_list, methods=['GET','POST'])
app.add_url_rule('/admin/faculty_view/<faculty_id>', view_func=admin.admin_faculty_view, methods=['GET','POST'])
app.add_url_rule('/admin/faculty_list_edit', view_func=admin.admin_faculty_list_edit, methods=['GET','POST'])
app.add_url_rule('/admin/edit-faculty/<faculty_id>', view_func=admin.admin_faculty_edit, methods=['GET','POST'])
app.add_url_rule('/admin/delete-faculty', view_func=admin.admin_faculty_delete, methods=['GET','POST'])
app.add_url_rule('/admin/faculty_excel', view_func=admin.ExcelDownload_faculty, methods=['GET','POST'])
# admin faculty end

# admin department start 
app.add_url_rule('/admin/department_list', view_func=admin.admin_department_list, methods=['GET','POST'])
app.add_url_rule('/admin/add_department', view_func=admin.admin_add_department, methods=['GET','POST'])
app.add_url_rule('/admin/department_list_edit', view_func=admin.admin_department_list_edit, methods=['GET','POST'])
app.add_url_rule('/admin/edit-department/<dept_id>', view_func=admin.admin_department_edit, methods=['GET','POST'])
app.add_url_rule('/admin/delete-department', view_func=admin.admin_department_delete, methods=['GET','POST'])
app.add_url_rule('/admin/dept_excel', view_func=admin.ExcelDownload_department, methods=['GET','POST'])
# admin department end

app.add_url_rule('/admin/add_course', view_func=admin.admin_add_course, methods=['GET','POST'])
app.add_url_rule('/admin/course_list', view_func=admin.admin_course_list, methods=['GET','POST'])
app.add_url_rule('/admin/course_edit/<c_id>', view_func=admin.admin_course_edit, methods=['GET','POST'])
app.add_url_rule('/admin/course_delete', view_func=admin.admin_course_delete, methods=['GET','POST'])
app.add_url_rule('/admin/course_excel', view_func=admin.ExcelDownload_course, methods=['GET','POST'])
app.add_url_rule('/admin/course_sem_assign', view_func=admin.admin_course_sem_assign, methods=['GET','POST'])
app.add_url_rule('/admin/course_sem_edit/<c_id>', view_func=admin.admin_course_sem_edit, methods=['GET','POST'])
app.add_url_rule('/admin/course_sem_delete/<c_id>', view_func=admin.admin_course_sem_delete, methods=['GET','POST'])
app.add_url_rule('/admin/course_student_assign', view_func=admin.admin_course_student_assign, methods=['GET','POST'])
app.add_url_rule('/admin/course_student_add/<student_id>', view_func=admin.admin_course_student_add, methods=['GET','POST'])
app.add_url_rule('/admin/course_student_delete/<student_id>', view_func=admin.admin_course_student_delete, methods=['GET','POST'])

app.add_url_rule('/admin/all_requests', view_func=admin.admin_inbox, methods=['GET','POST'])
app.add_url_rule('/admin/accepted_requests', view_func=admin.admin_accepted_requests, methods=['GET','POST'])
# admin end  

# ERROR
@app.errorhandler(404)
def not_found(e):
    return render_template("/faculty_panel/error_404.html"),404


if __name__ == '__main__':
    flag = 0
    app.run(host='0.0.0.0', port=5000, debug=True)