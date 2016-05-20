# coding: UTF-8
from django.db import models


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

    name = models.CharField(max_length=10, verbose_name='姓名')
    code = models.CharField(max_length=10, verbose_name='客户编号', default=0, unique=True)
    gender = models.CharField(max_length=6, verbose_name='性别', choices=gender_choice)
    phone = models.CharField(max_length=13, verbose_name='联系方式')
    birthday = models.DateField(verbose_name='出生日期')
    school = models.CharField(max_length=50, verbose_name='就读学校', blank=True)
    comments = models.TextField(max_length=400, verbose_name='备注', blank=True)
    client_status = models.CharField(max_length=10, verbose_name='客户状态', choices=client_status_choice, default='leads')
    client_type = models.CharField(max_length=8, verbose_name='客户类型', choices=client_type_choice, default='student', blank=True)
    adress = models.CharField(max_length=50, verbose_name='住址')
    leads_source = models.CharField(max_length=30, verbose_name='何处得知我们', blank=True)
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

#来访记录
class Record(models.Model):
    client = models.ForeignKey(Client, related_name='records',verbose_name='客户')
    title = models.CharField(max_length=100, verbose_name='标题')
    body = models.TextField(max_length=2000, verbose_name='正文')
    visit = models.IntegerField(default=0, verbose_name='到访次数')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '来访纪录'
        verbose_name = '来访纪录'

    def __str__(self):
        return self.client.name


class Appointment(models.Model):
    time_slot_choice = (
        ('tue', '周二下午'),
        ('wed', '周三下午'),
        ('thu', '周四下午'),
        ('fri', '周五下午'),
        ('sun1', '周日上午'),
        ('sun2', '周日下午'),
    )

    client = models.ForeignKey(Client, verbose_name='客户姓名')
    subject = models.CharField(max_length=30, verbose_name='预约主题')
    time_slot = models.CharField(choices=time_slot_choice, verbose_name='时间段')
    confirm_status =