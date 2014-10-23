

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SbFile(models.Model):
    file_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('SbUser', blank=True, null=True)
    file_category = models.ForeignKey('SbFileCategory', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    path = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'sb_file'


class SbFileCategory(models.Model):
    file_category_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=45, blank=True)
    file_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_file_category'


class SbFileRating(models.Model):
    file_rating_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('SbUser', blank=True, null=True)
    file = models.ForeignKey(SbFile, blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_file_rating'


class SbUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email_address = models.CharField(max_length=80, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postalcode = models.CharField(max_length=12, blank=True)
    region = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    registration_date = models.DateTimeField(blank=True, null=True)
    user_type = models.ForeignKey('SbUserType', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_user'


class SbUserFriend(models.Model):
    user = models.ForeignKey(SbUser)
    friend_id = models.IntegerField()
    accepted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_user_friend'


class SbUserLogin(models.Model):
    user_login_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(SbUser, blank=True, null=True)
    provider = models.CharField(max_length=45, blank=True)
    provider_id = models.CharField(max_length=150, blank=True)
    access_token = models.CharField(max_length=150, blank=True)

    class Meta:
        managed = False
        db_table = 'sb_user_login'


class SbUserType(models.Model):
    user_type_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'sb_user_type'