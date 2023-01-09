import pygame

peopleCount = 0
room = 0
for i in ['todd', 'sam', 'jim', 'ralph', 'blimpy', 'tyrone']:
    peopleCount = peopleCount + 1
    room = room + 1
    if i == 'jim':
        jimDetector = print('- This is jim.')
    else:
        jimDetector = print('- not jim')
    print('room:', room, 'patient:', i,
          'people servered:', peopleCount, jimDetector)
