#!/usr/bin/env python

from string import Template
import sys

def main(amount):
    template = Template(sys.stdin.read())
    context = {'amount': "%.2f" % amount}
    rendered = template.substitute(context)
    
    print (rendered)
    
    
if __name__ == '__main__':
    main(float(sys.argv[1]))
