from django import forms
from formapp.models import teachers, students, courses


class teacherform(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    office_details = forms.Field()
    phone = forms.IntegerField()
    email = forms.EmailField()

    def save_teacher(self):
        a = teachers(first_name=self.cleaned_data["first_name"],
                     last_name=self.cleaned_data["last_name"],
                     email=self.cleaned_data["email"],
                     office_details=self.cleaned_data['office_details'],
                     phone=self.cleaned_data['phone'])

        a.save()


class studentform(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    courses = forms.ModelMultipleChoiceField(courses.objects.all(),widget=forms.CheckboxSelectMultiple)

    def save_student(self):
        a = students(first_name=self.cleaned_data["first_name"],
                     last_name=self.cleaned_data["last_name"],
                     email=self.cleaned_data["email"],
                     )
        a.save()
        for item in self.cleaned_data['courses']:
            a.course.add(item)


class courseform(forms.Form):
    course_name = forms.CharField(max_length=50)
    code = forms.CharField(max_length=30)
    classroom = forms.CharField(max_length=30)
    time = forms.TimeField()
    teacher = forms.ModelChoiceField(teachers.objects.all())

    def save_course(self):
        a = courses(course_name=self.cleaned_data["course_name"],
                     code=self.cleaned_data["code"],
                     classroom=self.cleaned_data["classroom"],
                     time=self.cleaned_data['time'],teacher=self.cleaned_data['teacher'])

        a.save()
