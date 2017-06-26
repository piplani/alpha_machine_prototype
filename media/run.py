from PIL import Image as im
import numpy as np
from matplotlib import pyplot as plt
import csv
import os
import smtplib


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


import sys

# from webapp.views import dirname
machine_learning_R_models = ['decisionTree', 'randomForest', 'linearModel', 'neuralNetwork']
dataset = 'regressionDataSet.csv'
tail1 = '-Evaluation-Result.csv'
tail2 = '-ScatterPlot.png'
# running our models now
file = open('dir.txt', 'r')
dirname = file.read()
file.close()
print (os.getcwd())
for model in machine_learning_R_models:
    os.system('Rscript ' + os.getcwd() + '/media/' + dirname + '/' + model + '.R')
plots_array = []
results_array = []
pa = '/home/nightfury/PycharmProjects/alpha/media/' + dirname
for i in machine_learning_R_models:
    plots_array.append(pa + '/' + i + tail2)
    results_array.append(pa + '/' + i + tail1)

# loading images
# os.system('cd /home/nightfury/PycharmProjects/alpha/media/'+dirname)
# sys.path.append('/home/nightfury/PycharmProjects/alpha/media/' + dirname)
imagesarray = []
for img in plots_array:
    i = im.open(img)
    iar = np.array(i)
    imagesarray.append(iar)
c = 0
file = open(pa + '/results.txt', 'w')
for i in results_array:
    with open(i, 'rb') as csvfile:
        reade = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reade:
            s = row[0].split(',')
            if c == 0 or c % 2 == 1:
                file.write(s[0] + "  " + s[4] + '\n')
            c += 1
# os.system('gedit results.txt')
file.close()
file2 = open(pa + '/results.txt', 'r')
file1 = open('email.txt', 'r')
sendmail(file1.read(), file2.read())
fig = plt.figure()
ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)

ax1.imshow(imagesarray[0])
ax2.imshow(imagesarray[1])
ax3.imshow(imagesarray[2])
ax4.imshow(imagesarray[3])
plt.savefig(pa + '/result.png')
# plt.show()
