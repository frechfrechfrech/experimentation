import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='[package_name]',
      version='0.2',
      author='Alex Frech',
      author_email='frechfrechfrech@gmail.com',
      description='[description]',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='[github url]',
      license='MIT',
      packages=setuptools.find_packages(),
      # zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
