from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField


class RegistrationForm(forms.Form):
    username = forms.RegexField(
        regex=r'^[\w.@+-]+$',
        widget=forms.TextInput(
            attrs=dict(
                required=True,
                max_length=30,
            )
        ),
        label=_("Username"),
        error_messages={
            'invalid': _("This value must contain only letters, "
                         "numbers and underscores."),
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs=dict(
                required=True,
                render_value=False,
                type='password',
            )
        ),
        label=_("Password"),
    )
    mobile_number = PhoneNumberField(required=False)
    next = forms.CharField(required=False)

    def clean_username(self):
        if User.objects.filter(
            username__iexact=self.cleaned_data['username']
        ).exists():
            raise forms.ValidationError(_("Username already exists."))
        return self.cleaned_data['username']


class ProfilePasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs=dict(
                required=True,
                render_value=False,
                type='password',
            )
        ),
        label=_("Old Password"),
    )
    new_password = forms.CharField(
        widget=forms.TextInput(
            attrs=dict(
                required=True,
                render_value=False,
                type='password',
            )
        ),
        label=_("New Password"),
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs=dict(
                required=True,
                render_value=False,
                type='password',
            )
        ),
        label=_("Confirm Password"),
    )

    def clean(self):
        new_password = self.cleaned_data.get('new_password', None)
        confirm_password = self.cleaned_data.get('confirm_password', None)
        if (new_password and confirm_password and
                (new_password == confirm_password)):
            return self.cleaned_data
        else:
            raise forms.ValidationError(_('New passwords do not match.'))
