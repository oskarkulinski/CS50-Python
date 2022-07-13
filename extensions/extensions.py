name = input('What is the name of your file? ')
name = name.strip().lower()
x = name.length()
type = name.removeprefix(3)


if name.endswith('.gif')==True:
    print('image/gif')
elif name.endswith('jpg') ==True | name.endswith('jpeg') == True:
    print('image/jpeg')
case  name.endswith('png') == True:
    print('image/png')
case name.endswith('pdf')==True:
    print('application/pdf')
case 'txt':
    print('text/plain')
case 'zip':
    print('application/zip')
else
    print('application/octet-stream')