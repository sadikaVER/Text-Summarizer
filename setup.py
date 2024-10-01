import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="Text_Summarizer"
AUTHOR_USER_NAME="sadikaver"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="sadika.verma@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarization using Transformers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/"+AUTHOR_USER_NAME+"/"+REPO_NAME,

    project_urls={
        "Source Code": "https://github.com/"+AUTHOR_USER_NAME+"/"+REPO_NAME,
        "Bug Tracker": "https://github.com/"+AUTHOR_USER_NAME+"/"+REPO_NAME+"/issues",
    },

    package_dirs={"": "src"},
    packages=setuptools.find_packages(where="src")

)