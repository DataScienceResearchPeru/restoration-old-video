
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# CLASS HYPERTABLE IN APP API

# class ApiMedicKitPerUser(models.Model):
#     kit_id = models.TextField(primary_key=True)
#     user = models.ForeignKey('AuthUser', models.DO_NOTHING)
#     estado_comunicacion = models.TextField(blank=True, null=True)  # This field type is a guess.
#     estado_baterias = models.TextField(blank=True, null=True)  # This field type is a guess.
#     tiempo_muestreo = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'api_medic_kit_per_user'


# class ApiMedicNotifications(models.Model):
#     time = models.DateTimeField(primary_key=True)
#     json_notification = models.TextField(blank=True, null=True)  # This field type is a guess.
#     kit = models.ForeignKey(ApiMedicKitPerUser, models.DO_NOTHING, db_column='kit')

#     class Meta:
#         managed = False
#         db_table = 'api_medic_notifications'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class AuthtokenToken(models.Model):
#     key = models.CharField(primary_key=True, max_length=40)
#     created = models.DateTimeField()
#     user = models.OneToOneField(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'authtoken_token'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class Oauth2ProviderAccesstoken(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     token = models.CharField(unique=True, max_length=255)
#     expires = models.DateTimeField()
#     scope = models.TextField()
#     application = models.ForeignKey('Oauth2ProviderApplication', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#     source_refresh_token = models.OneToOneField('Oauth2ProviderRefreshtoken', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'oauth2_provider_accesstoken'


# class Oauth2ProviderApplication(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     client_id = models.CharField(unique=True, max_length=100)
#     redirect_uris = models.TextField()
#     client_type = models.CharField(max_length=32)
#     authorization_grant_type = models.CharField(max_length=32)
#     client_secret = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
#     skip_authorization = models.BooleanField()
#     created = models.DateTimeField()
#     updated = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'oauth2_provider_application'


# class Oauth2ProviderGrant(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     code = models.CharField(unique=True, max_length=255)
#     expires = models.DateTimeField()
#     redirect_uri = models.CharField(max_length=255)
#     scope = models.TextField()
#     application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#     code_challenge = models.CharField(max_length=128)
#     code_challenge_method = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'oauth2_provider_grant'


# class Oauth2ProviderRefreshtoken(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     token = models.CharField(max_length=255)
#     access_token = models.OneToOneField(Oauth2ProviderAccesstoken, models.DO_NOTHING, blank=True, null=True)
#     application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#     revoked = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'oauth2_provider_refreshtoken'
#         unique_together = (('token', 'revoked'),)


# class SocialAuthAssociation(models.Model):
#     server_url = models.CharField(max_length=255)
#     handle = models.CharField(max_length=255)
#     secret = models.CharField(max_length=255)
#     issued = models.IntegerField()
#     lifetime = models.IntegerField()
#     assoc_type = models.CharField(max_length=64)

#     class Meta:
#         managed = False
#         db_table = 'social_auth_association'
#         unique_together = (('server_url', 'handle'),)


# class SocialAuthCode(models.Model):
#     email = models.CharField(max_length=254)
#     code = models.CharField(max_length=32)
#     verified = models.BooleanField()
#     timestamp = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'social_auth_code'
#         unique_together = (('email', 'code'),)


# class SocialAuthNonce(models.Model):
#     server_url = models.CharField(max_length=255)
#     timestamp = models.IntegerField()
#     salt = models.CharField(max_length=65)

#     class Meta:
#         managed = False
#         db_table = 'social_auth_nonce'
#         unique_together = (('server_url', 'timestamp', 'salt'),)


# class SocialAuthPartial(models.Model):
#     token = models.CharField(max_length=32)
#     next_step = models.SmallIntegerField()
#     backend = models.CharField(max_length=32)
#     data = models.TextField()
#     timestamp = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'social_auth_partial'


# class SocialAuthUsersocialauth(models.Model):
#     provider = models.CharField(max_length=32)
#     uid = models.CharField(max_length=255)
#     extra_data = models.TextField()
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     created = models.DateTimeField()
#     modified = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'social_auth_usersocialauth'
#         unique_together = (('provider', 'uid'),)

