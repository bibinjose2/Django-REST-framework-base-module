from django.apps import apps
from django.contrib import admin
from usermanagement.models import User
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.
app = apps.get_app_config('usermanagement')



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdmin(admin.ModelAdmin):
    
    # The forms to add and change user instances
    form = UserCreationForm

    list_display = ('first_name', 'last_name', 'email', 'is_active',)
    search_fields = ['first_name', 'last_name', 'email']


    fieldsets = (
        ('Personal info', {'fields': ('first_name','last_name', 'email')}),
        ('Password', {
            'description': "You can set the user's password here.",
            'fields': ('password1', 'password2'),
            
        }),
    )
    filter_horizontal = ()

    def is_active(self, obj):
        return not bool(obj.deleted_at)

    is_active.boolean = True


admin.site.register(User, UserAdmin)


