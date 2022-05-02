from django.contrib import admin
from likes.models import Like

认准一手微信study322 其他均为翻录倒卖
九章来offer都有  需要的+我
课程目录
https://www.yuque.com/study001/xk/list

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'content_type',
        'object_id',
        'content_object',
        'created_at',
    )
    list_filter = ('content_type',)
    date_hierarchy = 'created_at'
