# -*- coding: utf-8 -*-

import peewee

db = peewee.SqliteDatabase('photo_with_mustache.db')


class Mustache(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = db
