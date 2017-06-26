from django.http import HttpResponse
from django.shortcuts import render
from .forms import dataform, adddata
from .models import data
import os
import smtplib
from shutil import copyfile


# Create your views here.
def sendmail(reciever, mes):
    sender = 'senderid@bla.com'  # place your email id here
    sender_pswd = '******'  # place your pswd here
    # reciever = 'piplani.rohan@gmail.com'

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender, sender_pswd)
    mail.sendmail(sender, reciever, mes)
    mail.close()


def index(request):
    file = open('dir.txt', 'w')
    file1 = open('email.txt', 'w')
    form = adddata(request.POST or None, request.FILES)
    upload = False
    dirname = ""
    new_data = None
    x = ""
    if form.is_valid():
        new_data = form.save(commit=False)
        new_data.save()
        x = new_data.id
        print (new_data.id)
        print (new_data.file.name)
        print (type(str(new_data.file.name)))
        dirname = str(new_data.id)
        # global dirname
        file.write(dirname)
        file.close()
        file1.write(new_data.email)
        file1.close()
        old_dir = '/home/nightfury/PycharmProjects/alpha/media/' + str(new_data.file.name)
        new_dir = '/home/nightfury/PycharmProjects/alpha/media/' + dirname + '/' + 'regressionDataSet.csv'
        os.mkdir(os.path.join('/home/nightfury/PycharmProjects/alpha/media', dirname))
        os.rename(old_dir, new_dir)
        # mail
        sendmail(new_data.email, dirname)
        upload = True
        processing(dirname)
    # img_path = '/home/nightfury/PycharmProjects/alpha/media/' + dirname + '/' + 'result.png'
    # os.mkdir(os.path.join('/home/nightfury/PycharmProjects/alpha/webapp/static/webapp/img', dirname))
    # os.rename(img_path, '/home/nightfury/PycharmProjects/alpha/webapp/static/webapp/img/'+dirname+'/result.png')
    print (x)
    context = {'form': form, 'upload': upload, 'x': x}
    return render(request, 'webapp/home.html', context)


def processing(dirname):
    li = ['decisionTree.R', 'linearModel.R', 'neuralNetwork.R', 'randomForest.R', 'run.py']
    pat = '/home/nightfury/PycharmProjects/alpha/media/'
    for i in li:
        copyfile(pat + i, pat + dirname + '/' + i)
    os.system('python ' + os.getcwd() + '/media/' + dirname + '/run.py')
    # print (os.getcwd())
