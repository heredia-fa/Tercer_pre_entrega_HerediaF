from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    age= models.IntegerField()
    favorite_game = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.lastname}" 
    
#Cambiar por  charfiel
class Game_table(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    date=models.DateField(auto_now=False, auto_now_add=False)
    players = models.ManyToManyField('User', related_name='tables', blank=True)
    max_players = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def add_player(self, player):
        self.players.add(player)

    def free_places(self):
       cant= self.max_players - self.players.count()
       return cant


#Quisiera  agregar una foto,  tengo que buscar como.
class New(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date=models.DateField(auto_now=False, auto_now_add=True)
            
#Borrar
class Game(models.Model):
    name = models.CharField(max_length=30)
    

    
