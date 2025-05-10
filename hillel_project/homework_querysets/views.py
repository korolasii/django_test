from django.http import JsonResponse
from django.db.models import Q
from .models import Department, Position

def homework_querysets(request):
    departments_with_managers = Department.objects.filter(
        position__title__icontains='manager'
    ).order_by('name').distinct()

    active_positions_count = Position.objects.filter(is_active=True).count()

    active_or_hr_positions = Position.objects.filter(
        Q(is_active=True) | Q(department__name="HR")
    )

    department_names_with_managers = Department.objects.filter(
        position__title__icontains='manager'
    ).values('name').distinct()

    positions_name_active = Position.objects.order_by('title').values('title', 'is_active')

    return JsonResponse({
        "departments_with_managers": list(departments_with_managers.values('id', 'name')),
        "active_positions_count": active_positions_count,
        "active_or_hr_positions": list(active_or_hr_positions.values('id', 'title')),
        "department_names_with_managers": list(department_names_with_managers),
        "positions_name_active": list(positions_name_active),
    })
