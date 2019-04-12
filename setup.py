from setuptools import setup, find_packages

about = {}
with open("yews/__about__.py") as fp:
    exec(fp.read(), about)

requirements = [
    'numpy',
    'torch>=1.0.0',
]

if __name__ == '__main__':

    setup(
        python_requires='>=3.6',  # Your supported Python ranges

        # metadata
        name=about['__title__'],
        version=about['__version__'],
        author=about['__author__'],
        author_email=about['__email__'],
        description="Deep learning toolbox for seismic waveform processing.",
        license=about['__license__'],

        # package info
        packages=find_packages(exclude=('tests', 'examples')),

        zip_safe=True,
        install_requires=requirements,
        extras_require={
            "scipy": ["scipy"],
            "obspy": ["obspy"],
        },
    )