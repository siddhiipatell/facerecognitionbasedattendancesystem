from django import forms


class ImageForm(forms.ModelForm):
    class Meta:
        model = Capturei
        fields = ["name", "imagefile"]
