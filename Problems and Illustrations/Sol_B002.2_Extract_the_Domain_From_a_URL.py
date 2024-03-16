# Prompt the user for a URL and extract the domain

# Ask for a URL
url = input('URL:\t')

# Set a default domain name to 'none
domain = 'none'

# If the URL doesn't start with 'http' and 'https', ask again
if (url[0:4] != 'http') & (url[0:5] != 'https'):
    while (url[0:4] != 'http') & (url[0:5] != 'https'):
        url = input('Please start with http or https:\t')

# If the URL starts with 'https' and doesn't contain '://' and 'www', ask again
if url[0:5] == 'https':
    while (url[5:8] != '://') & (url[8:11] != 'www'):
        url = input('URL(Use the correct format: \nhttps://www.domain_name.x:\t')

# If the URL starts with 'https' and doesn't contain '://' and 'www', ask again
elif url[0:4] == 'http':
    while (url[4:7] != '://') & (url[7:10] != 'www'):
        url = input('URL(Use the correct format: \nhttp://www.domain_name.x:\t')

# If the URL starts with 'http' and find where the last dot '.' is found and extract the domain
if url[0:4] == 'http':
    if url[-3] == '.':  # if the last dot '.' is found before 2 characters
        domain = url[11:-3]
    elif url[-4] == '.':  # if the last dot '.' is found before 3 characters
        domain = url[11:-4]
    elif url[-5] == '.':  # if the last dot '.' is found before 4 characters
        domain = url[11:-5]
    elif url[-6] == '.':  # if the last dot '.' is found before 5 characters
        domain = url[11:-6]
    elif url[-7] == '.':  # if the last dot '.' is found before 6 characters
        domain = url[11:-7]
    else:
        print('Unresolved domain name!')  # if the last dot '.' is before greater than 6 characters, print 'Unresolved'

# If the URL starts with 'https' and find where the last dot '.' is found and extract the domain
if url[0:5] == 'https':
    if url[-3] == '.':
        domain = url[12:-3]  # if the last dot '.' is found before 2 characters
    elif url[-4] == '.':
        domain = url[12:-4]  # if the last dot '.' is found before 3 characters
    elif url[-5] == '.':
        domain = url[12:-5]  # if the last dot '.' is found before 4 characters
    elif url[-6] == '.':
        domain = url[12:-6]  # if the last dot '.' is found before 5 characters
    elif url[-7] == '.':
        domain = url[12:-7]  # if the last dot '.' is found before 6 characters
    else:
        print('Unresolved domain name!')  # if the last dot '.' is before greater than 6 characters, print 'Unresolved'

print('Domain name:', domain)
