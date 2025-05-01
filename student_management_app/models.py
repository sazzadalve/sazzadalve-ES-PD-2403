from django.db import models


# class Hobby(models.Model):
#     name = models.CharField(max_length = 50)


#     def __str__(self):
#         return f'{self.name}"s Profile'

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}"s Profile'

class Result(models.Model):
    marks = models.FloatField()
    Subject = models.ForeignKey(Subject, on_delete= models.CASCADE)

class Student(models.Model):

    GENDER = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("third", "third"),
    ]

    RELIGION = [
        ("Islam", "Islam"),
        ("Hindu", "Hindu"),
        ("Cristian", "Cristian"),
        ("Buddho", "Buddho"),
    ]

    #prime_id = models.AutoField(primary_key=True, unique=True, editable=False, blank=False,null=False, default='101')
    name            = models.CharField(max_length=100)
    email           = models.EmailField(max_length=100)
    image           = models.ImageField(upload_to='images/', default= 'def.png', blank=True)
    father_name     = models.CharField(max_length=100)
    mother_name     = models.CharField(max_length=100)
    religion        = models.CharField(choices=RELIGION, max_length=10)
    gender          = models.CharField(choices=GENDER, max_length=10)
    date_of_birth   = models.DateField()
    roll            = models.IntegerField()
    city            = models.CharField(max_length=10)
    is_Bangladeshi  =  models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    age             = models.PositiveBigIntegerField()
    result          = models.ManyToManyField(Result)
    #hobby           = models.OneToOneField(Hobby, on_delete=models.CASCADE, null=True, blank=True)
    Subject         = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.name}"s Profile'