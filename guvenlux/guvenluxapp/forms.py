from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError


class ProductImageInlineFormSet(BaseInlineFormSet):
    """
    Custom inline formset for validating the number of images attached to a product.

    Ensures that no more than 3 images are uploaded for a single product.
    This validation is applied when saving related inline image forms
    in the Django admin or other inline formset contexts.
    """
    def clean(self):
        """
        Validates that the number of non-deleted images does not exceed 3.

        Raises:
            ValidationError: If more than 3 images are submitted.
        """
        super().clean()
        total_images = 0
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                total_images += 1
        if total_images > 3:
            raise ValidationError('Bir məhsula maksimum 3 şəkil əlavə etmək olar.')