from django import forms
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)

class ContactForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3),
            RegexValidator(
                regex="^[A-Za-z ]+$",
                message="Name can only contain letters."
            )
        ],
        error_messages={
            "required": "Please enter your name."
        }
    )

    email = forms.EmailField()

    age = forms.IntegerField(
        validators=[
            MinValueValidator(18),
            MaxValueValidator(60)
        ]
    )

    subject = forms.CharField(
        max_length=150,
        validators=[
            MaxLengthValidator(150)
        ]
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows":5,
                "placeholder":"Enter your message"
            }
        )
    )

    def clean_name(self):

        name = self.cleaned_data["name"]

        if name.lower() == "admin":
            raise forms.ValidationError(
                "Admin is not allowed."
            )

        return name

    def clean(self):

        cleaned_data = super().clean()

        subject = cleaned_data.get("subject")
        message = cleaned_data.get("message")

        if subject and message:

            if subject.lower() in message.lower():

                raise forms.ValidationError(
                    "Subject should not be repeated in message."
                )

        return cleaned_data