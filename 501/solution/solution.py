import zbar, requests, cStringIO, pyotp
from PIL import Image

#HOST = 'http://127.0.0.1'
HOST = 'http://tjctf-test.sdamashek.me'

def get_image(name):
    im = Image.open(name).convert('L')
    width, height = im.size
    raw = im.tostring()
    return zbar.Image(width, height, 'Y800', raw)

scanner = zbar.ImageScanner()

keys = []

for i in range(500):
    im = get_image('%d.png' % i)
    scanner.scan(im)
    for symbol in im:
        if str(symbol.type)=='QRCODE':
            keys.append(symbol.data.split('=')[-1]) 
    del(im)

s = requests.Session()

for key in keys:
    totp = pyotp.TOTP(key)
    print totp.now()
    resp = s.post('%s:8081' % HOST, data={'password':totp.now()}).text
    print resp
    
