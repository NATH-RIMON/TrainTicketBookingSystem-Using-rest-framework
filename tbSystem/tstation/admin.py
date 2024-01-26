from django.contrib import admin
from tstation.models.models import TrainStation

@admin.register(TrainStation)
class StationAdmin(admin.ModelAdmin):
    list_display = ("id","name","details","created_by",)
    list_filter = ("id","name","details","created_by",)



