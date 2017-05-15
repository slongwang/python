import urllib
import re


def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def get_img(html):
    reg = r'src="(.*?\.jpg)" size='
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    i = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % i)
        i += 1


html = get_html('http://tieba.baidu.com/p/4810104717')
# http://met-art-faces.com/met-art-mirayn-a-cromie/
print get_img(html)  