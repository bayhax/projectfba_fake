from django.db import models

# Create your models here.
from django.db import models
import django.utils.timezone as timezone
from django.db.models import ImageField
from tinymce.models import HTMLField
from db.base_model import BaseModel


class Blogs(BaseModel):
    """行业资讯表"""
    objects = models.Manager()
    title = models.CharField(max_length=50, verbose_name='标题')
    description = models.CharField(default='', max_length=1024, verbose_name='文章描述')
    keywords = models.CharField(default='', max_length=1024, verbose_name='关键词')
    content = HTMLField(verbose_name='博客内容')
    img = ImageField(upload_to='img/news')
    add_date = models.DateTimeField(default=timezone.now, verbose_name='保存日期')
    mod_date = models.DateTimeField(auto_now=True, verbose_name='修改日期')

    class Meta:
        db_table = 'blog'
        verbose_name = '博客表'
        verbose_name_plural = verbose_name
