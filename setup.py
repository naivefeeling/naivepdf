from setuptools import setup


setup(
    name='naivepdf',
    version='0.1',
    packages=['naivepdf', 'naivepdf.decoder', 'naivepdf.encoding', 'naivepdf.utils'],
    package_data={'naivepdf': ['cmap/*/*', 'Adobe-Core35_AFMs-314/*']},
    description='yet another pdf texts and tables extractor',
)
