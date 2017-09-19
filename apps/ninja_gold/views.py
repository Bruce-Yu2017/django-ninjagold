from django.shortcuts import render, redirect
import random
import datetime

def index(request):
  if not 'result' in request.session:
    request.session['message'] = []
    request.session['result'] = 0
  return render(request, "ninja_gold/ninja_gold.html")

def process(request):
  if request.POST['building'] == 'farm':
    # request.session['newearn'] = random.randint(10,20)
    request.session['result'] += random.randint(10,20)
    request.session['message'].append('Earned ' + str(random.randint(10,20)) + ' golds from the farm!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
    return redirect("/")
  
  if request.POST['building'] == 'cave':
    # session['newearn'] = random.randint(5,10)
    request.session['result'] += random.randint(5,10)
    request.session['message'].append('Earned ' + str(random.randint(5,10)) + ' golds from the cave!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
    return redirect("/")

  if request.POST['building'] == 'house':
    # session['newearn'] = random.randint(2,5)
    request.session['result'] += random.randint(2,5)
    request.session['message'].append('Earned ' + str(random.randint(2,5)) + ' golds from the house!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
    return redirect("/")

  if request.POST['building'] == 'casino':
    # session['newearn'] = random.randint(-50,50)
    request.session['result'] += random.randint(-50,50)
    if random.randint(-50,50) >= 0:
      request.session['message'].append('Entered a casino and earned ' + str(random.randint(-50,50)) + ' golds from the casino!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
    elif random.randint(-50,50) < 0:
      if request.session['result'] >= 0:
        request.session['message'].append('Entered a casino and lost ' + str(abs(random.randint(-50,50))) + ' golds from the casino!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
      elif request.session['result'] < 0:
        request.session['message'].append('Now you owe us ' + str(request.session['result']) + ' gold!')
    return redirect("/")

def reset(request):
  request.session['message'] = []
  request.session['result'] = 0
  return redirect('/')
