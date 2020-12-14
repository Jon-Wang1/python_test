department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'wzq'
COURSE_FEES_SEC = 45678.213534
COURSE_FEES_Python = 1238.51231

# line1 = 'Department1 name:' '%-15s' %department1 + 'Manager:'  '%-20s' %depart1_m + 'COURSE FEES:' + '%-20.3f'%COURSE\
# _FEES_SEC  +'THE END'
# line2 = 'Department2 name:' '%-15s' %department2 + 'Manager:'  '%-20s' %depart2_m + 'COURSE FEES:' + '%-20.3f'%COURSE\
# _FEES_Python + 'THE END'
line1 = 'Department1 name:' '{0:15}'.format(department1) + 'Manager:'  '{0:20}'.format(depart1_m) + 'COURSE FEES:' +\
        '{0:<20.2f}'.format(COURSE_FEES_SEC)  +'THE END'
line2 = 'Department2 name:' '%-15s' %department2 + 'Manager:'  '%-20s' %depart2_m + 'COURSE FEES:' + \
        '%-20.3f'%COURSE_FEES_Python + 'THE END'
line3 = 'Department2 name:' '%-15s' %department2 + 'Manager:'  '%-20s' %depart2_m + 'COURSE FEES:' + \
        '%-20.3f'%COURSE_FEES_Python + 'THE END'
line3 = 'Department2 name:' '%-15s' %department2 + 'Manager:'  '%-20s' %depart2_m + 'COURSE FEES:' + \
        '%-20.3f'%COURSE_FEES_Python + 'THE END'


length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
