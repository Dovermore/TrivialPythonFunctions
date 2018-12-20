from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='Dovermore',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Collections of short functions to be used in regular works",
    author="Dovermore",
    author_email='calvinyeye0627@gmail.com',
    url='https://github.com/Dovermore/Dovermore',
    packages=['TrivialFunctions'],
    entry_points={
        'console_scripts': [
            'TrivialFunctions=TrivialFunctions.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='Dovermore',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
