from django.core import serializers
from utils.json_encoder import JSONEncoder


class DjangoModelSerializer:

    @classmethod
    def serialize(cls, instance):

        #django serialzers needs a queryset or list, so use [instance]
        return serializers.serialize('json', [instance], cls=JSONEncoder)

    @classmethod
    def deserialize(cls, serialized_data):
        # 需要加 .object 来得到原始的 model 类型的 object 数据，要不然得到的数据并不是一个
        # ORM 的 object，而是一个 DeserializedObject 的类型
        #deserializer follow reversed path of serializer, needs to input a list
        return list(serializers.deserialize('json', serialized_data))[0].object
