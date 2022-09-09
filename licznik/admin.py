

from django.http import HttpResponseRedirect
from django.urls import path
from django.shortcuts import redirect
from import_export import resources
from import_export.admin import ExportMixin, ImportMixin
from django.contrib import messages
# from django_object_actions import DjangoObjectActions
from django.urls import reverse
# from admin_tools.menu import items, Menu
from django.contrib import admin
from import_export.fields import Field
from import_export.forms import ImportForm, ConfirmImportForm

from .models import *
from import_export.admin import ImportExportMixin
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportExportModelAdmin
from django import forms
from import_export.formats import base_formats
from django.core.mail import send_mail
from django.conf import settings
import smtplib, ssl
from django.core.mail import EmailMessage

class KandydatInline(admin.TabularInline):
    model = Kandydat
    exclude = ['last_login']
# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name','last_name','pesel']
    # readonly_fields = ['username']
    exclude = ['last_login','groups','password']
    inlines = [
        KandydatInline,
    ]


class MyUserAdmin(UserAdmin):

    def has_delete_permission(self, request, obj=None):
       if obj is None:
           return True
       else:
           # raise ValidationError('Nie wolno')

          return not obj.is_superuser
# admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

class KlasaAdmin(admin.ModelAdmin):
    list_display = ['name','school']


admin.site.register(Klasa, KlasaAdmin)


class OryginalAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Oryginal, OryginalAdmin)


class OcenaAdmin(admin.ModelAdmin):
    list_display = ['ocena']


admin.site.register(Ocena, OcenaAdmin)

# admin.site.register(Upload)

class KandydatResources(resources.ModelResource):

    user_last_name = Field(attribute="user__last_name", column_name="Nazwisko")
    first_name1 = Field(attribute="user__first_name", column_name='Imię1')
    second_name2 = Field(attribute="user__second_name", column_name='Imię2')
    pesel = Field(attribute="user__pesel" ,  column_name = "Pesel")
    dokument = Field(attribute="document__name", column_name="Dokument")
    suma_pkt = Field(attribute="suma_pkt", column_name="Pkt")
    class Meta:
        model = Kandydat
        # skip_unchanged = True
        # report_skipped = True
        fields = ('suma_pkt')


class ReadOnlyMixin(): # Add inheritance from "object" if using Python 2
    list_display_links = None



class KandydatAdmin(ReadOnlyMixin  ,ExportMixin, admin.ModelAdmin):
    # change_list_template = "admin/licznik/kandydat/post_changelist.html"
    def has_add_permission(self, request, obj=None):
        return False

    list_display = ['user','document', 'clas','suma_pkt']
    search_fields = ['user__last_name', 'user__pesel','document__name','user__first_name','user__second_name','user__last_name','clas__name']
    list_filter = ['document', 'clas','clas__school']
    readonly_fields = ['user']
    resource_class = KandydatResources
    list_per_page = 20


    def get_export_formats(self):

        formats = (
            base_formats.CSV,
            base_formats.XLS,

        )
        return [f for f in formats if f().can_export()]



    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('wp/', self.import2),

        ]
        return my_urls + urls


    def import2(request, queryset):
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(f'/zestawienie/')


admin.site.register(Kandydat, KandydatAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        receivers = []
        for receiver in User.objects.all():
            receivers.append(receiver.email)
        users = []
        for user  in User.objects.all():
            users.append(user.username)
        # send_mail(obj.title, obj.text,
        #           settings.EMAIL_HOST_USER,
        #           receivers, fail_silently=False)

        email = EmailMessage(
             obj.title,f'Witaj  {obj.text}','',[''],receivers,reply_to=['automat@ecompus.pl']
        )
        email.content_subtype = "html"
        email.send(fail_silently=True)
        return super(PostAdmin, self).save_model(request, obj, form, change)

    # actions = [send_emails]
    change_list_template = "admin/licznik/post/post_changelist.html"

    # def response_change(self, request, obj):
    #     if "_make-unique" in request.POST:
    #         matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
    #         matching_names_except_this.delete()
    #         obj.is_unique = True
    #         obj.save()
    #         self.message_user(request, "This villain is now unique")
    #         return HttpResponseRedirect(".")
    #     return super().response_change(request, obj)

    list_display = ['text','date']
    search_fields = ['text','date']
    list_filter = ['text','date']
    list_per_page = 20


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(School, SchoolAdmin)
# admin.site.register(Status)