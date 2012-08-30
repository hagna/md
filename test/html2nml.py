
import sys

line = sys.stdin.readline()
stack = []
i = 0
buf = ''
res = ''
TAG = 0
ATTR = 1
CONTENT = 3
ENDTAG = 4
while line:
	while line:
		s = i
		while (i < len(line) and line[i] != '<'):
			i += 1
		buf += line[s:i]
		if i == len(line):
			line = sys.stdin.readline()
			i = 0
			continue
		else:
			break
	# line[i] is the begin tag token
	j = i

	# attrs stay on the same line in this html

	while (j < len(line) and line[j] != '>' and line[j] != ' '):
		j += 1
	tagname = line[i+1:j]
	if tagname == '':
		print "no tag"
		continue
	if j < len(line) and line[j] == ' ':
		k = j
		while (k < len(line) and line[k] != '>'):
			k += 1
		attrs = line[j:k]
		stack.append((ATTR, attrs))
		j = k		
	if buf != '':
		stack.append((CONTENT, buf))	
		buf = ''
	i = j+1
	if tagname[0] == '/':
		stack.append((ENDTAG, tagname))
	else:
		stack.append((TAG, tagname))
		

last = None
for t, val in stack:
	if t == TAG:
		res += '<%s ' % val
		last = TAG
	if t == ATTR:
		val = val.strip()
		attrs = val.split(' ')
		for attr in attrs:
			i = attr.find('=')
			attr = '%s|%s' % (attr[:i], attr[i+1:].replace('"', ''))
			res += '<%s> ' % attr
		last = ATTR
	if t == CONTENT:
		if (last == ENDTAG or last == CONTENT):
			res += val
		else:
			res += '| %s' % val
		last = CONTENT
	if t == ENDTAG:
		res += '>'
		last = ENDTAG
		

print res
