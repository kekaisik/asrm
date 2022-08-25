from django.contrib import admin
from django.core.mail import send_mail, BadHeaderError
from django.utils.safestring import mark_safe
from django import forms
from .models import (Society, Event, News, Conference, Protocols, Index,
                     Society_Images, Event_Images, News_Images, Education_Images, Protocols_Images,
                     PDF_Society, PDF_Event, PDF_News, PDF_Education, PDF_Protocols,
                     URLS_Index,
                     User, Feedback,
                     )


class EmailReply(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.email_reply:
            return
        if not obj.email_reply_text:
            return
        recipients = User.objects.values('email')
        recipients = [{'email': 'kakaisik0606@gmail.com'}]
        for mail in recipients:
            try:
                send_mail(obj.email_reply_capt, obj.email_reply_text, 'kakaisik@gmail.com', [mail['email']], html_message=obj.email_reply_text)
            except BadHeaderError:
                pass
        super().save_model(request, obj, form, change)


admin.site.register(Feedback, EmailReply)


class IndexUrl(admin.StackedInline):
    model = URLS_Index
    extra = 1


class SocietyPDF(admin.StackedInline):
    model = PDF_Society
    extra = 1


class NewsPDF(admin.StackedInline):
    model = PDF_News
    extra = 1


class EventPDF(admin.StackedInline):
    model = PDF_Event
    extra = 1


class ProtocolsPDF(admin.StackedInline):
    model = PDF_Protocols
    extra = 1


class EducationPDF(admin.StackedInline):
    model = PDF_Education
    extra = 1


class SocietyInLine(admin.StackedInline):
    model = Society_Images
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="400" ')

    get_image.short_description = "Изображение"


class EventInLine(admin.StackedInline):
    model = Event_Images
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="400" ')

    get_image.short_description = "Изображение"


class NewsInLine(admin.StackedInline):
    model = News_Images
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="400" ')

    get_image.short_description = "Изображение"


class EducationInLine(admin.StackedInline):
    model = Education_Images
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="400" ')

    get_image.short_description = "Изображение"


class ProtocolsInLine(admin.StackedInline):
    model = Protocols_Images
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="400" ')

    get_image.short_description = "Изображение"


class BaseAdmin(admin.ModelAdmin):
    list_display = ("ru_title", "category", "paid", "draft",)
    list_display_links = ("ru_title",)
    list_filter = ("category", "paid", "date", "draft",)
    # search_fields = ("title", "text",)
    save_on_top = True
    list_editable = ("paid", "draft",)
    readonly_fields = ("main_image_preview",)

    def main_image_preview(self, obj):
        return obj.main_image_preview

    main_image_preview.short_description = "Основное фото"


@admin.register(Society)
class SocietyAdmin(BaseAdmin):
    inlines = [SocietyInLine, SocietyPDF, ]


@admin.register(Event)
class EventAdmin(BaseAdmin):
    inlines = [EventInLine,EventPDF]


@admin.register(Conference)
class EventAdmin(BaseAdmin):
    inlines = [EducationInLine, EducationPDF]


@admin.register(Protocols)
class ProtocolsAdmin(BaseAdmin):
    inlines = [ProtocolsInLine, ProtocolsPDF]


@admin.register(News)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "paid", "draft", "language")
    list_display_links = ("title",)
    list_filter = ("date", "draft", "paid", "language")
    search_fields = ("title", "text")
    inlines = [NewsInLine, NewsPDF]
    save_on_top = True
    list_editable = ("paid", "draft", "language")
    readonly_fields = ("main_image_preview",)

    def main_image_preview(self, obj):
        return obj.main_image_preview

    main_image_preview.short_description = "Основное фото"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "last_name", "first_name", "paid", "expiration_date",)
    list_filter = ("paid", "expiration_date", )
    search_fields = ("username", "last_name", "first_name",)
    list_editable = ("paid", "expiration_date",)


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ("ru_title",)
    inlines = [IndexUrl,]

