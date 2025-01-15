from setuptools import setup, find_packages

setup(
    name='pipin',  
    version='0.1.0',  
    description='make dependency a depencency',  
    author='jesse',  # Replace with your name
    author_email='cyberslueth@consutant.com',  
    url='https://github.com/unaveragetech/Pipin/main',  # Replace with your project URL
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        'tqdm',      # Progress bar library
        'pipin',     # Custom or unknown package (ensure it's installable)
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Replace with your chosen license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.12.6',
    ],
    python_requires='>=3.12.6',  # Specify the Python version requirements
)
