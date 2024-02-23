# The Get Construct

name_code = {
    '6085': 'Daniel',
    '608519': 'Natanim',
    '8519': 'Bilen'
}

print('What is your name code:')
code = input()

if code == '6085':
    print('Hell0,', name_code.get('6085', 'Not found'))
elif code == '608519':
    print('Hello,', name_code.get('608519', 'Not found'))
elif code == '8519':
    print('Hello,', name_code.get('8519', 'Not found'))
else:
    print('Not found')
