import zbar, requests, cStringIO, pyotp
from PIL import Image

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
    resp = s.post('http://127.0.0.1:8081', data={'password':totp.now()}).text
    print resp
    
