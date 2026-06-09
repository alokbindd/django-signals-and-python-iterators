from django.urls import path
from .views import test_sync_signal, test_thread_signal,test_transaction_signal

urlpatterns = [
    path('q1/',view=test_sync_signal,name='test-sync-signal'),
    path('q2/',view=test_thread_signal,name='test-thread-signal'),
    path('q3/',view=test_transaction_signal,name='test_transaction_signal'),
]