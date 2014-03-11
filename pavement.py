from paver.easy import *
import os
import glob

@task
def test():
  sh('nosetests code/test/*.py --with-coverage')
  #sh('nosetests code/test/*.py')
  pass

@task
def clean():
  os.path.exists('.coverage') and os.remove('.coverage')
  for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
  pass

@task
@needs(['clean', 'test'])
def default():
  pass