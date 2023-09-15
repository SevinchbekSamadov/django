from themes.models import Lesson
from django.views.generic import ListView
from themes.models import Lesson

# Create your views here. temolate na'lumotlarni brauzer oynasida chiqarish uchun kerak bo'ladi

class ShowLessonsView(ListView):
    model = Lesson

    template_name = 'themes.html'


# def ShowLessonsView(request):
#     context = {} #context bu html file ga jo'natildigan ma'lumotlar model bu ma'lumotar bazasining strukturasi
#     lessons = Lesson.objects.all()
#     context['lessons'] = lessons
#     return render(request, 'themes.html', context)