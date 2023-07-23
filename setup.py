import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "CluckNet-Avian-Ailment-Classifier"
AUTHOR_USER_NAME = "Odulah"
SRC_REPO = "Avian_Ailment_classifier"
AUTHOR_EMAIL = "aadim0311@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "Avian_Ailment_classifier"},
    packages=setuptools.find_packages(where="Avian_Ailment_classifier")
)