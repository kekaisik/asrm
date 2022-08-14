from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from ckeditor.fields import RichTextField
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/img', filename)


class User(AbstractUser):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    last_login = None
    groups = None
    # surname = models.CharField("Фамилия", max_length=100)
    # name = models.CharField("Имя", max_length=100)
    fatherland = models.CharField("Отчество", max_length=100, blank=True)
    paid = models.BooleanField("Участник Общества", default=False,)
    expiration_date = models.DateField("Подписка действительна до", blank=True, default=timezone.now())
    profession = models.CharField("Профессия", max_length=100)
    date_of_Birth = models.DateField("Дата Рождения", default=timezone.now)
    phone = models.CharField("Номер Телефона", max_length=50, unique=True)
    address = models.CharField("Адрес", max_length=100)
    city = models.CharField("Город", max_length=100)
    country = models.CharField("Страна", max_length=100)
    place_of_work = models.CharField("Место Работы", max_length=100)
    job = models.CharField("Должность", max_length=100)

    # #REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'profession', 'date_of_Birth', 'phone', 'address',
    #                    'city', 'country', 'place_of_work', 'job']


class BasePost(models.Model):
    ru_title = models.CharField("Название на русском", max_length=100)
    en_title = models.CharField("Название на английском", max_length=100)
    kz_title = models.CharField("Название на  казахском", max_length=100)
    ru_text = RichTextField("Текст на русском", blank=True, extra_plugins=['iframe'],)
    en_text = RichTextField("Текст на английском", blank=True, extra_plugins=['iframe'],)
    kz_text = RichTextField("Текст на казахском",blank=True, extra_plugins=['iframe'],)
    paid = models.BooleanField("Платный", default=False)
    main_image = models.ImageField("Основное фото", upload_to="post/img/", blank=True)
    category = models.CharField("Категория", max_length=50)
    date = models.DateTimeField("Дата Публикации", default=timezone.now)
    draft = models.BooleanField("Черновик", default=False)

    @property
    def main_image_preview(self):
        return mark_safe(f'<img src="{self.main_image.url}" width="400" />')

    @property
    def parse_date_en(self):
        dates = self.date.date()
        en_month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                         'August', 'September', 'October', 'November', 'December']
        return f'{dates.day} {en_month_list[dates.month-1]}, {dates.year}'

    @property
    def parse_date_ru(self):
        dates = self.date.date()
        ru_month_list = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
                         'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
        return f'{dates.day} {ru_month_list[dates.month - 1]}, {dates.year}'

    @property
    def parse_date_kz(self):
        dates = self.date.date()
        kz_month_list = ['Қаңтар', 'Ақпан', 'Наурыз', 'Сәуір',
                         'Мамыр', 'Маусым', 'Шілде', 'Тамыз', 'Қыркүйек', 'Қазан', 'Қараша', 'Желтоқсан']
        return f'{dates.day} {kz_month_list[dates.month - 1]}, {dates.year}'

    @property
    def get_text_ru(self,):
        return self.ru_text

    @property
    def get_title_ru(self):
        return self.ru_title

    @property
    def get_text_en(self, ):
        return self.en_text

    @property
    def get_title_en(self):
        return self.en_title

    @property
    def get_text_kz(self, ):
        return self.kz_text

    @property
    def get_title_kz(self):
        return self.kz_title

    class Meta:
        abstract = True


class Base_Images(models.Model):
    image = models.ImageField(upload_to=get_file_path, null=True)

    class Meta:
        abstract = True
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Base_Pdf(models.Model):
    pdf = models.FileField(upload_to=get_file_path, null=True)

    class Meta:
        abstract = True
        verbose_name = "PDF"
        verbose_name_plural = "PDF"


class Youtube_Url(models.Model):
    youtube_url = models.CharField('Ютуб ссылка', max_length=150)

    class Meta:
        verbose_name = "Ютуб Ссылка"
        verbose_name_plural = 'Ютуб Ссылки'
        abstract = True


# Классы


class Society(BasePost):

    @property
    def get_group(self):
        return 'society'

    @property
    def get_url(self):
        return f'society/{self.category}'

    class Meta:
        verbose_name = "Общество"
        verbose_name_plural = "Общество"


class Education(BasePost):
    @property
    def get_group(self):
        return 'education'

    @property
    def get_url(self):
        return f'education/{self.category}'

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"


class Protocols(BasePost):
    @property
    def get_group(self):
        return 'protocols'

    @property
    def get_url(self):
        return f'protocols/{self.category}'

    class Meta:
        verbose_name = "Клинические Протокол"
        verbose_name_plural = "Клинические Протоколы"


