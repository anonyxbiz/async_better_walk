from setuptools import setup, find_packages

try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    requirements = []

setup(
    name="async_better_walk",
    version="1.0.0",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Anonyxbiz",
    author_email="anonyxbiz@gmail.com",
    url="https://github.com/anonyxbiz/async_better_walk.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['async_better_walk'],
    python_requires='>=3.6',
)
