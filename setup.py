from setuptools import setup, find_packages
 
setup(name='libpythontest',
      version='0.1',
      url='https://github.com/Beltrao79/libpythontest.git',
      author='Beltrao79',
      author_email='beltrao.matheus.s@gmail.com',
      description='Teste de publicação de lib',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)