from django.db import models


class Exercise(models.Model):

    DIFFICULTY_CHOICES = [
        ("easy", "آسان"),
        ("medium", "متوسط"),
        ("hard", "سخت"),
    ]

    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    duration = models.PositiveIntegerField(
        help_text="مدت تمرین بر حسب ثانیه"
    )

    repetitions = models.PositiveIntegerField(
        default=0,
        help_text="تعداد تکرار؛ اگر تمرین زمانی است صفر بگذارید"
    )

    sets = models.PositiveIntegerField(
        default=1,
        help_text="تعداد ست"
    )

    rest = models.PositiveIntegerField(
        default=0,
        help_text="زمان استراحت بر حسب ثانیه"
    )

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default="easy"
    )

    image = models.ImageField(
        upload_to="exercises/images/",
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to="exercises/videos/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class DailyWorkout(models.Model):
    day = models.PositiveIntegerField(
        unique=True
    )

    def __str__(self):
        return f"روز {self.day}"


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        DailyWorkout,
        on_delete=models.CASCADE,
        related_name="workout_exercises"
    )

    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE
    )

    order = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return (
            f"روز {self.workout.day} - "
            f"{self.order} - "
            f"{self.exercise.name}"
        )