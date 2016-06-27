import pickle
import random
import string


line_length = raw_input("What is the largest number of characters per dialogue? ")
line_length = int(line_length)
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


def deets():
    details = open('details.txt', 'r')
    dee = []
    for d in details:
        dee.append(d)
    deet = random.choice(dee)
    deet = deet.strip()
    return deet


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


def name_swap(line):
    name1 = names().upper()
    name2 = names().upper()
    name3 = names().upper()
    name4 = names().upper()
    line = string.replace(line, "NAME1", name1)
    line = string.replace(line, "NAME2", name2)
    line = string.replace(line, "NAME3", name3)
    line = string.replace(line, "NAME4", name4)
    return line


def build_diag():
    output = ''
    length = random.randrange(1, line_length)
    while len(output) < length:
        output += (' ' + build_line())
    return output

def screen_play():
    title = build_line()
    title = title.upper()
    print name_swap(title)
    print deets()
    print location().upper()
    name1 = names().upper()
    name2 = names().upper()
    print name1 + ' ' + 'and' + " " + name2 + '\n'
    print name_swap(stage_direction())
    print name1 + ':' + ' ' + name_swap(build_diag()) + '\n'
    print name2 + ':' + ' ' + name_swap(build_diag()) + '\n'
    print name_swap(stage_direction()) + '\n'
    print name1 + ':' + ' ' + name_swap(build_diag()) + '\n'
    print name2 + ':' + ' ' + name_swap(build_diag()) + '\n'
    print 'END SCENE'

if __name__ == '__main__':
    main()
