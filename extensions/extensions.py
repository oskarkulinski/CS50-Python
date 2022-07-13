name = input('What is the name of your file? ')
name = name.strip().lower()
x = name.length()
type = name.removeprefix(3)

match type:
    case 'gif':
        print('image/gif')
    case 'jpg' | 'jpeg':
        print('image/jpeg')
    case  'png':
        print('image/png')
    case 'pdf':
        print('application/pdf')
    case 'txt':
        print('text/plain')
    case 'zip':
        print('application/zip')
    case _ :
        print('application/octet-stream')