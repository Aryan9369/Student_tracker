from django.db import models

class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()

    def __str__(self):
        return self.name

class tasks(models.Model):
    student=models.ForeignKey(student,on_delete=models.CASCADE,related_name='tasks')
     #related name like a attribute available for each student
     #student.tasks.all() using this you can get all task related to that student , student here is an object or a representing a single row of student table
    title=models.CharField(max_length=100)
    completed=models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

