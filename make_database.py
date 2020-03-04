'''
parse from original script to charactor and script.

'''

from parse import get_lines, parse_line
from querys import insert_script_with_charactor_name



def insert_script(script_number):
    '''
    insert messages into messages table from script file.
    :parameter {chaptor_id} : chaptor index.
    :parameter {charactor_id} : charactor index.
    :parameter {message} : message.
    :return {} : None
    '''
    lines = get_lines('scripts/%02d.txt' % script_number)
    count = 0
    for line in lines:
        charactor, message = parse_line(line)

        if message is None:
            continue

        insert_script_with_charactor_name(1, charactor, message)
        print(count)
        count += 1


for i in range(1, 16):
    insert_script(i)
