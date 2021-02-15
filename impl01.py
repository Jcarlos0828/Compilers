import  Hw01_Stack_Q_Dict
def setupStack():
    mstack = Hw01_Stack_Q_Dict.stack()
    mstack.push(1)
    mstack.push(2)
    mstack.push(3)
    return mstack

def setupQueue():
    mqueue = Hw01_Stack_Q_Dict.queue()
    mqueue.push(1)
    mqueue.push(2)
    mqueue.push(3)
    return mqueue

def setUpDict():
    #Example key order
    #d, l, m, z, u, r, e, h, v, i, p, t, a, j, y, k, x, w, b, c, s, f, g, o, n, q
    hass = Hw01_Stack_Q_Dict.dictionary()
    hass.add('a',36),hass.add('b',66),hass.add('c',70),hass.add('d',2),hass.add('e',25)
    hass.add('f',74),hass.add('g',84),hass.add('h',26),hass.add('i',31),hass.add('j',46),hass.add('k',59)
    hass.add('l',4),hass.add('m',11),hass.add('n',96),hass.add('o',86),hass.add('p',33)
    hass.add('q',97),hass.add('r',25),hass.add('s',73),hass.add('t',35),hass.add('u',22)
    hass.add('v',29),hass.add('w',65),hass.add('x',60),hass.add('y',51),hass.add('z',13)
    return hass
'''
You can delete the '#' in order to execute some of the instructions of either queue, stack or dictionary
'''
# stack = setupStack()
# stack.printt()

# queue = setupQueue()
# queue.printt()

# hashs = setUpDict()
# print(hashs.keys())
# print(hashs.values())
# hashs.delete('zz')
# hashs.delete('n')
# print(hashs.keys())
# print(hashs.values())