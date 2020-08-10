from django.core.signals import request_finished
from django.dispatch import receiver, Signal


@receiver(request_finished)
def request_receiver(sender, **kwargs):
    print('request success')


request_date_signal = Signal(providing_args=["date"])


@receiver(request_date_signal)
def request_date_receiver(sender, **kwargs):
    print(kwargs)
