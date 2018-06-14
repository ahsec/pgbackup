from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8', mode='r') as fopen:
    readme = fopen.read()

setup(
        name='pgbackup',
        version='0.1.0',
        description='Database backups locally or to AWS S3',
        long_description=readme,
        author='Angel',
        author_email='angel@gmail.com',
        packages=find_packages('src'),
        package_dir={'':'src'},
        install_requires=['boto3'],
        entry_points={
            'console_scripts': [
                'pgbackup=pgbackup.cli:main',
            ],
        }
    )

