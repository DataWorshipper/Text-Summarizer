import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__="0.0.0"
REPO_NAME="Text-Summarizer"
AUTHOR_USER_NAME="DataWorshipper"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="mandalabhiraj04@gmail.com"

setuptools.setup(
    name=SRC_REPO, 
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A ml project for text-summarization",
    
  
)
