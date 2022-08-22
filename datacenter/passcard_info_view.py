from datacenter.models import Passcard, format_duration, get_duration, is_visit_long
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        spent_time = get_duration(visit)
        visit_info = {
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(spent_time),
            'is_strange': is_visit_long(visit, minutes=60)
        }
        this_passcard_visits.append(visit_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
