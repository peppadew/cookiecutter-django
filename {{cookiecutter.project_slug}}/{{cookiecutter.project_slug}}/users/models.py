from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.utils import timezone


TITLE_CHOICES = (
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms')
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    title = models.CharField(
        max_length=8,
        choices=TITLE_CHOICES,
        blank=True,
        null=True
    )
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)

    company = models.CharField(max_length=32, blank=True, null=True)
    mobile_number = models.CharField(max_length=16, blank=True, null=True)
    gender = models.CharField(
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
        ),
        max_length=8,
        blank=True,
        null=True
    )
    city = models.CharField(max_length=255, blank=True, null=True)

    is_staff = models.BooleanField(
        default=False,
        help_text=('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return '%s %s'.strip() % (self.first_name, self.last_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
