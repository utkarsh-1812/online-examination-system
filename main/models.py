from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager
from django.core.validators import RegexValidator
from django.utils import timezone
import uuid
# Create your models here.

class NewUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)                  #self.normalize_email(email).lower
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_teacher', True)
        extra_fields.setdefault('is_student', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)



#class
class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """
    def to_python(self, value):
        """
        Convert email to lowercase.
        """
        value = super(LowercaseEmailField, self).to_python(value)
        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):
            return value.lower()
        return value


class User_new(AbstractUser):

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'Name',]

    # email = LowercaseEmailField(_('email address'), unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # if you require phone number field in your project
    phone_regex = RegexValidator(
        regex=r'^\d{10}$', message="phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[
                             phone_regex], blank=True, null=True)  # you can set it unique = True
    objects = NewUserManager()
    # is_customer = models.BooleanField(default=True)
    # is_seller = models.BooleanField(default = False)

    Name = models.CharField(max_length=255)
    email = LowercaseEmailField(_('email address'),primary_key=True, unique=True)
    User_ID = models.CharField(unique=True, max_length=100,default=uuid.uuid4().hex)
    Institute_ID = models.IntegerField(null=True)
    Institute_Name = models.CharField(max_length=255, blank=True, null=True)
    # Password = models.CharField(max_length=30)
    # object = StudentManager
    student_prof = models.ForeignKey('student.Student',null=True,on_delete=models.CASCADE)
    teacher_prof = models.ForeignKey('teacher.Teacher',null=True,on_delete=models.CASCADE)

    def __str__(self):
        return str((self.User_ID, self.Name,self.student_prof_id))
