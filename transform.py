import sys
import markdown

reload(sys)
sys.setdefaultencoding('UTF8')

if len(sys.argv) < 2:
  print 'need markdown file param'
  exit(1)

filename = sys.argv[1]
outfile = 'docs/' + sys.argv[1].split('.')[0] + '.html'

with open(filename) as fd:
  content = fd.read()

with open('template.html.in') as fd:
  template = fd.read()

# Real quotes. Real dashes. Because come on. It's about standards.
content = content.replace('``', '&ldquo;')
content = content.replace("''", '&rdquo;')
content = content.replace('---', '&mdash;')
content = content.replace('--', '&ndash;')

# This is gross. Oh well.
# ("It's about standards" went out the door quick, eh?)
content = content.split('\n')
title = content[0].strip('#')
content = markdown.markdown('\n'.join(content[1:]), tab_length=2)

result = template.replace('%$%TITLE%$%', title)
result = result.replace('%$%BODY%$%', content)

with open(outfile, 'w') as fd:
  fd.write(result)
