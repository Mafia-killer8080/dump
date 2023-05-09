import os, platform,time
try:
   import requests
except:
   os.system('python -m pip uninstall urllib3 && python -m pip install urllib3')
from time import sleep
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from dump import _login
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    _login()
elif bit == '32bit':
    from d32 import main
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    main()
