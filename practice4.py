'''
Created on 2017/07/21
student id 1710245
@author: WangLuming
'''

mountain = ['Fujisan', 'Kitadake', 'Okuhodakadake', 'Ainodake', 'Yarigatake', 'Warusawadake', 'Akaisidake', 'Karasawadake', 'Kitahodakadake', 'Oobamidake', 'Maehodakadake', 'Nakadake', 'Arakawanakadake', 'Ontakesan', 'Noutoridake', 'Shiomidake', 'Minamidake', 'Senjougatake', 'Norikuradake', 'Tateyama']
height = [3775, 3193, 3190, 3190, 3180, 3141, 3120, 3110, 3106, 3101, 3090, 3084, 3083, 3067, 3051, 3046, 3032, 3026, 3015]
while 1:
    inputMountain = raw_input('Enter the mountain')
    try:
        p = mountain.index(inputMountain)
        print height[p]
    except:
        print 'invalid mountain name'