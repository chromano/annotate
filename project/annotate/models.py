import os

from django.db import models
from mongoengine import connect, Document
from mongoengine.fields import DictField, ListField, StringField

connect("annotate", host=os.getenv("MONGOHQ_URL"))

class AnnotatedDoc(Document):
    text = ListField(DictField())
    title = StringField()

    def __unicode__(self):
        return "%s, %s" % (self.title, self.text)
