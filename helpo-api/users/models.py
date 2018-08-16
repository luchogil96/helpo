from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from decouple import config
from hashlib import sha256
from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.models import IndexedTimeStampedModel
import requests

class Profile(models.Model):
    usuario = models.OneToOneField('User')

    class Meta:
        abstract = True

class Imagen(models.Model):
    isExternal = models.BooleanField()
    url = models.TextField()    

class RubroOrganizacion(models.Model):
    # nombre deberia ser Unique=True, pero me da problemas en el serializer para hacer update
    # TODO: Ver como arreglar eso, por ahora workaround -> Sacar Unique=True
    nombre = models.CharField(max_length=100)

class Ubicacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    notas = models.CharField(max_length=140, null=True)    

class OrganizacionProfile(Profile):
    verificada = models.BooleanField(default=False)
    telefono = models.BigIntegerField(blank=True, null=True)
    cuit = models.BigIntegerField(blank=True, null=True)
    rubro = models.ForeignKey(RubroOrganizacion, on_delete=models.SET_NULL, blank=True, null=True)
    avatar = models.ForeignKey(Imagen, on_delete=models.SET_NULL, blank=True, null=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL,blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

class EmpresaProfile(Profile):
    telefono = models.BigIntegerField(null=True)
    cuit = models.BigIntegerField(blank=True, null=True)
    rubro = models.ForeignKey(RubroOrganizacion, on_delete=models.SET_NULL, blank=True, null=True)
    avatar = models.ForeignKey(Imagen, on_delete=models.SET_NULL, blank=True, null=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL,blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

class UserManager(BaseUserManager):

    def create_user(self, email, nombre, password, user_type, **kwargs):
        user = self.model(email=self.normalize_email(email), nombre=nombre, user_type=user_type)
        user.set_password(password)
        user.save(using=self._db)

        avatar = Imagen.objects.get(id=1)
        
        if user_type == 1:
            profile = OrganizacionProfile.objects.create(usuario=user, avatar=avatar)
        elif user_type == 2:
            profile = VoluntarioProfile.objects.create(usuario=user, apellido=kwargs["apellido"], avatar=avatar)
        else:
            profile = EmpresaProfile.objects.create(usuario=user, avatar=avatar)
        self.send_confirmation_email(user)
        
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def send_confirmation_email(self, user):
        str_to_encode = str(user.id) + user.email
        str_encoded = str_to_encode.encode('utf-8')
        uncutbash = str(sha256(str_encoded))
        bash = uncutbash[22:36]
        self.create_user_verification(user, bash)

        mail_from = "registro@helpo.com.ar"
        subject = "Verifique su registro en Helpo"
        url_confirmation = '%s/#/confirmMail/%s' % (config('URL_CLIENT', default='localhost:3000'), bash)
        content = '<a href=\\"%s\\">Confirme su cuenta haciendo click aqu&iacute;</a>' % (url_confirmation)


        url = "https://mail.zoho.com/api/accounts/%s/messages" % (config('ZOHO_ACCOUNT_ID'))
        payload = "{\n \"fromAddress\": \"%s\",\n \"toAddress\": \"%s\",\n \"subject\": \"%s\",\n \"content\": \"%s\"\n}" \
                    % (mail_from, user.email, subject, content)
        headers = {
            'Authorization': config('ZOHO_AUTH_TOKEN'),
            'Content-Type': "application/json"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        print("Enviando mail a %s response code: %s" % (user.email, response.status_code))

    def create_user_verification(self, user, token):
        UserVerification.objects.create(usuario=user, verificationToken=token)

class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    USER_TYPE_CHOICES = (
        (0, 'other'),
        (1, 'organizacion'),
        (2, 'voluntario'),
        (3, 'empresa')
    )
    nombre = models.CharField(max_length=140)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    is_confirmed = models.BooleanField(
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'user_type']

    def get_full_name(self):
        return self.nombre

    def get_short_name(self):
        return self.nombre

    def __str__(self):
        return self.email
    
    def validate_mail(self, token):        
        uv_object = UserVerification.objects.get(usuario=self)
        if (uv_object.verificationToken == token):
            self.is_confirmed=True
            self.save()
            uv_object.delete()
            return True
        return False

class VoluntarioProfile(Profile):
    sexo = models.TextField(blank=True, null=True)
    apellido = models.CharField(max_length=140, default="no apellido")
    telefono = models.BigIntegerField(blank=True, null=True)
    dni = models.BigIntegerField(blank=True, null=True)
    avatar = models.ForeignKey(Imagen, on_delete=models.SET_NULL, blank=True, null=True)
    gustos = models.TextField(blank=True, null=True)
    habilidades = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, related_name='perfil', on_delete=models.CASCADE)

class UserVerification(IndexedTimeStampedModel):
    usuario = models.OneToOneField('User')
    verificationToken = models.CharField(max_length=2000)


class Profile(models.Model):
    usuario = models.OneToOneField(User)

    class Meta:
        abstract = True

"""
AppValues se va utilizar como diccionario clave-valor para
almacenar valores generales.

Precaucion: Asegurarse que la entrada este inicializada (campo creado en BD),
por ahora hay que hacerlo manual

Estructura (Mantener actualizado para saber que contiene):
    imgurAccessToken: [TOKEN]
    imgurRefreshToken: [TOKEN]
    imgurLastRefresh: (time in seconds)
"""
class AppValues(models.Model):
    key = models.TextField(primary_key=True)
    value = models.TextField()   
