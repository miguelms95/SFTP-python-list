import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

sftp = pysftp.Connection('host',username='user',password='pass', cnopts=cnopts)

sftp.chdir('./carpeta1/carpeta2')

print sftp.pwd
for i in range(len(sftp.listdir())):
    print sftp.listdir_attr()[i]

sftp.close()
raw_input('Clic para salir...')