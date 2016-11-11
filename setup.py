from setuptools import setup, find_packages

setup(
    name='django-facebook-applications',
    version=__import__('facebook_applications').__version__,
    description='Django implementation for Facebook Graph API Applications',
    long_description=open('README.md').read(),
    author='ramusus',
    author_email='ramusus@gmail.com',
    url='https://github.com/ramusus/django-facebook-applications',
    download_url='http://pypi.python.org/pypi/django-facebook-applications',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    install_requires=[
        'django-facebook-api>=0.1.4',
    ],
    dependency_links=['https://github.com/vittadev/django-facebook-api#egg=django-facebook-api'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
