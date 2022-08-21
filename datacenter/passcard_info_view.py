from datacenter.models import Passcard, format_duration, get_duration, is_visit_long
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    user_passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = []
    user_visits = Visit.objects.filter(passcard=user_passcard)
    for visit in user_visits:
        spent_time = get_duration(visit)
        visit_info = {
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(spent_time),
            'is_strange': is_visit_long(visit, minutes=12)
        }
        this_passcard_visits.append(visit_info)

    context = {
        'passcard': user_passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
