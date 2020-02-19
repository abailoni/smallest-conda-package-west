from setuptools import setup, find_packages

exec(open('scpw/__version__.py').read())
setup(
    name='plantseg',
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    description='Smallest Conda Package in the West.',
    author='Lorenzo Cerrone',
    url='https://github.com/lorenzocerrone/smallest-conda-package-west',
    author_email='lorenzo.cerrone@iwr.uni-heidelberg.de',
)