name = input('What is the name of your file? ')
name = name.strip().lower()
type =''
name, type = name.rsplit(sep='.', maxsplit=1)

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