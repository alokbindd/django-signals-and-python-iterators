from django.db import models

class SyncTestModel(models.Model):
    name = models.CharField(max_length=100)

class ThreadTestModel(models.Model):
    name = models.CharField(max_length=100)

class TransactionTestModel(models.Model):
    name = models.CharField(max_length=100)

class LogModel(models.Model):
    message = models.CharField(max_length=100)