class Event(BasePost):
    en_announcement = models.CharField("Аннонс на английском", max_length=100, default='')
    ru_announcement = models.CharField("Аннонс на русском", max_length=100, default='')
    kz_announcement = models.CharField("Аннонс на казахском", max_length=100, default='')
    end_date = models.DateField("Окончание Мероприятия", default=timezone.now)

    @property
    def get_announcement_ru(self):
        return self.en_announcement

    @property
    def get_announcement_en(self):
        return self.ru_announcement

    @property
    def get_announcement_kz(self):
        return self.kz_announcement

    @property
    def parse_end_date_en(self):
        dates = self.end_date
        en_month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                         'August', 'September', 'October', 'November', 'December']
        return f'{dates.day} {en_month_list[dates.month - 1]}, {dates.year}'

    @property
    def parse_end_date_ru(self):
        dates = self.end_date
        ru_month_list = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
                         'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
        return f'{dates.day} {ru_month_list[dates.month - 1]}, {dates.year}'

    @property
    def parse_end_date_kz(self):
        dates = self.end_date
        kz_month_list = ['Қаңтар', 'Ақпан', 'Наурыз', 'Сәуір',
                         'Мамыр', 'Маусым', 'Шілде', 'Тамыз', 'Қыркүйек', 'Қазан', 'Қараша', 'Желтоқсан']
        return f'{dates.day} {kz_month_list[dates.month - 1]}, {dates.year}'

    @property
    def get_group(self):
        return 'events'

    @property
    def get_url(self):
        return f'events/{self.category}'

    class Meta:
        verbose_name = "Мероприятия"
        verbose_name_plural = "Мероприятия"


class News(models.Model):
    title = models.CharField("Название", max_length=100)
    text = RichTextField("Текст", extra_plugins=['iframe'],)
    paid = models.BooleanField("Платный", default=False)
    language = models.CharField("Язык", choices=[('ru', 'Русский'), ('en', 'Английский'), ('kz', 'Казахский')], max_length=2)
    main_image = models.ImageField("Основное фото", upload_to="post/img/", blank=True)
    date = models.DateTimeField("Дата Публикации", default=timezone.now)
    draft = models.BooleanField("Черновик", default=False)

    @property
    def parse_date(self):
        dates = self.date.date()
        en_month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                         'August', 'September', 'October', 'November', 'December']
        ru_month_list = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
                         'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
        kz_month_list = ['Қаңтар', 'Ақпан', 'Наурыз', 'Сәуір',
                         'Мамыр', 'Маусым', 'Шілде', 'Тамыз', 'Қыркүйек', 'Қазан', 'Қараша', 'Желтоқсан']
        if self.language == 'ru':
            return f'{dates.day} {ru_month_list[dates.month - 1]}, {dates.year}'
        elif self.language == 'kz':
            return f'{dates.day} {kz_month_list[dates.month - 1]}, {dates.year}'
        return f'{dates.day} {en_month_list[dates.month - 1]}, {dates.year}'

    @property
    def get_group(self):
        return 'news'

    def __str__(self):
        return self.title

    @property
    def get_url(self):
        return f'news/{self.id}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Index(models.Model):
    tags = [("about-us", "О нас"), ("membership", "Членство")]

    ru_title = models.CharField("Название на русском", max_length=50)
    kz_title = models.CharField("Название на казахском", max_length=50)
    en_title = models.CharField("Название на английском", max_length=50)
    ru_text = RichTextField("Текст на русском",  extra_plugins=['iframe'], blank=True, default='')
    en_text = RichTextField("Текст на английском",  extra_plugins=['iframe'], blank=True, default='')
    kz_text = RichTextField("Текст на казахском",  extra_plugins=['iframe'], blank=True, default='')
    category = models.CharField(choices=tags, max_length=15)

    @property
    def get_text_ru(self,):
        return self.ru_text

    @property
    def get_title_ru(self):
        return self.ru_title

    @property
    def get_text_en(self, ):
        return self.en_text

    @property
    def get_title_en(self):
        return self.en_title

    @property
    def get_text_kz(self, ):
        return self.kz_text

    @property
    def get_title_kz(self):
        return self.kz_title

    class Meta:
        verbose_name = "Начальная Страница"
        verbose_name_plural = "Начальная Страница"

#


class Society_Images(Base_Images):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, related_name="images")


class Education_Images(Base_Images):
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name="images")


class Protocols_Images(Base_Images):
    protocols = models.ForeignKey(Protocols, on_delete=models.CASCADE, related_name="images")


class Event_Images(Base_Images):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images")


class News_Images(Base_Images):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="images")


#


#


class PDF_Society(Base_Pdf):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, related_name="pdfs")


class PDF_Education(Base_Pdf):
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name="pdfs")


class PDF_Protocols(Base_Pdf):
    protocols = models.ForeignKey(Protocols, on_delete=models.CASCADE, related_name="pdfs")


class PDF_Event(Base_Pdf):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="pdfs")


class PDF_News(Base_Pdf):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="pdfs")
