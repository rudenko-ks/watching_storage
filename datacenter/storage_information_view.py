from datacenter.models import Visit, is_visit_long
from datacenter.models import get_duration, format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []

    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in active_visits:
        user_inside = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit, minutes=60)
        }
        non_closed_visits.append(user_inside)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
