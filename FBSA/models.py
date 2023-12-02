from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=50)

    def __str__(self):
        return self.d_name


class F_Registration(models.Model):
    f_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    n_pass = models.CharField(max_length=50)
    c_pass = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Semester(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=50)

    def __str__(self):
        return self.s_name


class Gender(models.Model):
    g_name = models.CharField(max_length=10)

    def __str__(self):
        return self.g_name


class F_login(models.Model):
    fl_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    c_pass = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class S_Login(models.Model):
    st_id = models.AutoField(primary_key=True)
    s_fname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    c_pass = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class S_registration(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_fname = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    e_no = models.CharField(max_length=50)
    sem = models.IntegerField()
    gender = models.CharField(max_length=50)
    b_date = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    n_pass = models.CharField(max_length=50)
    c_pass = models.CharField(max_length=50)

    def __str__(self):
        return self.s_fname


class F_code(models.Model):
    code = models.CharField(max_length=5)
    sub_name = models.CharField(max_length=20)

    def __str__(self):
        return self.code


class S_code(models.Model):
    code = models.CharField(max_length=5)
    sub_name = models.CharField(max_length=20)

    def __str__(self):
        return self.code


class Subject(models.Model):
    sub_name = models.CharField(max_length=20)

    def __str__(self):
        return self.sub_name
