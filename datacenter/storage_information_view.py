from datacenter.models import Visit, is_visit_long
from datacenter.models import get_duration, format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []

    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in active_visits:
        entered_at = localtime(visit.entered_at)
        spent_time = get_duration(visit)

        user_inside = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': entered_at,
            'duration': format_duration(spent_time),
            'is_strange': is_visit_long(visit, minutes=12)
            }
        non_closed_visits.append(user_inside)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
