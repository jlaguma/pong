import pong
import sys
from setuptools import setup

if sys.version_info.major < 3 or (sys.version_info.minor < 6
                                  and sys.version_info.major == 3):
    sys.exit('Python < 3.6 is unsupported.')

with open('README.md', encoding='utf8') as file:
    long_description = file.read()

setup(
    name='pong',
    version=pong.__version__,
    packages=['pong'],
    package_data={},
    install_requires=['click'],
    license='GNU GPLv3',
    description='Pong Game',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=pong.__author__,
    author_email='james@taran.biz',
    url='https://www.linkedin.com/in/jlaguma/',
    entry_points={'console_scripts': ['pong = pong.__main__:main']},
)
