import mysql.connector
from datetime import datetime 
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class
from Lesson import Lesson
class DbManager:
    def __init__(self):
        self.connection=connection
        self.cursor = connection.cursor()


    def getLessonByClass(self,classId):
        sql = "select l.name from classlesson as cl inner join lesson as l on l.id=cl.lessonId where classId=%s"  
        value=(classId,)
        
        self.cursor.execute(sql,value)
        try:
            obj=self.cursor.fetchall()
            return Lesson.createLesson(obj)
        except mysql.connector.Error as err:
            print("Hata: ",err)
    def getStudentById(self,id):
        sql ="select * from student where id = %s"
        value=(id,)
        self.cursor.execute(sql,value)
        try:
            obj=self.cursor.fetchone()
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print("Hata: ",err)


    def getStudentsByClassId(self,classId):
        sql ="select * from student where classId = %s"
        value=(classId,)
        self.cursor.execute(sql,value)
        try:
            obj=self.cursor.fetchall()
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print("Hata: ",err)
    def getClasses(self):
        sql ="select * from class"
        self.cursor.execute(sql)
        try:
            obj=self.cursor.fetchall()
            return Class.createClass(obj)
        except mysql.connector.Error as err:
            print("Hata: ",err)
    def addTeacher(self,teacher: Teacher):
        sql = "INSERT INTO teacher(branch,name,surname,birthdate,gender) VALUES (%s,%s,%s,%s,%s)"
        value = (teacher.branch, teacher.name, teacher.surname, teacher.birthday, teacher.gender)       
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi ")
        except mysql.connector.Error as err:
            print("hata ",err) 
    def addStudent(self, student: Student):

        sql = "INSERT INTO student(studentNumber,name,surname,birthdate,gender,classId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber, student.name, student.surname, student.birthday, student.gender, student.classId)       
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi ")
        except mysql.connector.Error as err:
            print("hata ",err)
    def deleteStudent(self,studentId):
        sql="delete from student where id=%s"   
        value=(studentId,)  
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt silindi ")
        except mysql.connector.Error as err:
            print("hata ",err)           
    def editStudent(self, student: Student):
        sql="update student set studentNumber=%s, name=%s,surname=%s,birthdate=%s,gender=%s,classId=%s where id = %s"
        value = (student.branch, student.name, student.surname, student.birthday, student.gender, student.classId,student.id)       
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi ")
        except mysql.connector.Error as err:
            print("hata ",err)
        
    def editTeacher(self, teacher: Teacher):
        pass
    def __del__(self):
        self.connection.close()
        print("db silindi")
        
# db = DbManager()

#get student by Id

# student=db.getStudentById(7)
# print(student[0].name)

#get students by ClassId

# students= db.getStudentsByClassId(1)
# print(students[0].name)
# print(students[1].name)

#add student
# student=db.getStudentById(7)
# student[0].name ="Veli"
# student[0].surname ="Bozar"
# student[0].studentNumber = "503"
# db.addStudent(student[0])

#edit student
# student=db.getStudentById(7)
# student[0].name ="Ahmet"
# db.editStudent(student[0])
