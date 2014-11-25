import qrcode
import pyotp

AMOUNT = 500 # Generate 500
keys = open('keys.txt','w')

for i in range(AMOUNT):
    secret = pyotp.random_base32()
    keys.write(secret+'\n')
    totp = pyotp.TOTP(secret)
    prov_uri = totp.provisioning_uri('bobbytables@tjctf.org')
    img = qrcode.make(prov_uri)
    img.save('%d.png' % i, 'PNG')

keys.close()
