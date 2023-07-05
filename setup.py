import setuptools

# with open("requirements.txt", "r") as fh:
#     requirements = [line.strip() for line in fh]

setuptools.setup(
    name="send-sms",
    version="0.0.1",
    author="Hamed Matari",
    author_email="hamedmatari1@yahoo.com",
    description="send sms easily with smpp",
    long_description="send sms easily with smpp",
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
)
