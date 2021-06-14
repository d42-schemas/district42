from setuptools import find_packages, setup

setup(
    name='district42',
    description='Data description language for defining data models',
    version='0.6.9',
    url='https://github.com/nikitanovosibirsk/district42',
    author='Nikita Tsvetkov',
    author_email='nikitanovosibirsk@yandex.com',
    python_requires='>=3.6',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Delorean==0.5.0'
    ]
)
