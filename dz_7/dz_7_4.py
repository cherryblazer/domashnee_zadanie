import os


def try_it(directory):
 for fname in os.listdir(directory):
  if fname == 'templates':
   return True
 
 return False


def main(directory):
 for fname in os.listdir(directory):
  f = os.path.join(directory, fname)

  if not os.path.isfile(f) and try_it(f):
   os.system('mv ' + f + '/templates ' + directory)