from django import forms
from django.utils.translation import ugettext_lazy as _
from molo.profiles.forms import RegistrationForm


class FBRegistrationForm(RegistrationForm):
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
