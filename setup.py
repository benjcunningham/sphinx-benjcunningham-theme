from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()

extras = {
    "quality": ["black", "flake8", "isort"],
    "testing": ["pytest"],
}

extras["dev"] = extras["quality"] + extras["testing"]

setup(
    name="sphinx-benjcunningham-theme",
    version="0.1.0.dev0",
    author="Ben Cunningham",
    author_email="benjamescunningham@gmail.com",
    description="Custom Sphinx theme based on Read the Docs",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/benjcunningham/sphinx-benjcunningham-theme",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "Sphinx<4.0",
        "sphinx-multiversion==0.2.4",
        "sphinx_rtd_theme<1.0",
    ],
    extras_require=extras,
    python_requires=">=3.7.0",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
    include_package_data=True,
)
