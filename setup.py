from setuptools import find_packages, setup


def main():
    setup(name='narumi',
          use_scm_version=True,
          setup_requires=['setuptools_scm'],
          author='なるみ',
          author_email='weaper@gamil.com',
          packages=find_packages())


if __name__ == "__main__":
    main()
