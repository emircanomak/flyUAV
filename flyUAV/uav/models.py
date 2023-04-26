from django.db import models

# Create your models here.

class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class Model(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"
    
class ihaModel(models.Model):
    id=models.AutoField(primary_key=True)
    model=models.ForeignKey(Model,max_length=40,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,max_length=40,on_delete=models.CASCADE)
    weight=models.PositiveBigIntegerField(default=0)
    category=models.ForeignKey(Category,max_length=50,on_delete=models.CASCADE)
    date=models.DateField()
    image=models.URLField(default="")

