import pickle
import random


def main():
    screen_play()


def names():
    notes = open('names.txt', 'r')
    note = []
    for n in notes:
        note.append(n)
    name = random.choice(note)
    name = name.strip()
    return name

def location():
    locs = open('locations.txt', 'r')
    loc = []
    for l in locs:
        loc.append(l)
    location = random.choice(loc)
    location = location.strip()
    return location

def build_line():
    chain = pickle.load(open("chain.p", "rb"))
    new_line = []
    sword1 = "BEGIN"
    sword2 = "NOW"
    while True:
        sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
        if sword2 == "END":
            break
        new_line.append(sword2)
    line = ' '.join(new_line)
    line = line + '\n'
    return line


def stage_direction():
    chain = pickle.load(open("chain.d", "rb"))
    direct = []
    sword1 = "BEGIN"
    sword2 = "NOW"
    while True:
        sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
        if sword2 == "END":
            break
        direct.append(sword2)
    stage = ' '.join(direct).upper()
    stage = stage + '\n'
    return stage


def build_diag():
    output = ''
    while len(output) < 200:
        output += (' ' + build_line())
        print output, len(output)
    return output

def screen_play():
    print build_line().title
    print '\n\n'
    print location()
    print '\n\n'
    name1 = names().upper()
    name2 = names().upper()
    print name1 + 'and' + name2 + '\n'
    print stage_direction()
    print '\n\n'
    print name1 + ':' + ' ' + build_diag() + '\n'
    print name2 + ':' + ' ' + build_diag() + '\n'
    print name1 + ' ' + stage_direction() + '\n'
    print name1 + ':' + ' ' + build_diag() + '\n'
    print 'END SCENE'

if __name__ == '__main__':
    main()
