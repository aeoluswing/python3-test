#!/usr/bin/env python3
'''this py file test dynamic code invoke'''

import math

# dynamic code block
code = '''
def area_of_circle(r):
  return math.pi*r**2
'''

context={}
# define math in code block,otherwise an error 'math not define' will occur
context['math']=math

# third arg 'locals() can make exec have permission to read local mem stack objects'
#exec(code,context,locals())
exec(code,context)

dynamic_result=context['area_of_circle']
print("dynamic_result:",dynamic_result(2))