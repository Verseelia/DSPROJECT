from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str):
    """
    This function reads a requirements file and returns a list of dependencies.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

# Correct placement of setup()
setup(
    name="mlproject",
    version="0.0.1",
    author="Verseelia",
    author_email="verseeliafrancis1503@gmail.com",
    install_requires=get_requirements('requirements.txt')
)
