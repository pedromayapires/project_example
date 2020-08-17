from django.db import models
from rest_framework import serializers
from django.db.models.query import QuerySet


# def query_get_dict_array(model_class, queryset, many=True):
def query_get_dict_array(queryset, many=True):
    class BaseSerializer(serializers.ModelSerializer):
        class Meta:
            # model = model_class
            model = queryset.model
            fields = "__all__"

    return BaseSerializer(queryset, many=many).data


class BaseQuerySet(QuerySet):
    def to_dict_array(self, many=True):
        return query_get_dict_array(self, many)


class BaseManager(models.Manager):
    _queryset_class = BaseQuerySet


class BaseModel(models.Model):
    # define abstract so that it does not cause any problem with model
    # hierarchy in database
    class Meta:
        abstract = True

    objects = BaseManager()

    @classmethod
    def get_dict_array(cls, queryset, many=True):
        # serializerObj = cls.get_serializer()
        # return serializerObj(queryset, many=many).data
        return query_get_dict_array(cls, queryset, many=many).data
