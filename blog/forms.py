from django import forms


class PostSearchForm(forms.Form):
    s = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["s"].widget.attrs.update({"class": "form-control"})
