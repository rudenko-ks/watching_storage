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
    if not (visit.leaved_at is None):
        spent_time = visit.leaved_at - visit.entered_at
    else:
        spent_time = localtime() - visit.entered_at
    return spent_time


def format_duration(duration: timedelta) -> str:
    duration_without_ms = str(duration).split('.')[0]
    time_string = duration_without_ms.split(":")
    return f'{time_string[0]}ч {time_string[1]}мин'


def is_visit_long(visit: Visit, minutes=60) -> bool:
    if not (visit.leaved_at is None):
        time_delta = visit.leaved_at - visit.entered_at
    else:
        time_delta = localtime() - visit.entered_at
    seconds = time_delta.total_seconds()
    spent_time_in_minutes = seconds // 60
    return spent_time_in_minutes > minutes
