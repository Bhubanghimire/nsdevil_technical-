from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an Email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    profile = models.ImageField(upload_to="profile", null=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email Address")
    full_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, choices=CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=20, default="")
    added_by_admin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_student(self):
        if hasattr(self, 'student'):
            return True
        return False

    @property
    def is_teacher(self):
        if hasattr(self, 'teacher'):
            return True
        return False

    class Meta:
        verbose_name_plural = "USER"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    class_id = models.ForeignKey("info.Class", on_delete=models.CASCADE, default=1)
    USN = models.CharField(primary_key='True', max_length=100)

    def __str__(self):
        return str(self.user)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dept = models.ForeignKey("info.Dept", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.user)
