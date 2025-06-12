from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ad")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    date = models.DateField(verbose_name="Tarix")
    time = models.TimeField(verbose_name="Vaxt")
    people = models.PositiveIntegerField(verbose_name="Nəfər sayı")
    message = models.TextField(verbose_name="Əlavə qeyd", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

    class Meta:
        verbose_name = "Rezervasiya"
        verbose_name_plural = "Rezervasiyalar"