import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfin-sentiment",
    version="0.1.1",
    author="Moritz Wilksch",
    author_email="moritzwilksch@gmail.com",
    description="A library for market sentiment analysis of financial social media posts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moritzwilksch/pyfin-sentiment",
    project_urls={
        "Bug Tracker": "https://github.com/moritzwilksch/pyfin-sentiment/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=["joblib", "scikit-learn>=1.1.1", "polars", "scipy>=1.8.0"],
)
