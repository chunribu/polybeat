from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='polybeat',
    version='1.0.0',
    description='A toy for visualizing polyrhythms',
    url='https://github.com/chunribu/polybeat/',
    author='Jian Jiang',
    author_email='pccfreespace@gmail.com',
    packages=find_packages(),
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={'polybeat': ['sounds/*.wav']},
    include_package_data=True,
    install_requires=[],
    entry_points = {},
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='polybeat polyrhythm pccfs',
)