from django.apps import apps
from django.contrib import admin

# Register your models here.
app = apps.get_app_config('usermanagement')


class Users(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active',)

    def is_active(self, obj):
        return not bool(obj.deleted_at)

    is_active.boolean = True


for model_name, model in app.models.items():
	if model_name == 'user':
		admin.site.register(model, Users)#admin.site.register(model)

