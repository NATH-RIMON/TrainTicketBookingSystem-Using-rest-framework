from django.contrib import admin
from tbPlatform.models.models import Train

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ("id","name", "class_status", "schedule", "departure_time","plat_form",)
    list_filter = ("id","name", "class_status", "schedule", "departure_time","plat_form",)
