from datetime import date
import calendar
from django import forms
from django.forms import ChoiceField
from django.core.exceptions import ValidationError
from first_app.models import Employee

from common.enums import WorkDayEnum


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('username', 'first_name', 'last_name', 'email', 'position')




class SalaryForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = date.today()
        week_day, num_days = calendar.monthrange(today.year, today.month)
        for day in range(1, num_days + 1):
            day_coord = today.year, today.month, day
            weekday = calendar.weekday(*day_coord)
            weekday_name = calendar.day_name[weekday]
            field_name = f"day_{day}"

            if calendar.weekday(*day_coord) >= 5:
                self.fields[field_name] = forms.ChoiceField(
                    label=f'{day} - {weekday_name}',
                    choices=[(WorkDayEnum.WEEKEND.name, WorkDayEnum.WEEKEND.value)],
                    initial=WorkDayEnum.WEEKEND.name
                )
            else:
                self.fields[field_name] = forms.ChoiceField(
                    label=f'{day} - {weekday_name}',
                    choices=[(option.name, option.value) for option in WorkDayEnum],
                    initial=WorkDayEnum.WORKING_DAY.name,
                )

    def clean_employee(self):
        employee = self.cleaned_data.get('employee')
        if not employee:
            raise ValidationError("Переконайтеся, що поле employee заповнено.")
        return employee

    def clean(self):
        cleaned_data = super().clean()

        days_dict = {field: cleaned_data.get(field) for field in self.fields}
        sick_days_count = sum(1 for day, day_type in days_dict.items() if day_type == WorkDayEnum.SICK_DAY.name)
        holiday_days_count = sum(1 for day, day_type in days_dict.items() if day_type == WorkDayEnum.HOLIDAY.name)

        if sick_days_count > 5:
            raise ValidationError("Кількість лікарняних днів не повинна перевищувати 5.")

        if holiday_days_count > 3:
            raise ValidationError("Кількість днів відпочинку не повинна перевищувати 3.")

        return cleaned_data