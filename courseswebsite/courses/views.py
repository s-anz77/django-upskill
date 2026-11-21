from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from .models import Course, Lesson, LessonComments
from .forms import AddLessonCommentForm

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
        course = kwargs.get('object') or self.get_object()
        lesson = get_object_or_404(
            Lesson,
            course=course,
            slug=self.kwargs['lesson_slug'],
        )

        lesson.video = lesson.video.split('=')[1].split('&')[0]

        ctx['course'] = course
        ctx['title'] = lesson
        ctx['lesson'] = lesson
        ctx['lessons'] = Lesson.objects.filter(course=course)
        ctx['comments'] = LessonComments.objects.filter(lesson=lesson).select_related('author')
        ctx['form'] = kwargs.get('form') or AddLessonCommentForm()
        return ctx

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('user')

        course = self.get_object()
        lesson = get_object_or_404(
            Lesson,
            course=course,
            slug=kwargs['lesson_slug'],
        )
        form = AddLessonCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.lesson = lesson
            comment.save()
            return redirect(
                'lesson-detail',
                slug=course.slug,
                lesson_slug=lesson.slug,
            )

        context = self.get_context_data(object=course, form=form)
        return self.render_to_response(context, status=400)

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
