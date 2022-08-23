from datetime import timedelta
from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit: Visit) -> timedelta:
    if visit.leaved_at:
        spent_time = visit.leaved_at - visit.entered_at
    else:
        spent_time = localtime() - localtime(visit.entered_at)
    return spent_time


def format_duration(duration: timedelta) -> str:
    seconds = duration.total_seconds()
    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    return f'{hours:.0f}ч {minutes:.0f}мин'


def is_visit_long(visit: Visit, minutes=60) -> bool:
    duration = get_duration(visit)
    spent_time_in_minutes = duration.total_seconds() // 60
    return spent_time_in_minutes > minutes
