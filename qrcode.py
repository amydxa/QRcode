import segno

cv= 'https://amydxa.github.io/Portfolio_website/'

my_first_QR_code = segno.make(cv)
my_first_QR_code.save('portfoliowebsite.png', border = 1, scale=10, dark='pink', data_dark="purple")