from setuptools import setup

try:
      with open("VERSION", "r") as ver:
            version_program = ver.read()
except:
      pass


setup(name='terminator',
      version=version_program,
      description='Modular penetration testing platform, With tested and published user modules',
      url='https://github.com/G00Dway/Terminator',
      author='G00Dway',
      license='GNU 3.0',
      python_requires='>=3.5.0',
       install_requires=[
          'requests', 'paramiko', 'colorama',
          'pyngrok'
      ]
)