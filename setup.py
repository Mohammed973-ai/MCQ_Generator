from setuptools import find_packages, setup

setup(
    name='MCQgenerator',
    version='0.0.1',
    author='Mohammed Waseem',
    author_email='mhamedwaseem2001@gmail.com',
    install_requires=[
        "Groq",
        "langchain",
        "streamlit",
        "python-dotenv",
        "PyPDF2",
        "pandas",
        "langchain-groq",
        "langchain_community",
        "langchain_groq",
        "traceback"
    ],
    packages=find_packages()
)