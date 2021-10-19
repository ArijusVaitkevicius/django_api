from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=150)
    band_id = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.band_id.name} {self.name}'


class Song(models.Model):
    name = models.CharField(max_length=150)
    duration = models.FloatField(null=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.album_id.band_id.name} {self.album_id.name} {self.name}'


class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    SCORE_CHOICES = (
        ('1', '1 of 10'),
        ('2', '2 of 10'),
        ('3', '3 of 10'),
        ('4', '4 of 10'),
        ('5', '5 of 10'),
        ('6', '6 of 10'),
        ('7', '7 of 10'),
        ('8', '8 of 10'),
        ('9', '9 of 10'),
        ('10', '10 of 10'),
    )

    score = models.CharField(
        max_length=2,
        choices=SCORE_CHOICES,
        blank=True,
        default='10',
        help_text='Score',
    )

    def __str__(self):
        return f'{self.user}: {self.score} of 10 ({self.album_id.band_id.name} {self.album_id.name})'


class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)