from django.db import models
from django.urls import reverse

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
            return self.title

    def get_absolute_url(self):
            return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})