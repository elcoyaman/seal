from django.test import TestCase
from seal.model.course import Course
from seal.model.student import Student
from seal.model.practice import Practice

class CourseIntegrationTest(TestCase):
    def testCourseUniqueName(self):
        """
        I will try to create a Course with the same name as another and expect a failure
        """
        aName = '2012-2C'
        Course.objects.get_or_create(name=aName)
        course = Course.objects.get(name=aName)
        self.assertEqual(course.name, aName, "course's expected name was '" + aName + "' but actual was '" + course.name + "'")
    
    def testCourseAddStudent(self):
        """
        I will take a course and add a student to it. Then, try to get it from the database.
        """
        course_name = '2012-1C'
        aCourse = Course.objects.get_or_create(name=course_name)[0]
        aStudent = Student.objects.get_or_create(name="Juan Perez", uid='1234', email = "email@pagnia.com.ar")[0]
        aCourse.add_student(aStudent)
        aCourse.save()
        
        aCourse = Course.objects.get(name=course_name)
        self.assertTrue(aStudent in aCourse.get_students(), 'Set, expected to contain Juan Perez')
    
    def testCourseDeleteStudent(self):
        """
        I Will add a Student from a Course and verify it contains the student
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')[0]
        aStudent = Student.objects.get_or_create(name="Juan Perez", uid='1234', email = "email@pagnia.com.ar")[0]
        aCourse.add_student(aStudent)
        aCourse.save()
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertTrue(aStudent in aCourse.get_students(), 'Set, expected to contain Juan Perez')
        
        aCourse.remove_student(aStudent)
        aCourse.save()
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertFalse(aStudent in aCourse.get_students(), 'Set, expected to have no Juan Perez student')
    
    def testCourseAddAssignment(self):
        """
        I will take a course and add an assignment to it. Then, try to get it from the database.
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')[0]
        assignment = Practice.objects.get_or_create(uid="LPC", course=aCourse, deadline="2012-12-01")[0]
        aCourse = Course.objects.get(name='2012-1C')
        self.assertTrue(assignment in aCourse.get_practices(), 'Set, expected to contain LPC')
    
    def testCourseDeleteAssignment(self):
        """
        I will take a course and remove an assignment from it. Then, try to get it from the database.
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')[0]
        assignment = Practice.objects.get_or_create(uid="LPC", course=aCourse, deadline="2012-12-01")[0]
        self.assertTrue(assignment in aCourse.get_practices(), 'Set, expected to contain LPC')
        assignment.delete()
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertFalse(assignment in aCourse.get_practices(), 'Set, not expected to contain LPC')
    
