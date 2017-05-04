""" Simple and easy way to serialize Django Object
    based on DjangoRestFramework.
    Different from ``django.core.serializers``.
"""

from django.apps.registry import apps as registered_apps
from django.core import exceptions
from django.db.models.fields import related
from django.utils.encoding import is_protected_type
from rest_framework import serializers

__all__ = [
    'serialize',
    'deserialize',
]


def get_model_label(model):
    return '{}.{}'.format(model._meta.app_label, model._meta.object_name)


def get_model(model_label):
    return registered_apps.get_model(model_label)


def get_serializer_class(obj):
    class AbstractModelSerializer(serializers.ModelSerializer):

        class Meta:
            model = obj._meta.model

        def create(self, validated_data):
            return self.Meta.model(**validated_data)

        def update(self, instance, validated_data):
            if not instance or not instance.id:
                return self.create(validated_data)
            else:
                for k, v in validated_data.items():
                    setattr(instance, k, v)
            return instance

    serializer_class = AbstractModelSerializer
    return serializer_class


def _natural_foreign(field):
    return isinstance(field, related.ForeignKey) \
           and hasattr(field.remote_field.model, 'natural_key')


def handle_natural_foreign(obj, field):
    if hasattr(field.remote_field.model, 'natural_key'):
        _related = getattr(obj, field.name)
        if _related:
            value = _related.natural_key()
        else:
            value = None
    else:
        value = getattr(obj, field.get_attname())
        if not is_protected_type(value):
            value = field.value_to_string(obj)
    return value


def serialize(obj, natural_foreign=True, natural_primary=False):
    """ Serialize Django object to JSON

    :param obj: Django model object
    :param natural_foreign: use foreign_key.natural_key
    :param natural_primary: natural primary
    :return: data
    """
    serializer = get_serializer_class(obj)(obj)
    return serializer.data


def deserialize(model, data, instance=None):
    """ Deserialize JSON data to a Django Model object
    :param model: model
    :param data: dict
    :param instance: model object instance
    :return: obj
    """
    serializer_cls = get_serializer_class(model)
    serializer = serializer_cls(instance=instance, data=data)
    if not serializer.is_valid():
        raise exceptions.ValidationError(serializer.errors)

    obj = serializer.save()
    return obj
