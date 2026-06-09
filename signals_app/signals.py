import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SyncTestModel, LogModel,ThreadTestModel,TransactionTestModel
from signals_app.views import signal_thread_id

@receiver(post_save,sender=SyncTestModel)
def test_signal(sender, instance, **kwarg):
    print("Signal Started")
    time.sleep(5)
    print("Signal finished")

@receiver(post_save, sender=ThreadTestModel)
def test_thread_signal(sender, instance, **kwargs):
    import signals_app.views
    signals_app.views.signal_thread_id = threading.get_ident()

@receiver(post_save,sender=TransactionTestModel)
def test_transaction_signal(sender, instance, **kwargs ):
    LogModel.objects.create(
        message="Created From signal"
    )

    print("Signal Executed")