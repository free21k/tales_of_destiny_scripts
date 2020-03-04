'''
parse from original script to charactor and script.

'''

def parse_line(origin):
    '''
    parse from original text to charactor and script.
    :parameter {origin} : to be parsed.
    :return {charactor, script} : charactor, script
    '''
    if len(origin) <= 2:
        return None, None
    splited_line = origin.split(':')
    if len(splited_line) < 2:
        return None, origin
    charactor_name = splited_line[0]
    message = ''
    for i in range(1, len(splited_line)):
        message += splited_line[i]
    return charactor_name.strip(), message.strip()


def get_lines(file_name):
    '''
    get lines from file.
    :parameter {file_name} : to be read.
    :return {lines} : lines from file.
    '''
    file = open(file_name, 'r', encoding='UTF8')
    lines = []
    while True:
        line = file.readline()
        lines.append(line.strip())
        if not line:
            break
    file.close()
    return lines
