from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class PersonManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório")
        if not username:
            raise ValueError("O username é obrigatório")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, email, password, **extra_fields)

class Person(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nome de usuário', max_length=30, unique=True)
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    surname = models.CharField('Sobrenome', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo?', default=True)
    is_staff = models.BooleanField('É da equipe?', default=False)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)
    github_link = models.URLField('Link do GitHub', blank=True, null=True)
    linkedin_link = models.URLField('Link do LinkedIn', blank=True, null=True)
    instagram_link = models.URLField('Link do Instagram', blank=True, null=True)

    objects = PersonManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'surname']

    def __str__(self):
        return f"{self.name} {self.surname}" if self.name or self.surname else self.username


    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['username']