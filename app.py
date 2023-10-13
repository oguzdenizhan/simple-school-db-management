from dbmanager import DbManager
import datetime
from Student import Student
from Teacher import Teacher
class App:
    def __init__(self):
        self.db= DbManager()
    def initApp(self):
        msg= "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/Ç)"

        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == "1":
                self.displayStudents()
            elif islem =="2":
                self.addStudent()
            if islem == "3":
                self.editStudent()
            elif islem =="4":
                self.deleteStudent()
            if islem == "5":
                self.addTeacher()
            elif islem =="6":
                self.getLessonByclass()
            elif islem =="E" or islem=="Ç":
                break
    def addTeacher(self):
        branch = input("Branş: ")
        name = input("Ad: ")
        surname = input("Soyad: ")
        year = int(input("Yıl: "))
        month = int(input("Ay: "))
        day = int(input("Gün: "))
        birthday =  datetime.date(year,month,day)
        gender = input("Cinsiyet(E/K): ")

        teacher = Teacher(None,branch,name,surname,birthday,gender)
        self.db.addTeacher(teacher)

    def addStudent(self):
        self.displayClasses()
        classId= int(input("Hangi Sınıf"))
        number = input("Numara: ")
        name = input("Ad: ")
        surname = input("Soyad: ")
        year = int(input("Yıl: "))
        month = int(input("Ay: "))
        day = int(input("Gün: "))
        birthday =  datetime.date(year,month,day)
        gender = input("Cinsiyet(E/K): ")

        student = Student(None,number,name,surname,birthday,gender,classId)
        self.db.addStudent(student)
    def editStudent(self):
        classid = self.displayStudents()
        studentId = int(input("Öğrenci id: "))
        student=self.db.getStudentById(studentId)

        student[0].name = input("Ad: ") or student[0].name
        student[0].surname = input("Soyad: ") or student[0].surname
        student[0].gender = input("Cinsiyet (E/K): ") or student[0].gender
        student[0].classId = input("Sınıf: ") or student[0].classId

        year = input("Yıl ") or student[0].birthday.year
        month = input("Ay ") or student[0].birthday.month
        day = input("Gün ") or student[0].birthday.day
        student[0].birthday = datetime.date(year,month,day)

        self.db.editStudent(student[0]) 
    def getLessonByclass(self):
        self.displayClasses()
        classId= int(input("Hangi Sınıf: "))

        lessons = self.db.getLessonByClass(classId)
        print("Ders Listesi")
        for les in lessons:
            print(f"{les}")
        return classId

        for c in classes:
            print(f"{c.id}: {c.name}")
    def deleteStudent(self):
        classid = self.displayStudents()
        studentId = int(input("Öğrenci id: "))
        self.db.deleteStudent(studentId)

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f"{c.id}: {c.name}")

    def displayStudents(self):
        self.displayClasses()
        classId= int(input("Hangi Sınıf"))

        students = self.db.getStudentsByClassId(classId)
        print("Öğrenci Listesi")
        for std in students:
            print(f"{std.id}-{std.name} {std.surname}")
        return classId

app = App()
app.initApp()