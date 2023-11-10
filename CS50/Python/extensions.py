askFileName = input("File name:")
FileName = askFileName.lower().strip()[-3:]
if FileName == "gif":
    print ('image/gif')
elif FileName == "jpg":
    print ('image/jpeg')
elif FileName == "peg":
    print ('image/jpeg')
elif FileName == "png":
    print ('image/png')
elif FileName == "pdf":
    print ('application/pdf')
elif FileName == "txt":
    print ('text/plain')
elif FileName == "zip":
    print ('application/zip')
else:
    print ('application/octet-stream')
