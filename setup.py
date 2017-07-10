"""
USAGE: 
   o install in develop mode: navigate to the folder containing this file,
                              and type 'python setup.py develop --user'.
                              (ommit '--user' if you want to install for 
                               all users)                           
"""


from setuptools import setup

setup(name='gromacsplotter',
      version='0.1',
      description='Read xvg files created with gromacs for plotting with matplotlib',
      url='',
      author='Ilyas Kuhlemann',
      author_email='ilyasp.ku@gmail.com',
      license='MIT',
      packages=["gromacsplotter"],
      scripts=[],
      install_requires=['numpy',
                        "matplotlib"],
      entry_points = {
          'console_scripts': ["gromacsplotter = gromacsplotter.plot_xvg_data:main"]
      },
      zip_safe=False)
