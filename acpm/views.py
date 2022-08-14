from itertools import chain

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Society, News, Education, Protocols, Event, Index
from .serializers import (SocietyListSerializerRU, SocietyListSerializerEN, SocietyListSerializerKZ,
                          EventListSerializerEN, EventListSerializerRU, EventListSerializerKZ,
                          SearchListSerializerKZ, SearchListSerializerEN, SearchListSerializerRU,
                          CategoriesSerializerEN, CategoriesSerializerKZ, CategoriesSerializerRU,
                          IndexSerializerKZ, IndexSerializerEN, IndexSerializerRU,
                          EventCategoriesSerializerEN, EventCategoriesSerializerKZ, EventCategoriesSerializerRU,
                          NewsListSerializer)
from django.db.models import Q


class CustomDetail(APIView):
    permission_classes = [permissions.AllowAny]
    state_serializer = None
    state_model = None

    def get(self, request, pk):
        post = self.state_model.objects.filter(id=pk, draft=False)
        serializer = self.state_serializer(post, many=True)
        serializer.data[0]['text'] = serializer.data[0]['text'].replace('\r\n', '')
        return Response(serializer.data)


class CustomNavigation(APIView):
    permission_classes = [permissions.AllowAny]
    state_serializer = None
    state_model = None

    def get(self, request, language, category):
        posts = self.state_model.objects.order_by('-date').filter(category=category, draft=False)
        if language == 'ru':
            serializer = SocietyListSerializerRU(posts, many=True)
        elif language == 'en':
            serializer = SocietyListSerializerEN(posts, many=True)
        else:
            serializer = SocietyListSerializerKZ(posts, many=True)
        serializer.data[0]['text'] = serializer.data[0]['text'].replace('\r\n', '')
        return Response(serializer.data)


class CustomCategoriesView(APIView):
    permission_classes = [permissions.AllowAny]
    state_model = None

    def get(self, request, language):
        if language == 'ru':
            serializers = CategoriesSerializerRU
        elif language == 'kz':
            serializers = CategoriesSerializerKZ
        else:
            serializers = CategoriesSerializerEN
        posts = self.state_model.objects.order_by('id').distinct()
        serializer = serializers(posts, many=True)
        return Response(serializer.data)

#


class SocietyDetailView(CustomDetail):
    state_model = Society


class EducationDetailView(CustomDetail):
    state_model = Education


class NewsDetailView(CustomDetail):
    state_model = News
    state_serializer = NewsListSerializer


# class EventDetailView(CustomDetail):
#     state_model = Event
#     state_serializer = EventListSerializer


class ProtocolsDetailView(CustomDetail):
    state_model = Protocols


#


class SocietyNavigationView(CustomNavigation):
    state_model = Society


class EducationNavigationView(CustomNavigation):
    state_model = Education


class ProtocolsNavigationView(CustomNavigation):
    state_model = Protocols


class EventNavigationView(CustomNavigation):
    permission_classes = [permissions.AllowAny]

    def get(self, request, language, category):
        posts = Event.objects.order_by('-date').filter(category=category, draft=False)
        if language == 'ru':
            serializer = EventListSerializerRU(posts, many=True)
        elif language == 'en':
            serializer = EventListSerializerEN(posts, many=True)
        else:
            serializer = EventListSerializerKZ(posts, many=True)
        serializer.data[0]['text'] = serializer.data[0]['text'].replace('\r\n', '')
        return Response(serializer.data)


#


class SocietyCategoriesView(CustomCategoriesView):
    state_model = Society


class EducationCategoriesView(CustomCategoriesView):
    state_model = Education


class ProtocolsCategoriesView(CustomCategoriesView):
    state_model = Protocols


class EventCategoriesView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, language):
        if language == 'ru':
            serializers = EventCategoriesSerializerRU
        elif language == 'kz':
            serializers = EventCategoriesSerializerKZ
        else:
            serializers = EventCategoriesSerializerEN
        posts = Event.objects.order_by('id').distinct()
        serializer = serializers(posts, many=True)
        return Response(serializer.data)


#


class IndexNavigationView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, language, category):
        posts = Index.objects.filter(category=category)
        if language == 'ru':
            serializers = IndexSerializerRU
        elif language == 'kz':
            serializers = IndexSerializerKZ
        else:
            serializers = IndexSerializerEN
        serializer = serializers(posts, many=True)
        serializer.data[0]['text'] = serializer.data[0]['text'].replace('\r\n', '')
        return Response(serializer.data)


#


class NewsListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, language):
        posts = News.objects.order_by('-date').filter(language=language, draft=False)
        serializer = NewsListSerializer(posts, many=True)
        serializer.data[0]['text'] = serializer.data[0]['text'].replace('\r\n', '')
        return Response(serializer.data)


class SearchDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, language, search):
        ru_search = Q(ru_title__icontains=search) | Q(ru_text__icontains=search)
        en_search = Q(en_title__icontains=search) | Q(en_text__icontains=search)
        kz_search = Q(kz_title__icontains=search) | Q(kz_text__icontains=search)
        if language == 'ru':
            serializers = SearchListSerializerRU
            education = Education.objects.filter(ru_search)
            news = News.objects.filter(Q(title__icontains=search) | Q(text__icontains=search))
            society = Society.objects.filter(ru_search)
            protocols = Protocols.objects.filter(ru_search)
            event = Event.objects.filter(ru_search)
        elif language == 'kz':
            serializers = SearchListSerializerKZ
            education = Education.objects.filter(kz_search)
            news = News.objects.filter(Q(title__icontains=search) | Q(text__icontains=search))
            society = Society.objects.filter(kz_search)
            protocols = Protocols.objects.filter(kz_search)
            event = Event.objects.filter(kz_search)
        else:
            serializers = SearchListSerializerEN
            education = Education.objects.filter(en_search)
            news = News.objects.filter(Q(title__icontains=search) | Q(text__icontains=search))
            society = Society.objects.filter(en_search)
            protocols = Protocols.objects.filter(en_search)
            event = Event.objects.filter(en_search)
        result_list = list(chain(education, society, protocols, event,))
        serializer1 = NewsListSerializer(news, many=True)
        serializer2 = serializers(result_list, many=True)
        return Response(serializer2.data + serializer1.data)
