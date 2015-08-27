# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

CHOICES_YES_NO = (
    (0,'NO'),
    (1,'YES'),
)

CHOICES_VERSION = (
    ('1.08','1.08'),
    ('1.09','1.09'),
    ('1.09','1.09'),
)

CHOICES_CONFIG_TYPE = (
    (0,'0任务'),
    (1,'1成就'),
    (2,'2道具'),
    (3,'3商店'),
    (4,'4礼包'),
    (5,'5选关界面'),
    (6,'6游戏内复活后'),
    (7,'7我的冲客'),
    (8,'8主界面'),
    (100,'100未购买角色'),
    (101,'101首次进入界面'),
)

class Configuimodel(models.Model):
    type = models.IntegerField(blank=True, null=True,choices=CHOICES_CONFIG_TYPE)
    version = models.CharField(max_length=255, blank=True, null=True,choices=CHOICES_VERSION)
    parms = models.CharField(max_length=255, blank=True, null=True)
    descript = models.CharField(max_length=255, blank=True, null=True)
    

    class Meta:
        db_table = 'configuimodel'
        verbose_name = '客户端UI配置表'
        
        
    def __str__(self):
        return str(self.type) + ':' + self.descript
        
class Realinfodatamodel(models.Model):
    itemid = models.IntegerField(db_column='itemID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    needhappypoint = models.IntegerField(db_column='needHappyPoint', blank=True, null=True)  # Field name made lowercase.
    refleshnum = models.IntegerField(db_column='RefleshNum', blank=True, null=True)  # Field name made lowercase.
    minuteforreflesh = models.IntegerField(db_column='MinuteForReflesh', blank=True, null=True)  # Field name made lowercase.
    timerefleshcng = models.IntegerField(db_column='timeRefleshCng', blank=True, null=True)  # Field name made lowercase.
    canreplace = models.IntegerField(db_column='canReplace', blank=True, null=True,choices=CHOICES_YES_NO)  # Field name made lowercase.
    descript = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'realinfodatamodel'
        verbose_name = '欢乐无尽兑换表'
        
    def __str__(self):
        return self.name
        
class Activitymodel(models.Model):

    CHOICES_ACTIVITY_ID = (
        (103,'103'),
        (104,'104'),
        (105,'105'),
        (106,'106'),
        (107,'107'),
        (108,'108'),
    )
    
    CHOICES_VERSION = (
        ('1.08','1.08'),
        ('1.09','1.09'),
        ('1.10','1.10'),
    )
    activityid = models.IntegerField(db_column='activityID', blank=True,choices=CHOICES_ACTIVITY_ID)  # Field name made lowercase.
    version = models.CharField(max_length=255, blank=True, choices=CHOICES_VERSION)
    begin = models.DateTimeField(blank=True)
    end = models.DateTimeField(blank=True)
    parms = models.CharField(max_length=255, blank=True, null=True)
    descript = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'activitymodel'
        unique_together = (('activityid', 'version'),)
        verbose_name = '活动表'
        
    def __str__(self):
        return self.version+':'+self.descript
        
        
        
class Blacklistdata(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    identify = models.CharField(db_column='Identify', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'blacklistdata'
        verbose_name = '黑名单'
        
    def __str__(self):
        return self.username


class Gameuser(models.Model):
    userid = models.IntegerField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    passportid = models.CharField(db_column='PassportId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retailid = models.CharField(db_column='RetailId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identify = models.CharField(db_column='Identify', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=255, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    diamond = models.IntegerField(db_column='Diamond', blank=True, null=True)  # Field name made lowercase.
    thetotal = models.IntegerField(db_column='theTotal', blank=True, null=True)  # Field name made lowercase.
    preranking = models.IntegerField(db_column='preRanking', blank=True, null=True)  # Field name made lowercase.
    compensationdate = models.DateTimeField(db_column='CompensationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gameuser'
        
    def __str__(self):
        return self.nickname


class Happymodedata(models.Model):
    the3rduserid = models.IntegerField(db_column='the3rdUserId', primary_key=True)  # Field name made lowercase.
    enternum = models.IntegerField(db_column='EnterNum', blank=True, null=True)  # Field name made lowercase.
    happypoint = models.IntegerField(db_column='HappyPoint', blank=True, null=True)  # Field name made lowercase.
    happyrelivenum = models.IntegerField(db_column='HappyReliveNum', blank=True, null=True)  # Field name made lowercase.
    realitembuycntinrefleshtime = models.TextField(db_column='realItemBuyCntInRefleshTime', blank=True, null=True)  # Field name made lowercase.
    prerefleshtime = models.DateTimeField(db_column='PreRefleshTime', blank=True, null=True)  # Field name made lowercase.
    actionenterhappypoint = models.TextField(db_column='ActionEnterHappyPoint', blank=True, null=True)  # Field name made lowercase.
    realiteminfolst = models.TextField(db_column='RealItemInfoLst', blank=True, null=True)  # Field name made lowercase.
    payinfodic = models.TextField(db_column='PayInfoDic', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'happymodedata'
        
    def __str__(self):
        return str(self.the3rduserid)


class Userranking(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    identify = models.CharField(db_column='Identify', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userranking'
        
    def __str__(self):
        return str(self.username)
