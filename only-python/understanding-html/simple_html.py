from bs4 import BeautifulSoup

HTML_SAMPLE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Python</title>
</head>
<body>
    <h1> HI! Heading tag </h1>
    <p class = "subtitle"> here a p </p>
    <p class = 'second'>
        <a href='home/download/index.html' class = 'achorTag' title='A Book'>Book</a>
    </p>
    <ul>
        <li>Umesh</li>
        <li>Aku</li>
        <li>Moon</li>
        <li>Sad</li>
    </ul>
</body>
</html>
'''
simple_soup = BeautifulSoup(HTML_SAMPLE, 'html.parser')

h1_tag = simple_soup.find('h1')
print(h1_tag)

li_tag = simple_soup.find_all('li')
print(li_tag)

p_tag = simple_soup.find('p', {'class': 'subtitle'})
print(p_tag)

locater = 'p.second a'
itamName = simple_soup.select_one(locater)
print(itamName.attrs['title'])
print(itamName.attrs['class'])
print(itamName.attrs)
