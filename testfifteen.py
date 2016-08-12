'test 15'
import re

'15-1'
p1 = 'bat|bit|but|hat|hit|hut'
p1 = r'[bh][aiu]t'
s1 = 'hbat bitt sd dsad ht hutta'
m1 = re.findall(p1, s1)
if m1 is not None:
	print m1


'15-2'
p2 = r'[A-Za-z]+\s[A-Za-z]+\s'

s2 = '2abc wojsfd'
f2 = open('test15.txt', 'r')
for eachLine in f2.readlines():
	m2 = re.search(p2, eachLine.strip())
	if m2 is not None:
		print m2.group()

'15-3'
p2 = r'[A-Za-z]+,\s[A-Za-z]\s'
f2 = open('test15.txt', 'r')
for eachLine in f2.readlines():
	m2 = re.search(p2, eachLine.strip())
	if m2 is not None:
		print m2.group()

'15-4'
p4 = '[A-Za-z_]\w*'


'15-5'
p5 = r'[0-9]{4}(\s[a-zA-Z]+)+[\s]'
f5 = open('test15.txt', 'r')
for eachLine in f5.readlines():
	m5 = re.search(p5, eachLine)
	if m5 is not None:
		print m5.group()

'15-6'
p6 = r'www\.[\w]+\.com[\s]'
f6 = open('test15.txt', 'r')
for eachLine in f6.readlines():
	m6 = re.search(p6, eachLine)
	if m6 is not None:
		print m6.group()


'15-7'
p7 = r'0|[1-9]+'
f7 = open('test15.txt', 'r')
for eachLine in f7.readlines():
	m7 = re.search(p7, eachLine.strip())
	if m7 is not None:
		print m7.group()

'15-9'
p9 = r'\d+(\.\d+)?'

'15-10'
p10 = r'\d+([\+-](\d+)?j)?'
f10 = open('test15.txt', 'r')
for eachLine in f10.readlines():
	m10 = re.search(p10, eachLine.strip())
	if m10 is not None:
		print m10.group()

'15-11'
p11 = r'\w+@\w+\.com(\.\w+)?'

'15-12'
p12 = r'http(s)?:\\\\www\.\w+\.\w+(\.\w+)?'
f12 = open('test15.txt', 'r')
for eachLine in f12.readlines():
	m12 = re.search(p12, eachLine.strip())
	if m12 is not None:
		print m12.group()

'15-13'
p13 = r"'[A-Za-z_]+'"
f13 = open('test15.txt', 'r')
for eachLine in f13.readlines():
	m13 = re.search(p13, eachLine.strip())
	if m13 is not None:
		print m13.group()

'15-14'
p14 = '[1][0|1|2]'
f14 = open('test15.txt', 'r')
for eachLine in f14.readlines():
	m14 = re.search(p14, eachLine.strip())
	if m14 is not None:
		print m14.group()

'15-15'
p15 = '\d{4}-\d{6}-\d{5}|\d{4}-\d{4}-\d{4}-\d{4}'
f15 = open('test15.txt', 'r')
for eachLine in f15.readlines():
	m15 = re.search(p15, eachLine.strip())
	if m15 is not None:
		print m15.group()
	else:
		print eachLine.strip(),' is useless'


'15-17'
p16 = r'^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
f16 = open('redata459.txt', 'r')
d16 = {'Mon':0, 'Tue':0, 'Wed':0, 'Thu':0, 'Fri':0, 'Sat':0, 'Sun':0}

for eachLine in f16.readlines():
	m16 = re.match(p16, eachLine.strip())

	if m16 is not None:
		d16[m16.group()] = d16[m16.group()] + 1

for eachKey in d16.keys():
	print eachKey, d16[eachKey]

p16 = r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b'
f16 = open('redata459.txt', 'r')
d16 = {'Jan':0, 'Feb':0, 'Mar':0, 'Apr':0, 'May':0, 'Jun':0, 'Jul':0, 'Aug':0, 'Sep':0, 'Oct':0, 'Nov':0, 'Dec':0}

for eachLine in f16.readlines():
	m16 = re.search(p16, eachLine.strip())

	if m16 is not None:
		d16[m16.group()] = d16[m16.group()] + 1

for eachKey in d16.keys():
	print eachKey, d16[eachKey]

'15-19'
p19 = r'[\w\s\:]+[\d]{4}'
f19 = open('redata459.txt', 'r')

for eachLine in f19.readlines():
	m19 = re.search(p19, eachLine.strip())

	if m19 is not None:
		print m19.group()

'15-20'
p20 = r'[a-z]+@[a-z]+\.(org|com|edu|net|gov)'
f20 = open('redata459.txt', 'r')

for eachLine in f20.readlines():
	m20 = re.search(p20, eachLine.strip())

	if m20 is not None:
		print m20.group()

'15-21'
p21 = r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b'
f21 = open('redata459.txt', 'r')

for eachLine in f21.readlines():
	m21 = re.search(p21, eachLine.strip())

	if m21 is not None:
		print m21.group()

'15-22'
p22 = r'[\d]{4}'
f22 = open('redata459.txt', 'r')

for eachLine in f22.readlines():
	m22 = re.search(p22, eachLine.strip())

	if m22 is not None:
		print m22.group()

'15-23'
p23 = r'[\d]{2}\:[\d]{2}\:[\d]{2}'
f23 = open('redata459.txt', 'r')

for eachLine in f23.readlines():
	m23 = re.search(p23, eachLine.strip())

	if m23 is not None:
		print m23.group()


'15-24'

'15-25'
p25 = r'[a-z]+@([a-z]+)\.(org|com|edu|net|gov)'
f25 = open('redata459.txt', 'r')

for eachLine in f25.readlines():
	m25 = re.search(p25, eachLine.strip())

	if m25 is not None:
		print m25.group()
		print m25.group(1), m25.group(2)

'15-26'
p26 = r'[a-z]+@[a-z]+\.(org|com|edu|net|gov)'
f26 = open('redata459.txt', 'r')

for eachLine in f26.readlines():
	m26 = re.sub(p26, '123@456.com', eachLine.strip())
	print m26


'15-27'
p27 = r'([a-zA-Z]{3}\s[\d]{2}).+([\d]{4})'
f27 = open('redata459.txt', 'r')

for eachLine in f27.readlines():
	m27 = re.search(p27, eachLine.strip())

	if m27 is not None:
		print m27.group(1),",", m27.group(2)

'15-28'
p28 = r'(\d{3}-)?\d{3}-\d{4}'
f28 = open('test15.txt', 'r')

for eachLine in f28.readlines():
	m28 = re.search(p28, eachLine.strip())

	if m28 is not None:
		print m28.group()

'15-29'
p29 = r'(\(\d{3}\)|\d{3}-)?\d{3}-\d{4}'
f29 = open('test15.txt', 'r')

for eachLine in f29.readlines():
	m29 = re.search(p29, eachLine.strip())

	if m29 is not None:
		print m29.group()


