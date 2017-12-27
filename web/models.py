from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Host(models.Model):
    hostname = models.CharField(max_length=64,unique=True)
    wip = models.GenericIPAddressField()
    lip = models.GenericIPAddressField()
    idc = models.ForeignKey('IDC')
    tag = models.ManyToManyField('Tag')
    bindhost = models.ForeignKey('BindHost')
    hostgroup = models.ManyToManyField('HostGroup')
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    memo = models.TextField()
    def __unicode__(self):
        return  self.hostname
    class Meta:
        unique_together =('wip','lip')


class IDC(models.Model):
    name = models.CharField(max_length=64)
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=64)
    def __unicode__(self):
        return self.name

class BindHost(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    def __unicode__(self):
        return "%s-%s" %(self.username,self.password)

class HostGroup(models.Model):
    name = models.CharField(max_length=32)
    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    dep = models.ForeignKey('Dep')
    def  __unicode__(self):
        return self.email


class Dep(models.Model):
    name = models.CharField(max_length=32)
    def __unicode__(self):
        return self.name