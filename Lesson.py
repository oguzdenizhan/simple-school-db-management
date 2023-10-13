class Lesson:
    def __init__(self,id,name):
        if id is None:
            self.id=0
        else:
            self.id=id
        self.name = name
    @staticmethod
    def createLesson(obj):
        lesson_list = list(obj)
        liste=[]
        for i in lesson_list:
            i = list(i)
            liste.append(i)
        return liste

