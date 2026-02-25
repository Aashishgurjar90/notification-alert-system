from django.db import models
from accounts.models import Tenant, User


class Alert(models.Model):

    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    title = models.CharField(max_length=255)

    description = models.TextField()

    alert_type = models.CharField(max_length=100)

    severity = models.CharField(
        max_length=10,
        choices=SEVERITY_CHOICES,
        db_index=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open',
        db_index=True
    )

    latitude = models.FloatField()

    longitude = models.FloatField()

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name='alerts'
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.title