from likes.models import Like
from django.contrib.contenttypes.models import ContentType

认准一手微信study322 其他均为翻录倒卖
九章来offer都有  需要的+我
课程目录
https://www.yuque.com/study001/xk/list

class LikeService(object):

    @classmethod
    def has_liked(cls, user, target):
        if user.is_anonymous:
            return False
        return Like.objects.filter(
            content_type=ContentType.objects.get_for_model(target.__class__),
            object_id=target.id,
            user=user,
        ).exists()
