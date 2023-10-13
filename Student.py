class Student:
    def __init__(self,id,studentNumber,name,surname,birthdate,gender,classId):
        if id is None:
            self.id=0
        else:
            self.id=id
        self.studentNumber = studentNumber
        if len(name)>45:
            raise Exception("name için max 45 karakter giriniz")
        self.name = name
        self.surname = surname
        self.birthday = birthdate
        self.gender = gender
        self.classId = classId
    @staticmethod
    def createStudent(obj):
        list=[]
        if isinstance(obj,tuple): #gelen obje tuple ise
            
            list.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return list