from django.shortcuts import render, redirect
from .models import (
  New,
  User,
  Game_table
)
from .forms import(
  User_form,
  Search_user_form,
  New_form,
  New_table,
  List_user
)

# Create your views here.

def home(req):
  # Tengo que cambiar la fecha a español
  new_list= New.objects.all().order_by("-date")

  return render(req, "home.html", {"new_list":new_list})

def tables(req):
  table_list = Game_table.objects.all().order_by("-date")
  my_form= List_user()

  return render(req, "tables.html", {"table_list":table_list, "my_form":my_form})

def users(req, message_in= None ):

  user_list=  User.objects.all().order_by("name")
  my_form = Search_user_form()
  context= {"user_list":user_list, "my_form":my_form}

  if message_in:
    if message_in=="1":
      context ["message"]  = "Usuario agreagado correctamente"
    else:
      context ["message"]  = "Datos incorrectos"
      

  return render(req, "users.html",context)

def search_user(req):

  my_form= Search_user_form(req.GET)

  if  my_form.is_valid():

    data= my_form.cleaned_data

    name= data['name']

    user_list= User.objects.filter(name__icontains=name)

    if user_list:

      return render(req, "search_user.html",{"name":name,"user_list":user_list})
    else:

      return render(req, "search_user.html",{"name":name,"message":"Ninguna coincidencia"})


  
  return render (req, "search_user.html")

def about(req):

  return render(req, "about.html", {})

def not_implemented(req):

  return render(req, "not_implemented.html", {})

def add_user(req):

  if req.method == 'POST':

    my_form = User_form(req.POST)


    if my_form.is_valid():

      data = my_form.cleaned_data

      new_user = User(name=data['name'], lastname=data['lastname'], email=data['email'], age=data['age'], favorite_game=data['favorite_game'])
      new_user.save()

      #NOSE si estos redirect estan bien usados, lo hice asi porque 
      #sino tenia que definir poner aqui la carga de usuarios y el formulario  nuevamente
      return redirect(users,1)
    else:
     
      return redirect(users,2)
    
  else:

    my_form= User_form()

    return render(req, "add_user.html", {"my_form": my_form})

def add_new(req):

  if req.method == 'POST':

    my_form = New_form(req.POST)


    if my_form.is_valid():

      data = my_form.cleaned_data

      new_user = New(title=data['title'], description=data['description'])
      new_user.save()

      #NOSE si estos redirect estan bien usados, lo hice asi porque 
      #sino tenia que  poner aqui la carga noticias  nuevamente
      return redirect(home)
    else:
     
      return redirect(home)
    
  else:

    my_form= New_form()

    return render(req, "add_new.html", {"my_form": my_form})

def add_table(req):

  if req.method == 'POST':

    my_form = New_table(req.POST)


    if my_form.is_valid():

      data = my_form.cleaned_data

      new_user = Game_table(name=data['name'],description=data['description'],date=data['date'],max_players=data['max_players'])
      new_user.save()

      #NOSE si estos redirect estan bien usados, lo hice asi porque 
      #sino tenia que  poner aqui la carga noticias  nuevamente
      return redirect(tables)
    else:
     
      return redirect(tables)
    
  else:

    my_form= New_table()

    return render(req, "add_table.html", {"my_form": my_form})