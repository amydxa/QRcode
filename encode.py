import segno

cv= 'https://amydxa.github.io/Portfoliowebsite/'

my_first_QR_code = segno.make(cv)
my_first_QR_code.save('portfoliowebsite.png', border = 5, scale=10, dark='pink', data_dark="purple")