'''
Author @miguelms_es www.miguelms.es
'''
import pysftp	#First install pysftp package

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

sftp = pysftp.Connection('host',username='user',password='pass', cnopts=cnopts)	# Conection data

sftp.chdir('./carpeta1/carpeta2')	# Path to be listed

print sftp.pwd
for i in range(len(sftp.listdir())):
    print sftp.listdir_attr()[i]

sftp.close()
raw_input('Click for exit...')