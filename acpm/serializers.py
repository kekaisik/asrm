from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import (Society, Society_Images, PDF_Society,
                     User, Event, Index, News
                    )


class UserRegistrationSerializer(UserCreateSerializer):
    # password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'fatherland', 'profession',
                  'date_of_Birth', 'phone', 'address', 'city', 'country',
                  'place_of_work', 'job',)

#


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Society_Images
        fields = ('image',)


class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF_Society
        fields = ('pdf',)


#


class SocietyListSerializerRU(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    pdfs = PDFSerializer(many=True)
    date = serializers.CharField(source='parse_date_ru', max_length=50)
    group = serializers.CharField(source='get_group')
    title = serializers.CharField(source='get_title_ru')
    text = serializers.CharField(source='get_text_ru')

    class Meta:
        model = Society
        depth = 1
        fields = ('id', 'title', 'text', 'main_image', 'paid', 'date', 'images', 'pdfs', 'group')


class SocietyListSerializerKZ(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    pdfs = PDFSerializer(many=True)
    date = serializers.CharField(source='parse_date_kz', max_length=50)
    group = serializers.CharField(source='get_group')
    title = serializers.CharField(source='get_title_kz')
    text = serializers.CharField(source='get_text_kz')

    class Meta:
        model = Society
        depth = 1
        fields = ('id', 'title', 'text', 'main_image', 'paid', 'date', 'images', 'pdfs', 'group')


class SocietyListSerializerEN(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    pdfs = PDFSerializer(many=True)
    date = serializers.CharField(source='parse_date_en', max_length=50)
    group = serializers.CharField(source='get_group')
    title = serializers.CharField(source='get_title_en')
    text = serializers.CharField(source='get_text_en')

    class Meta:
        model = Society
        depth = 1
        fields = ('id', 'title', 'text', 'main_image', 'paid', 'date', 'images', 'pdfs', 'group')


class NewsListSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    pdfs = PDFSerializer(many=True)
    date = serializers.CharField(source='parse_date', max_length=50)
    group = serializers.CharField(source='get_group')

    class Meta:
        model = News
        depth = 1
        fields = ('id', 'title', 'text', 'main_image', 'paid', 'date', 'images', 'pdfs', 'group')


class EventListSerializerKZ(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    pdfs = PDFSerializer(many=True)
    group = serializers.CharField(source='get_group')
    date = serializers.CharField(source='parse_date_kz', max_length=50)
    end_date = serializers.CharField(source='parse_end_date_kz', max_length=15)
    title = serializers.CharField(source='get_title_kz')
    text = serializers.CharField(source='get_text_kz')
    announcement = serializers.CharField(source='get_announcement_kz')

    class Meta:
        model = Event
        depth = 1
        fields = ('id', 'title', 'text', 'main_image', 'paid', 'date',
                  'end_date', 'images', 'pdfs', 'group', 'end_date', 'announcement')


class EventListSerializerRU(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    pdfs = PDFSerializer(many=True)
    group = serializers.CharField(source='get_group')
    date = serializers.CharField(source='parse_date_ru', max_length=50)
    end_date = serializers.CharField(source='parse_end_date_ru', max_length=15)
    title = serializers.CharField(source='get_title_ru')
    text = serializers.CharField(source='get_text_ru')
    announcement = serializers.CharField(source='get_announcement_ru')

    class Meta:
        model = Event
        depth = 1
        fields = ('id', 'title', 'text', 'main_image', 'paid', 'date',
                  'end_date', 'images', 'pdfs', 'group', 'end_date', 'announcement')


class EventListSerializerEN(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    pdfs = PDFSerializer(many=True)
    group = serializers.CharField(source='get_group')
    date = serializers.CharField(source='parse_date_en', max_length=50)
    end_date = serializers.CharField(source='parse_end_date_en', max_length=15)
    title = serializers.CharField(source='get_title_en')
    text = serializers.CharField(source='get_text_en')
    announcement = serializers.CharField(source='get_announcement_en')

    class Meta:
        model = Event
        depth = 1
        fields = ('id', 'title', 'text', 'main_image', 'paid', 'date',
                  'end_date', 'images', 'pdfs', 'group', 'end_date', 'announcement')


class SearchListSerializerRU(serializers.ModelSerializer):
    url = serializers.URLField(source='get_url')
    title = serializers.CharField(source='get_title_ru')

    class Meta:
        model = Event
        fields = ('title', 'url',)


class SearchListSerializerKZ(serializers.ModelSerializer):
    url = serializers.URLField(source='get_url')
    title = serializers.CharField(source='get_title_kz')

    class Meta:
        model = Event
        fields = ('title', 'url',)


class SearchListSerializerEN(serializers.ModelSerializer):
    url = serializers.URLField(source='get_url')
    title = serializers.CharField(source='get_title_en')

    class Meta:
        model = Event
        fields = ('title', 'url',)


class IndexSerializerRU(serializers.ModelSerializer):
    title = serializers.CharField(source='get_title_ru')
    text = serializers.CharField(source='get_text_ru')

    class Meta:
        model = Index
        fields = ('title', 'text',)


class IndexSerializerEN(serializers.ModelSerializer):
    title = serializers.CharField(source='get_title_en')
    text = serializers.CharField(source='get_text_en')

    class Meta:
        model = Index
        fields = ('title', 'text',)


class IndexSerializerKZ(serializers.ModelSerializer):
    title = serializers.CharField(source='get_title_kz')
    text = serializers.CharField(source='get_text_kz')

    class Meta:
        model = Index
        fields = ('title', 'text',)


class CategoriesSerializerRU(serializers.ModelSerializer):
    title = serializers.CharField(source='get_title_ru')

    class Meta:
        model = Society
        fields = ('category', 'title')


class CategoriesSerializerKZ(serializers.ModelSerializer):
    title = serializers.CharField(source='get_title_kz')

    class Meta:
        model = Society
        fields = ('category', 'title')


class CategoriesSerializerEN(serializers.ModelSerializer):
    title = serializers.CharField(source='get_title_en')

    class Meta:
        model = Society
        fields = ('category', 'title')


class EventCategoriesSerializerRU(serializers.ModelSerializer):
    title = serializers.CharField(source='get_title_ru')
    announcement = serializers.CharField(source='get_announcement_ru')
    date = serializers.CharField(source='parse_date_ru', max_length=50)
    end_date = serializers.CharField(source='parse_end_date_ru', max_length=15)

    class Meta:
        model = Society
        fields = ('category', 'title', 'announcement', 'date', 'end_date', 'main_image')


class EventCategoriesSerializerKZ(serializers.ModelSerializer):
    title = serializers.CharField(source='get_title_kz')
    announcement = serializers.CharField(source='get_announcement_kz')
    date = serializers.CharField(source='parse_date_kz', max_length=50)
    end_date = serializers.CharField(source='parse_end_date_kz', max_length=15)

    class Meta:
        model = Society
        fields = ('category', 'title', 'announcement', 'date', 'end_date', 'main_image')


class EventCategoriesSerializerEN(serializers.ModelSerializer):
    title = serializers.CharField(source='get_title_en')
    announcement = serializers.CharField(source='get_announcement_en')
    date = serializers.CharField(source='parse_date_en', max_length=50)
    end_date = serializers.CharField(source='parse_end_date_en', max_length=15)

    class Meta:
        model = Society
        fields = ('category', 'title', 'announcement', 'date', 'end_date', 'main_image')
