# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
def gen_code_from_int(original_pk, starting_number_excl=0, length=6):
    """
        Generate a fixed length code(string) from PK,
        e.g. 20 -> 100020 / 000020
    """
    code_str = str(starting_number_excl + original_pk)
    return code_str[-length:].zfill(length)

#客户信息
class Client(models.Model):
    gender_choice = (
        ('male', '男'),
        ('female', '女')
    )

    client_status_choice = (
        ('leads', '潜在客户'),
        ('normal', '正式客户'),
        ('end', '已结案'),
    )

    client_type_choice = (
        ('student', '学生'),
        ('parent', '家长'),
        ('adault', '成人'),
    )

    vip_class_choice = (
        ('no', '无'),
        ('1', 'VIP1'),
        ('2', 'VIP2'),
        ('3', 'VIP3'),
        ('life', '终身制'),
    )

    name = models.CharField(max_length=10, verbose_name='姓名')
    code = models.CharField(max_length=10, verbose_name='客户编号', default=0, unique=True)
    gender = models.CharField(max_length=6, verbose_name='性别', choices=gender_choice)
    phone = models.CharField(max_length=13, verbose_name='联系方式')
    birthday = models.DateField(verbose_name='出生日期')
    school = models.CharField(max_length=50, verbose_name='就读学校', blank=True)
    vip_class = models.CharField(max_length=4, verbose_name='VIP级别', default='no', choices=vip_class_choice)
    client_status = models.CharField(max_length=10, verbose_name='客户状态', choices=client_status_choice, default='leads')
    client_type = models.CharField(max_length=8, verbose_name='客户类型', choices=client_type_choice, default='student', blank=True)
    adress = models.CharField(max_length=50, verbose_name='住址')
    leads_source = models.CharField(max_length=30, verbose_name='何处得知我们', blank=True)
    comments = models.TextField(max_length=400, verbose_name='备注', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False, verbose_name='在案客户')

    class Meta:
        ordering = ('-created',)
        verbose_name = '客户'
        verbose_name_plural = '客户'



    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)

        # Populate the code if it is missing
        # 第一次保存时，生成6位流水号
        if self.pk and not self.code:
            self.code = gen_code_from_int(self.pk, length=6, starting_number_excl=0)
            kwargs['force_insert'] = False
            super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# 预约来访
class Appointment(models.Model):
    time_slot_choice = (

        ('AM', '10:00-11:00'),
        ('PM', '15:00-16:00'),
    )

    confirm_status_choice = (
        ('un', '未确认'),
        ('co', '已到访'),
        ('ab', '缺席'),
    )

    client = models.ForeignKey(Client, related_name='appointments', verbose_name='客户姓名')
    time_slot = models.CharField(choices=time_slot_choice, max_length=4, verbose_name='时间段', default='PM')
    confirm_status = models.CharField(choices=confirm_status_choice, max_length=2, verbose_name='确认状态', default='un')
    date = models.DateField(verbose_name='预约日期')
    subject = models.CharField(max_length=30, verbose_name='预约主题')
    comment = models.TextField(max_length=100, verbose_name='备注', blank=True)

    class Meta:
        ordering = ('-date',)
        verbose_name = '咨询预约'
        verbose_name_plural = '咨询预约'

    def __str__(self):
        return self.client.name


#来访记录
class Record(models.Model):
    client = models.ForeignKey(Client, related_name='records',verbose_name='客户')
    title = models.CharField(max_length=100, verbose_name='标题')
    body = models.TextField(max_length=2000, verbose_name='正文')
    visit = models.IntegerField(default=0, verbose_name='到访次数')
    appointment = models.ForeignKey(Appointment, related_name='records', verbose_name='预约记录')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '来访纪录'
        verbose_name = '来访纪录'

    def __str__(self):
        return self.client.name


# 回访
class Returning_call(models.Model):
    client = models.ForeignKey(Client, related_name='returning_calls', verbose_name='客户姓名')
    comment = models.TextField(max_length=1000, verbose_name='回访记录')
    call_date = models.DateTimeField(verbose_name='回访时间')
    created_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        ordering = ('-call_date',)
        verbose_name = '回访记录'
        verbose_name_plural = '回访记录'

    def __str__(self):
        return self.client.name

