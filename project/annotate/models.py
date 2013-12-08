from django.db import models
from mongoengine import connect, Document
from mongoengine.fields import DictField, ListField

connect("annotate")

class AnnotatedDoc(Document):
    text = ListField(DictField())

