from django.db import models


class OrderStatusChoices(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    COMPLETED = 'Completed', 'Completed'
    CANCELED = 'Canceled', 'Canceled'
