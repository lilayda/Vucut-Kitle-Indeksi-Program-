print('''Vücut Kitle İndeksi Programı

Bilgilendirme:
VKİ 18.5'un altındaysa -------> Zayıf

VKİ 18.5 ile 25 arasındaysa ------> Normal

VKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

VKİ 30'un üstündeyse -------------> Obez''')

a = int(input('kilonuz:'))
b = float(input('boyunuz:'))
c = a/b**2
c = int(c)
print('Vücut Kitle İndeksiniz:{}'.format(c))
if c<18.5:
    print('zayıf')
elif c>18.5 and c<25:
    print('normal')
elif c>25 and c<30:
    print('fazla kilolu')
else:
    print('obez')



