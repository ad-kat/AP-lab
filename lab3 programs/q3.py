def detect_locals(func_name):
    func_code = func_name.__code__
    return func_code.co_nlocals
#the above function uses built-in functions

def the_func():
  a = 1
  b = 2
  c = 3
  p=16
  q=17
  r=18
  x=24
  y=25
  z=26

  print("The number of local variables in my_function is:", detect_locals(the_func))


the_func()
