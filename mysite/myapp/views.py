from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.
def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        return redirect('index')

    consumed_food = Consume.objects.filter(user = request.user)
    foods = Food.objects.all()
    context = {
        "foods":foods,
        "consumed_food" : consumed_food,
    }
    return render(request, 'myapp/index.html', context)

def delete(request, id):
    Consume.objects.get(id=id).delete()
    return redirect('index')