import time
import threading
from django.http import HttpResponse
from django.db import transaction
from .models import SyncTestModel, LogModel,ThreadTestModel,TransactionTestModel

def test_sync_signal(request):
    start_time = time.time()

    SyncTestModel.objects.create(name="Test")

    end_time = time.time()

    total_time = end_time - start_time

    return HttpResponse(
        f"Time taken: {total_time:.2f} seconds"
    )

signal_thread_id = None

def test_thread_signal(request):
    global signal_thread_id

    caller_thread_id = threading.get_ident()

    ThreadTestModel.objects.create(name="Thread Test")

    return HttpResponse(
        f"Caller Thread: {caller_thread_id}<br>"
        f"Signal Thread: {signal_thread_id}"
    )

def test_transaction_signal(request):
    TransactionTestModel.objects.all().delete()
    LogModel.objects.all().delete()

    try:
        with transaction.atomic():
            TransactionTestModel.objects.create(
                name="Transaction Test"
            )

            raise Exception("Force RollBack")
    except Exception:
        pass

    transaction_test_count = TransactionTestModel.objects.count()
    log_count = LogModel.objects.count()

    return HttpResponse(
        f"Transaction Model Count = {transaction_test_count}<br>"
        f"LogModel Count = {log_count}"
    )