from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course, Lesson

class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_queryset(self):
        return super().get_queryset().order_by('-id')

    def get_context_data(self, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'

        ctx['free_courses'] = Course.objects.filter(is_free=True).order_by('-pk')[:3]
        ctx['paid_courses'] = Course.objects.filter(is_free=False).order_by('-pk')[:3]

        return ctx

class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course)
        return ctx

class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lesson-detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

        lesson.video = lesson.video.split('=')[1].split('&')[0]

        ctx['title'] = lesson
        ctx['lesson'] = lesson
        ctx['lessons'] = Lesson.objects.filter(course=course)
        return ctx

def SubscriptionPage(request):
    return render(request, 'courses/sub.html')

# def AllCoursesPage(request):
#     return render(request, 'courses/courses.html')

class AllCoursesPage(ListView):
    model = Course
    template_name = 'courses/courses.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_queryset(self):
        return super().get_queryset().order_by('-id')

    def get_context_data(self, **kwargs):
        ctx = super(AllCoursesPage, self).get_context_data(**kwargs)
        return ctx