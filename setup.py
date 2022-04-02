from setuptools import setup

setup(name='terminator',
      version='1.8.0',
      description='Modular penetration testing platform',
      url='https://github.com/G00Dway/Terminator',
      author='G00Dway',
      license='GNU 3.0',
      python_requires='>=3.8.0',
       install_requires=[
          'packaging', 'pyyaml', 'requests', 'paramiko',
          'adb-shell', 'pyngrok',
      ]
)