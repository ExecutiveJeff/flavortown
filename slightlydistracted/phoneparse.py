import random
import datetime
from twisted.internet import task
from twisted.internet import reactor

TIMER = datetime.timedelta(minutes=1).seconds
TIME = datetime.timedelta(seconds=1).seconds

def main():
    for i in range(5000):
        l = task.LoopingCall(printout)
    l.start(TIME)
        #print cleanup


def printout():
    customer = ("(" + areacode() + ")" + " " + phonenumber() + " ") + (
    addgen() + " " + lastgen() + "," + " " + namegen() + " " + mailgen() + " ") + (
        city() + " " + state() + " " + zip() + " " + notes() + " " + dnc())

    cleanup = str(customer).strip('\n').rstrip('\n').lstrip('\n')
    print cleanup

def city():
    city = open('city.txt', 'r')
    cities = []
    for c in city:
        cities.append(c)
    cit = random.choice(cities)
    cit = cit.strip()
    return cit


def state():
    state = open('state.txt', 'r')
    states = []
    for s in state:
        states.append(s)
    stat = random.choice(states)
    stat = stat.strip()
    return stat


def zip():
    zip = open('zip.txt', 'r')
    zips = []
    for z in zip:
        zips.append(z)
    zippy = random.choice(zips)
    zippy = zippy.strip()
    return zippy

def notes():
    notes = open('note.txt', 'r')
    note = []
    for n in notes:
        note.append(n)
    nots = random.choice(note)
    nots = nots.strip()
    return nots

def areacode():
    keywords = ["510", "415", "208", "680", "910", "143", "213", "690", "462", "254", "612", "780", "760"]
    areacode = str(random.choice(keywords))
    return areacode

def phonenumber():
    keys = ["412-1412", "231-5124", "234-1565", "840-9014", "853-9182", "142-4132", "972-5124"]
    phonenumber = str(random.choice(keys))
    return phonenumber


def addgen():
    address = open('address.txt', 'r')
    addpend = []
    for i in address:
        addpend.append(i)
    addy = str(random.choice(addpend))
    addy = addy.strip()
    return addy


def namegen():
    names = open('names.txt', 'r')
    firstname = []
    for n in names:
        firstname.append(n)
    fname = str(random.choice(firstname))
    fname = fname.strip()
    return fname


def lastgen():
    last = open('last.txt', 'r')
    lastname = []
    for l in last:
        lastname.append(l)
    lname = str(random.choice(lastname))
    lname = lname.strip()
    return lname


def mailgen():
    mail = open('email.txt', 'r')
    email = []
    for e in mail:
        email.append(e)
    mail = str(random.choice(email))
    mail = mail.strip()
    return mail


def dnc():
    keys = ["DNC", "CLEAR"]
    dncstat = str(random.choice(keys))
    return dncstat

if __name__ == '__main__':
    l = task.LoopingCall(main)
    l.start(TIMER)
    reactor.run()