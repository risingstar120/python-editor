from setuptools import setup

version = '0.1'

setup(
    name='python-editor',
    version=version,
    description="Programmatically open an editor, capture the result.",
    #long_description='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='editor library vim emacs',
    author='Peter Ruibal',
    author_email='ruibalp@gmail.com',
    url='https://github.com/fmoo/python-editor',
    license='Apache',
    py_modules=[
        'editor',
    ],
    requires=[
        #'six',
    ],
)
