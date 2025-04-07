import os
import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.db import models
def user_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/user/', filename)


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """This function will create normal user"""
        if not email:
            raise ValueError("Email not found")
        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.active = True
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """This function will create super user or admin user"""
        user = self.create_user(email=email, password=password, **extra_fields)
        user.staff = True
        user.admin = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    """Model for User object"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, )
    active = models.BooleanField(default=True)
    profile_picture = models.ImageField(null=True, upload_to=user_image_file_path)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        """Is the user a employee of the company?"""
        return self.admin

    @property
    def is_staff(self):
        """Is the user a staff member?"""
        return self.staff

    @property
    def is_active(self):
        """Is the user active?"""
        return self.active

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):  # Avoid re-hashing already hashed passwords
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
