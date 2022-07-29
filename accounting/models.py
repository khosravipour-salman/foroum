from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class CustomManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=CustomManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        u = self.create_user(
        	email,
        	password=password,
		)
        u.is_active = True
        u.is_admin = True
        u.is_staff = True
        u.admin = True
        u.is_superuser = True 

        u.save(using=self._db)
        return u



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
	)
    phone_number = models.IntegerField(null=True, blank=True)
    bio = models.CharField(max_length=32, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
	
    objects = CustomManager()

    def __str__(self):
    	return self.email