from import_export.resources import ModelResource
from .models import YourModel, Fan

class YourModelResource(ModelResource):
    def before_import_row(self, row, **kwargs):
        fan_id = kwargs.get("user_selected_fan_id")  # Admin panelda tanlangan fan ID
        if fan_id:
            try:
                fan = Fan.objects.get(id=fan_id)  # Fanni bazadan topish
                row["fan"] = fan.id  # ID ni berish
            except Fan.DoesNotExist:
                pass  # Agar fan topilmasa, hech narsa qilmaymiz

    class Meta:
        model = YourModel
