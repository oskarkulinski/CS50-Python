name = input('What is the name of your file? ')
name = name.strip().lower()


if name.endswith('.gif')==True:
    print('image/gif')
elif name.endswith('jpg') ==True | name.endswith('jpeg') == True:
    print('image/jpeg')
elif  name.endswith('png') == True:
    print('image/png')
elif name.endswith('pdf')==True:
    print('application/pdf')
elif name.endswith('txt')==True:
    print('text/plain')
elif name.endswith('zip')==True:
    print('application/zip')
else:
    print('application/octet-stream')