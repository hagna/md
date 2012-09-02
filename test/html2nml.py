
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
COMMENT = 5
comment = False
while line:
	while line:
		#print "work on line %r[%d] at %r" % (line, len(line), line[i:])
		s = i
		if comment:
			#print "searching for close comment starting at %d %r" % (i, line[i:])
			while (i < len(line) and not(line[i-2] == '-' and
						line[i-1] == '-' and
						line[i] == '>')):
				i += 1
				#print i
			if i >= len(line):
				buf += line[s:i]
				line = sys.stdin.readline()
				i = 0
				continue
			else:
				buf += line[s:i-2]
				#print "COMMENT buffer found", buf
				stack.append((COMMENT, buf))
				buf = ''
				#print "Found close comment at %d" % i
				comment = False
				break
		else:
			while (i < len(line) and line[i] != '<'):
				i += 1
				#print i
			buf += line[s:i]
			if i >= len(line):
				line = sys.stdin.readline()
				i = 0
				continue
			else:
				break
			#print "found tag token at", i
	# line[i] is the begin tag token
	j = i

	# attrs stay on the same line in this html

	while (j < len(line) and line[j] != '>' and line[j] != ' '):
		j += 1
	tagname = line[i+1:j]
	#print "found tag ", tagname	
	if tagname.startswith('!--'):
		#print "Found comment at %d" % i
		comment = True
		if buf:
			stack.append((CONTENT, buf))
			buf = ''
		i = j+1
		continue
	if tagname == '':
		#print "%r contains no tag at index %d:%d" % (line, i+1, j)
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
		if last == TAG:
			res += '| <%s ' % val
			last = TAG
		else:
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
	if t == COMMENT:
		res += "<!--| %s>" % val
	if t == ENDTAG:
		res += '>'
		last = ENDTAG
		

print res
