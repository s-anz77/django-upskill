from django.db import models
from django.urls import reverse
from django.conf import settings

class Course(models.Model):
    title = models.CharField('Название курса', max_length=120)
    slug = models.SlugField('Уникальное название')
    category = models.CharField('Категория', max_length=20, default='none')
    description = models.TextField('Описание курса')
    image = models.ImageField('Изображение', default='courses_images/default-course.png', upload_to='courses_images')
    icon = models.ImageField('Иконка', default='courses_images/icons/default-course-icon.png', upload_to='courses_images/icons')
    is_free = models.BooleanField('Бесплатно?', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})

class Lesson(models.Model):
    title = models.CharField('Название урока', max_length=120)
    slug = models.SlugField('Уникальное название урока')
    description = models.TextField('Описание урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Какой курс?')
    number = models.IntegerField('Номер урока')
    video = models.CharField('URL Видеоурока', max_length=100)

    def __str__(self):
            return f'{self.course.slug} | #{self.number}: {self.title}'

    def get_absolute_url(self):
            return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})


class LessonComments(models.Model):
    text = models.TextField('Текст комментария')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='К какому уроку?')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        text = self.text[:20]
        if len(self.text) > 20:
            text += '…'
        return f'{self.lesson.slug} | {self.author}: {text}'

    class Meta:
        verbose_name = 'Комментарий к уроку'
        verbose_name_plural = 'Комментарии к урокам'
