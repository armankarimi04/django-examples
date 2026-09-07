from django.db import models

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Film(models.Model):
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('sci-fi', 'Science Fiction'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('documentary', 'Documentary'),
        ('animation', 'Animation'),
        ('fantasy', 'Fantasy'),
    ]
    
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="Rating from 0.0 to 10.0"
    )
    synopsis = models.TextField(max_length=500, blank=True)
    duration_minutes = models.PositiveIntegerField(help_text="Duration in minutes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-release_year', 'title']
        verbose_name = 'Film'
        verbose_name_plural = 'Films'
    
    def __str__(self):
        return f"{self.title} ({self.release_year})"
    
    @property
    def duration_display(self):
        """Convert minutes to hours and minutes format"""
        hours = self.duration_minutes // 60
        minutes = self.duration_minutes % 60
        if hours > 0:
            return f"{hours}h {minutes}m"
        return f"{minutes}m"