from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    github = models.URLField(null=False, blank=False, max_length=500)
    linkedin = models.URLField(null=False, blank=False, max_length=500)
    bio = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    github_url = models.URLField(max_length=500, null=False, blank=False)
    keyword = models.CharField(max_length=50, null=False, blank=False)
    key_skill = models.CharField(max_length=50, null=False, blank=False)
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='projects')

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    url = models.URLField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    timestamp = models.DateTimeField(null=False,
                                     blank=False,
                                     auto_now_add=True,
                                     max_length=500)
    profiles = models.ManyToManyField(Profile,
                                      related_name='certificates',
                                      blank=False,
                                      max_length=500)
    certifying_institution = models.ForeignKey(CertifyingInstitution,
                                               on_delete=models.CASCADE,
                                               related_name='certificates',
                                               null=False,
                                               blank=False,
                                               max_length=500)

    def __str__(self):
        return self.name
