from django.contrib import admin
from .models import SyncTestModel, LogModel,ThreadTestModel,TransactionTestModel

# Register your models here.

class SyncTestModelAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
class ThreadTestModelAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
class TransactionTestModelAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
class LogModelAdmin(admin.ModelAdmin):
    list_display = ('id','message',)


admin.site.register(SyncTestModel,SyncTestModelAdmin)
admin.site.register(ThreadTestModel,ThreadTestModelAdmin)
admin.site.register(TransactionTestModel,TransactionTestModelAdmin)
admin.site.register(LogModel,LogModelAdmin)
