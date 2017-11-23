'''
Created on 2017/07/22
student id 1710245
@author: WangLuming
'''

def dict_from_list(l1, l2):
    list = {}
    i=0
    while i<len(l2):
        list[l1[i]] = l2[i]
        i+=1
    return list

name = ['Fujisan', 'Kitadake', 'Okuhodakadake', 'Ainodake', 'Yarigatake', 'Warusawadake', 'Akaisidake', 'Karasawadake', 'Kitahodakadake', 'Oobamidake', 'Maehodakadake', 'Nakadake', 'Arakawanakadake', 'Ontakesan', 'Noutoridake', 'Shiomidake', 'Minamidake', 'Senjougatake', 'Norikuradake', 'Tateyama']
height = [3775, 3193, 3190, 3190, 3180, 3141, 3120, 3110, 3106, 3101, 3090, 3084, 3083, 3067, 3051, 3046, 3032, 3026, 3015]
mountain = dict_from_list(name, height)
while 1:
    inputMountain = raw_input('Enter the mountain')
    try:
        print mountain[inputMountain]
    except:
        print 'invalid mountain name'