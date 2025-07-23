from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError


# Custom form for product image count control on admin panel
class ProductImageInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        total_images = 0
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                total_images += 1
        if total_images > 3:
            raise ValidationError('Bir məhsula maksimum 3 şəkil əlavə etmək olar.')