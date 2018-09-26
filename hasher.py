import hashlib
import os

# BLOCKSIZE is arbitrary
BLOCKSIZE = 65536 #Lets it read stuff in 64kb chuncks!
md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 =hashlib.sha256()
print(r"""

   ██░ ██  ▄▄▄        ██████  ██░ ██      ██████  ██▓     ██▓ ███▄    █   ▄████  ██▓ ███▄    █   ▄████
  ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒   ▒██    ▒ ▓██▒    ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓██▒ ██ ▀█   █  ██▒ ▀█▒
  ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░   ░ ▓██▄   ▒██░    ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
  ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██      ▒   ██▒▒██░    ░██░▓██▒  ▐▌██▒░▓█  ██▓░██░▓██▒  ▐▌██▒░▓█  ██▓
  ░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓   ▒██████▒▒░██████▒░██░▒██░   ▓██░░▒▓███▀▒░██░▒██░   ▓██░░▒▓███▀▒
   ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒   ▒ ▒▓▒ ▒ ░░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒
   ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░   ░ ░▒  ░ ░░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░  ░   ░  ▒ ░░ ░░   ░ ▒░  ░   ░
   ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░   ░  ░  ░    ░ ░    ▒ ░   ░   ░ ░ ░ ░   ░  ▒ ░   ░   ░ ░ ░ ░   ░
   ░  ░  ░      ░  ░      ░   ░  ░  ░         ░      ░  ░ ░           ░       ░  ░           ░       ░

               ██░ ██  ▄▄▄        ██████  ██░ ██ ▓█████  ██▀███
              ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
              ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒███   ▓██ ░▄█ ▒
              ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄
              ░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░▒████▒░██▓ ▒██▒
               ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
              ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
               ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░   ░     ░░   ░
               ░  ░  ░      ░  ░      ░   ░  ░  ░   ░  ░   ░     """)
print("Only use a relative path if your file resides here:  " + os.getcwd())
var2 = input("What file shall I sla..*ahem* hash? (include extension): ")
print(var2)
with open(var2, 'rb') as afile:
    while True:
        data = afile.read(BLOCKSIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)
        sha256.update(data)
print("MD5: {0}".format(md5.hexdigest()))
print("SHA1: {0}".format(sha1.hexdigest()))
print("SHA256: {0}".format(sha256.hexdigest()))
