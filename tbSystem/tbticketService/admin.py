from django.contrib import admin
from tbticketService.models.models import TrainJourney

@admin.register(TrainJourney)
class TrainJourneyAdmin(admin.ModelAdmin):
    list_display = ("id","passenger", "start_station", "end_station", "train","seat_number",)
    list_filter = ("id","passenger", "start_station", "end_station", "train","seat_number",)


