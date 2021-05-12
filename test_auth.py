import flask
import unittest
import flask_testing
from flask import *
from app import app
import data_requests


class TestAuth(flask_testing.TestCase):
    def create_app(self):
        return app

    def testHomepage(self):
        with app.test_client() as TestClient:
            response = TestClient.get('/')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('index.html')

    def testFacultyLoginPost(self):
        data1 = data_requests.faculty_login1
        data2 = data_requests.faculty_login2
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data1)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done

            # invalid login
            response = TestClient.post('/login/faculty', data=data2)
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('faculty/login.html')

    def testAdminLoginPost(self):
        data1 = data_requests.faculty_login1
        data2 = data_requests.faculty_login2
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/admin', data=data1)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done

            # invalid login
            response = TestClient.post('/login/admin', data=data2)
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/login.html')

    def testStudentLoginPost(self):
        data1 = data_requests.faculty_login1
        data2 = data_requests.faculty_login2
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/student', data=data1)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done

            # invalid login
            response = TestClient.post('/login/student', data=data2)
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student/login.html')

    def testInvalidUserLoginPost(self):
        data1 = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/abc', data=data1)
            self.assertEqual(response.status_code, 400)

    def testLogout(self):
        data1 = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/student', data=data1)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            # now logout
            response = TestClient.post('/logout')
            self.assert_template_used('index.html')
            self.assert_context("flash", "Logged out successfully!")

    def testResetPasswordGet(self):
        with app.test_client() as TestClient:
            # student
            response = TestClient.get('/resetpassword/student')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('resetrequest.html')

            # admin
            response = TestClient.get('/resetpassword/admin')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('resetrequest.html')

            # faculty
            response = TestClient.get('/resetpassword/faculty')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('resetrequest.html')

    def testResetPasswordPost(self):
        data1 = {'user_id': '1'}
        data2 = {'user_id': '123'}
        with app.test_client() as TestClient:
            # student
            response = TestClient.post('/resetpassword/student', data=data1)
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student/login.html')
            self.assert_context(
                "flash", "Reset link has been sent to your registered Email.")

            response = TestClient.post('/resetpassword/student', data=data2)
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('resetrequest.html')
            self.assert_context("flash", "Invalid Username")

            # admin
            response = TestClient.post('/resetpassword/admin', data=data1)
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/login.html')
            self.assert_context(
                "flash", "Reset link has been sent to your registered Email.")

            response = TestClient.post('/resetpassword/admin', data=data2)
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('resetrequest.html')
            self.assert_context("flash", "Invalid Username")

            # faculty
            response = TestClient.post('/resetpassword/faculty', data=data1)
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('faculty/login.html')
            self.assert_context(
                "flash", "Reset link has been sent to your registered Email.")

            response = TestClient.post('/resetpassword/faculty', data=data2)
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('resetrequest.html')
            self.assert_context("flash", "Invalid Username")

    def testResetTokenGet(self):
        data1 = {'user_id': '1'}
        with app.test_client() as TestClient:
            # student
            response = TestClient.get('/resetpassword/student/abc')
            self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
