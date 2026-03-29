from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    theme_class = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GameStat(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    value = models.CharField(max_length=50)