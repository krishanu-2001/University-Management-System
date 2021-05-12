'''
For running test file
STEPS: 

    pip install -r requirements.txt
    python test.py

FOR DETAILED COVERAGE

    coverage run --source models -m unittest discover && coverage report
    coverage html


TestCase Details - 
1. Home section
2. Admin section
3. Student section
4. Faculty section
'''

import flask
import unittest
import flask_testing
from app import app
import data_requests
from flask import json

''' Section 1 - Home Section '''
class TestHome(flask_testing.TestCase):
    def create_app(self):
        return app

    def testHomepage(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('index.html')

    def testGetStartedPage(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/getStarted')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('getStarted.html')
    
    def testStudentLogin(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/login/student')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student/login.html')
    
    def testAdminLogin(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/login/admin')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/login.html')
    
    def testFacultyLogin(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/login/faculty')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('faculty/login.html')


#---------------------------------------------------------------------#


''' section 2 - Admin Section '''

class TestAdmin(flask_testing.TestCase):
    def create_app(self):
        return app

    def testHomepage(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('index.html')

    def testAdminLoginGet(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/login/admin')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/login.html')

    def testAdminLoginPost(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done

# Admin-Student

    def testAdmin_logged_out(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login not done
            response= TestClient.get('/admin/dashboard')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_list')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/add_student')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_list_edit')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/edit-student/12')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_view/12')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/modal_update')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_excel')
            self.assert_template_used('error.html')
            
            response= TestClient.get('/admin/add_course')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_list')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_edit/1')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_delete')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_excel')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_sem_assign')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_sem_edit/1')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_student_assign')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_student_add/2')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_student_delete/2')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_student_assign')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_sem_delete')
            self.assert_template_used('/faculty_panel/error_404.html')

            response= TestClient.get('/admin/add_faculty')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/faculty_list')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/faculty_view/2')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/faculty_list_edit')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/edit-faculty/2')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/delete-faculty')
            self.assert_template_used('error.html')

            response= TestClient.get('/admin/department_list')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/add_department')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/department_list_edit')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/edit-department/2')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/delete-department')
            self.assert_template_used('error.html')

    def testAdmin_partial_logged_out(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/admin/dashboard')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_list')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/add_student')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_list_edit')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/edit-student/12')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_view/12')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/modal_update')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_excel')
            self.assert_template_used('error.html')
            
            response= TestClient.get('/admin/add_course')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_list')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_edit/1')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_delete')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_excel')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_sem_assign')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_sem_edit/1')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_student_assign')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_student_add/2')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_student_delete/2')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_student_assign')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/course_sem_delete')
            self.assert_template_used('/faculty_panel/error_404.html')

            response= TestClient.get('/admin/add_faculty')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/faculty_list')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/faculty_view/2')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/faculty_list_edit')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/edit-faculty/2')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/delete-faculty')
            self.assert_template_used('error.html')

            response= TestClient.get('/admin/department_list')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/add_department')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/department_list_edit')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/edit-department/2')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/delete-department')
            self.assert_template_used('error.html')

    def testAdminDashboard(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/dashboard')
            self.assert_template_used('admin/index.html')
    
    def testAdminStudent_list(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/student_list')
            self.assert_template_used('/admin/students_list.html')

    def testAdminStudent_add(self):
        data = data_requests.admin_login
        new_student = data_requests.admin_student_add
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            # get
            response= TestClient.get('/admin/add_student')
            self.assert_template_used('admin/add-student.html')
            # post
            response= TestClient.post('/admin/add_student', data = new_student)
            self.assert_template_used('admin/add-student.html')

    def testAdminStudent_list_edit(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/student_list_edit')
            self.assert_template_used('/admin/student.html')

    def testAdminEditStudent(self):
        data = data_requests.admin_login
        student_edit = data_requests.admin_student_edit
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/edit-student/1')
            self.assert_template_used('/admin/student-edit.html')
            # post
            response= TestClient.post('/admin/edit-student/12', data = student_edit)
            self.assert_template_used('/admin/student-edit.html')

    def testAdminStudentDetail(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/student_view/1')
            self.assert_template_used('admin/student-detail.html')

    def testAdminmodal_update(self):
        data = data_requests.admin_login
        modal_data = data_requests.admin_modal_next
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/modal_update')
            self.assert_template_used('/admin/modal_update.html')
            # post
            response= TestClient.post('/admin/modal_update', data = modal_data)
            self.assert_template_used('/admin/modal_update.html')

    def testAdminStudentExcel(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/student_excel')
            self.assertEqual(response.status_code, 200)

    def testAdminStudent_delete(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            # deleting student 12 which was added before
            response= TestClient.get('/admin/delete-student/12')
            self.assertEqual(response.status_code, 302)


# Admin-Course

    def testAdminCourse_add(self):
        data = data_requests.admin_login
        new_course = data_requests.admin_course_add
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/add_course')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/add_course.html')
            # post
            response= TestClient.post('/admin/add_course', data = new_course)
            self.assertEqual(response.status_code, 302)
            self.assert_template_used('admin/add_course.html')

    def testAdminCourse_list(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/course_list')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('/admin/course_list.html')
            
    def testAdminCourse_edit(self):
        data = data_requests.admin_login
        edit_course = data_requests.admin_course_edit
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/course_edit/3')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('/admin/edit_course.html')
            # post
            response = TestClient.post('/admin/course_edit/3', data = edit_course)
            self.assertEqual(response.status_code, 302)
            self.assert_template_used('/admin/edit_course.html')
            
    def testAdminCourse_delete(self):
        data = data_requests.admin_login
        delete_course = data_requests.admin_course_delete
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.post('/admin/course_delete', data = delete_course)
            self.assertEqual(response.status_code, 302)
            
    def testAdminCourse_excel(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/course_excel')
            self.assertEqual(response.status_code, 200)
            
    def testAdminCourse_sem_assign(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/course_sem_assign')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('/admin/course_section_assign.html')
            
    def testAdminCourse_sem_edit(self):
        data = data_requests.admin_login
        sem_assign = data_requests.admin_course_sem_assign
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/course_sem_edit/2')
            self.assertEqual(response.status_code, 200)
            # post
            response= TestClient.post('/admin/course_sem_edit/2', data = sem_assign)
            self.assertEqual(response.status_code, 302)
            
    def testAdminCourse_sem_delete(self):
        data = data_requests.admin_login
        del_course_sem = data_requests.admin_course_sem_delete

        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/course_sem_delete/12')
            self.assertEqual(response.status_code, 200)
            # post
            response= TestClient.post('/admin/course_sem_delete/12', data = del_course_sem)
            self.assertEqual(response.status_code, 302)

    def testAdminCourse_student_assign(self):
        data = data_requests.admin_login
        new_course = data_requests.admin_course_add
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/course_student_assign')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('/admin/course_student_assign.html')

    def testAdminCourse_student_add(self):
        data = data_requests.admin_login
        course_student_data = data_requests.admin_course_student_assign
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/course_student_add/2')
            self.assertEqual(response.status_code, 200)
            # post
            response= TestClient.post('/admin/course_student_add/2', data = course_student_data)
            self.assertEqual(response.status_code, 302)

    def testAdminCourse_student_delete(self):
        data = data_requests.admin_login
        course_student_del = data_requests.admin_course_student_delete
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/course_student_delete/2')
            self.assertEqual(response.status_code, 200)
            # POST
            response= TestClient.post('/admin/course_student_delete/2', data = course_student_del)
            self.assertEqual(response.status_code, 302)


# requests

    def testAdmin_requests(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/all_requests')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('/admin/inbox.html')

    def testAdmin_completed_requests(self):
        data = data_requests.admin_login
        accept_message = data_requests.admin_all_requests
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/accepted_requests')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('/admin/inbox.html')
            # post
            response= TestClient.post('/admin/accepted_requests', data = accept_message)
            self.assertEqual(response.status_code, 302)


# faculty

    def testAdminFaculty_add(self):
        data = data_requests.admin_login
        new_faculty = data_requests.admin_faculty_add
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/add_faculty')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/add-faculty.html')
            # post
            response= TestClient.post('/admin/add_faculty', data = new_faculty)
            self.assertEqual(response.status_code, 302)

    def testAdminFaculty_list(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/faculty_list')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/faculty_list.html')

    def testAdminFaculty_view(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/faculty_view/2')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/faculty-detail.html')

    def testAdminFaculty_list_edit(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/faculty_list_edit')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('/admin/faculty.html')

    def testAdminFaculty_edit(self):
        data = data_requests.admin_login
        admin_fac_edit = data_requests.admin_faculty_edit
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/edit-faculty/2')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('/admin/edit-faculty.html')
            # post
            response= TestClient.post('/admin/edit-faculty/2', data = admin_fac_edit)
            self.assertEqual(response.status_code, 302)

    def testAdminFaculty_delete(self):
        data = data_requests.admin_login
        admin_fac_delete = data_requests.admin_faculty_delete
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/delete-faculty')
            self.assertEqual(response.status_code, 200)
            response= TestClient.post('/admin/delete-faculty', data=json.dumps(dict(id='12')),
                       content_type='application/json')
            self.assertEqual(response.status_code, 200)


# department

    def testAdminDepartment_list(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/department_list')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/department_list.html')

    def testAdminDepartment_add(self):
        data = data_requests.admin_login
        new_dept = data_requests.admin_department_add
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/add_department')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/add-department.html')
            # post
            response= TestClient.post('/admin/add_department', data = new_dept)
            self.assertEqual(response.status_code, 302)

    def testAdminDepartment_list_edit(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/department_list_edit')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('/admin/department.html')

    def testAdminDepartment_edit(self):
        data = data_requests.admin_login
        admin_dept_edit = data_requests.admin_department_edit
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/edit-department/cse')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('/admin/edit-department.html')
            # post
            response= TestClient.post('/admin/edit-department/cse', data = admin_dept_edit)
            self.assertEqual(response.status_code, 302)

    def testAdminDepartment_delete(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.post('/admin/delete-department', data=json.dumps(dict(id='bio')),
                       content_type='application/json')
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()