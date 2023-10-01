import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bag_convert",
    version="0.0.1",
    author="daohu527",
    author_email="daohu527@gmail.com",
    description="Ros bag to Apollo record or reverse conversion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daohu527/bag_convert",
    project_urls={
        "Bug Tracker": "https://github.com/daohu527/bag_convert/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    install_requires=[
        'cyber_record',
        'record_msg<=0.1.1',
        'py3rosmsgs',
        'rospkg',
        'pycryptodomex',
    ],
    entry_points={
        'console_scripts': [
            'bag_convert = bag_convert.main:main',
        ],
    },
    python_requires=">=3.6",
)
