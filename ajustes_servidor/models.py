from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
# Librerias.
from django.utils import timezone
from ajustes_servidor.opciones_models.opciones_models import guardar_imagen
from ajustes_servidor.opciones_models.opciones_models import Lenguajes, Niveles_Usuarios

#♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦#
# MODELO USUARIO PERZONALIZADO  
#♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦#
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El email debe ser obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True')
        return self._create_user(email, password, **extra_fields)
    
class usuario(AbstractBaseUser, PermissionsMixin):
    # Registro por defecto:
    email = models.EmailField(unique=True)
    # Datos perzonales:
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    # Datos de permisos:
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # Datos de registro:
    imagen_perfil = models.ImageField(upload_to=guardar_imagen, default="static/img/user/default.png", blank=True, null=True)
    # Configuracion de usuario:
    contenido_adulto = models.BooleanField(default=False)
    idioma = models.CharField(max_length=300, blank=True, choices=(Lenguajes), default="spanish")
    comentarios = models.BooleanField(default=True)
    nivel_usuario = models.CharField(max_length=300, blank=True, choices=(Niveles_Usuarios), default="Registrado")
    # Datos automaticos:
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    objects = CustomUserManager()
    ip_address = models.GenericIPAddressField(verbose_name='Dirección IP del usuario', blank=True, null=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    def __str__(self):
        return self.email
    def get_short_name(self):
        return self.email or self.email.split('@')[0]
    def get_full_name(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True


    