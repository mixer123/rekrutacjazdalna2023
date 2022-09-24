from django.contrib.admin import display
from django.urls import path

from import_export import resources
from import_export.admin import ExportMixin
from django.contrib import admin
from import_export.fields import Field
from .forms import UserForm, UserChangeForm, UserForm1, UserForm2
from .models import *
from import_export.formats import base_formats
from django.core.mail import EmailMessage
from django.forms import TextInput, Textarea
class KandydatInline(admin.TabularInline):
    model = Kandydat
    exclude = ['last_login']

class UserAdmin(admin.ModelAdmin):


    form = UserForm2
    add_form = UserForm1
    # Pole username jest readonly gdy uaktualizujemy obiekt. Gdy tworzymy nowy to jest edytowalne
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["username","password"]
        else:
            return []
    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj:
            defaults['form'] = self.add_form
        if obj is None:
            defaults['form'] = self.form
        defaults.update(kwargs)
        # return super().get_form(request, obj, **defaults)
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['password'].disabled = False
        return form

    list_display = ['username', 'first_name','last_name','pesel']


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

admin.site.register(User, UserAdmin)

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
    # pesel = Field(attribute="user__pesel" ,  column_name = "Pesel")
    # dokument = Field(attribute="document__name", column_name="Dokument")
    suma_pkt = Field(attribute="suma_pkt", column_name="Pkt")
    class Meta:
        model = Kandydat
        # skip_unchanged = True
        # report_skipped = True
        fields = ('suma_pkt')


class ReadOnlyMixin(): # Add inheritance from "object" if using Python 2
    list_display_links = None



class KandydatAdmin(ExportMixin, admin.ModelAdmin):
    # form = KandydatFormAdmin

    # change_list_template = "admin/licznik/kandydat/post_changelist.html"
    #Wyłaczenie dodawania kandydata ustaw na False

    def has_add_permission(self, request, obj=None):
        return True


    # Pole user będzie readonly gdy obiekt jest aktualizowany gdy tworzę nowy obiekt to  będzie edytowalne
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['user']
        else:
            return []
#''' W ten sposób dodajemy foreignkey do list_display; ordering odpowiedzialne jest za sortowanie'''
    @display(ordering='user__last_name',description='Nazwisko i imię')
    def get_first_name_last_name(self, obj):
        return f'{obj.user.last_name} {obj.user.first_name} '

    @display(ordering='user__pesel', description='Pesel')
    def get_pesel(self, obj):
        return f'{obj.user.pesel} '

    list_display = ['get_first_name_last_name','get_pesel','user','document', 'clas','suma_pkt']
    search_fields = ['user__last_name', 'user__pesel', 'user__first_name', 'user__second_name']
    list_filter = ['document', 'clas', 'clas__school']
    # readonly_fields = ['user']
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
        return HttpResponseRedirect('/zestawienie/')


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
        email = EmailMessage(
             obj.title,f'Witaj<br>  {obj.text}<br> <i>Prosimy nie odpowiadać na tą wiadomość</i>.\n <i>Ta wiadomość została wygenerowana automatycznie.</i> ','',[''],receivers,reply_to=['automat@ecompus.pl']
        )
        email.content_subtype = "html"
        email.send(fail_silently=True)
        return super(PostAdmin, self).save_model(request, obj, form, change)
    change_list_template = "admin/licznik/post/post_changelist.html"
    list_display = ['text', 'date']
    search_fields = ['text', 'date']
    list_filter = ['text', 'date']
    list_per_page = 20


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(School, SchoolAdmin)


class StatusAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        for stat in Status.objects.all():
            stat.delete()
        return super(StatusAdmin, self).save_model(request, obj, form, change)


admin.site.register(Status, StatusAdmin)
