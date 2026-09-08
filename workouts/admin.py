from django.contrib import admin

from .models import (
    Exercise,
    DailyWorkout,
    WorkoutExercise
)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "duration",
        "image",
        "video",
    )


class WorkoutExerciseInline(admin.TabularInline):

    model = WorkoutExercise

    extra = 1

    ordering = (
        "order",
    )


@admin.register(DailyWorkout)
class DailyWorkoutAdmin(admin.ModelAdmin):

    list_display = (
        "day",
    )

    inlines = [
        WorkoutExerciseInline
    ]