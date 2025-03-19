from django.db import models
import uuid
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
    
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class MasterActivity(models.Model):
    Type= models.CharField(max_length=255)
    Subject= models.CharField(max_length=255)
    Comment= models.TextField(max_length=500)
    IsDeleted= models.BooleanField(default=False)
    AssignedUser= models.CharField(max_length=255)
    CreatedBy= models.CharField(max_length=255)
    CreatedDate= models.DateField(auto_now_add=True)
    ModifiedBy= models.CharField(max_length=255,null=True,)
    ModifiedDate= models.DateField(auto_now=True)
    DueDate= models.DateField()
    ActivityType= models.CharField(max_length=255)

    def __str__(self):
        return self.Subject
    

class MemberDetails(models.Model):
    MemberUUID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    MemberID = models.CharField(max_length=255)
    MemberName = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    MemberPhone = models.CharField(max_length=255)
    MemberEmail = models.CharField(max_length=255)
    MemberAddress = models.CharField(max_length=255)
    MemberType=models.CharField(max_length=255)
    MemberScore=models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.MemberName
class Loan(models.Model):
    LoanType=models.CharField(max_length=255)
    LoanPassingOfficer=models.CharField(max_length=255)
    LoanAmount=models.DecimalField(decimal_places=3,max_digits=100)
    LoanTenure=models.DecimalField(decimal_places=2,max_digits=4)
    InterestRate=models.DecimalField(decimal_places=2,max_digits=5)
    AmountRepayed=models.DecimalField(decimal_places=2,max_digits=100)
    Member=models.CharField(max_length=50)

    def __str__(self):
        return self.LoanType

class Offer(models.Model):
    Name=models.CharField(max_length=255)
    percentage=models.DecimalField(decimal_places=2,max_digits=4)
    Bonus=models.DecimalField(decimal_places=2,max_digits=4)
    ExpiryDate=models.DateField()
    FromDate=models.DateField(auto_now_add=True)
    ToDate=models.DateField()
    Member=models.CharField(max_length=50)

    def __str__(self):
        return self.Name