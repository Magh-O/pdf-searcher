setup(
    name="pdf-reader",
    version="1.0.0",
    description="Search a word in all the pdfs of a folder",
    long_description=README,
    url="https://github.com/Magh-O/pdf-searcher",
    author="Adran Moure - MaghO",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["pdfsearcher"],
    include_package_data=True,
    install_requires=[
        "pdfminer.six"
    ],
    entry_points={"console_scripts":["searcher=pdfsearcher.__main__:main"]}
)