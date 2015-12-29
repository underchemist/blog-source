Nanonispy: My fist python package
=================================

:date: 2015-12-28 14:33
:slug: nanonispy-my-first-python-package
:tags: python
:status: published

:summary: :code:`nanonispy` is a small library written in python 3. It came about by needing to do some quasiparticle interference (QPI) analysis on STM grids. Nanonis saves the data in binary files, which need to be unpacked into :code:`numpy` arrays for further processing. I had written a version of this that was a bit more hardcoded with the analysis code so I decided to try and refactor this into a more general library, and get some experience making a nice clean python library. I don't know if I've achieved that but that's why you practice. The code is unit tested, with ~ 100% coverage although I don't know that the tests are all that good. However it does mean that should you need to change things for your needs, it should be relatively easy to troubleshoot if errors do come up.

|Build Status|  |Coverage Status|  |Install with conda|

First of all this will be only of use to those that use an STM with a Nanonis hardware/software. Also since this is a python package, you should probably be using python for data analysis.

:code:`nanonispy` is a small library written in python 3. It came about by needing to do some quasiparticle interference (QPI) analysis on STM grids. Nanonis saves the data in binary files, which need to be unpacked into :code:`numpy` arrays for further processing. I had written a version of this that was a bit more hardcoded with the analysis code so I decided to try and refactor this into a more general library, and get some experience making a nice clean python library. I don't know if I've achieved that but that's why you practice. The code is unit tested, with ~ 100% coverage although I don't know that the tests are all that good. However it does mean that should you need to change things for your needs, it should be relatively easy to troubleshoot if errors do come up.

------------------------------------------------------------------------------------------------------------------------------------------

Things it can do
----------------

- Read Nanonis generated grid, scan, or point spectroscopy files ('.3ds', '.sxm', and '.dat' files, respectively).
- Parse the header for each file and store each entry into a dict for easy retrieval during post-processing.
- Read the binary data in, appropriately shaped, for each channel into :code:`numpy` arrays.
- Since each channel is just a numpy array, you're able to save each in a '.npy' binary format for easy figure generation after some post-processing.

Things it cannot do
-------------------

- Handle incomplete or non-square datasets.
- Apply image correction techniques like flattening.
- Handle memory management. If you need to process a lot of grid data (200-300+ MB a pop), keep in mind that you may fill up your RAM quite quickly.

Things it should be able to do (in time)
----------------------------------------

- Have basic image flattening utility fuctions.
- Have unified header dictionaries between grid and scan files. The formats Nanonis saves grid and scan information in is quite different and up until now I have been to lazy to try to normalize it a bit.
- More gracefully handle incomplete/non-square data.
- Have docs? just to describe things in a minimal way.

Installation
------------

In the continued theme of I don't know what I'm doing, I uploaded :code:`nanonispy` to pypi_, conda_, and of course github_. So there several, I think all fairly easy ways of installing the program. The easiest, or at least in the sense of not presuming much of anything of your development environment, is with setup.py:

.. code-block:: bash

    $ git clone git@github.com:underchemist/nanonispy.git
    $ python setup.py install

However most people will have one of pip or conda installed (if not both). This makes it even simpler and all that is required to download the source code and install it is:

.. code-block:: bash

    $ pip install nanonispy

or

.. code-block:: bash

    $ conda install -c https://conda.anaconda.org/underchemist nanonispy

and you're good to go!

Usage
-----

I tend to explore my data a bit in an ipython/jupyter console, which is sort of how I developed the code. However it's just as easy to start scripting away since the library is pretty small and only requires you to do one thing: Initialize!

A typical script using for :code:`nanonispy` might start out like:

.. code-block:: python

    import nanonispy as nap  # what I found convenient, up to you

    fname = '/path/to/my/big/important/stm/data.3ds'
    grid = nap.read.Grid(fname)

    fname2 = '/path/to/my/less/important/stm/scan.sxm'
    scan = nap.read.Scan(fname2)

    fname3 = '/path/to/spectroscopy/data.dat'
    spec = nap.read.Spec(fname3)

Now you have 3 class objects initialized with all their data and header information avaible as class attributes! Analyze away.

------------------------------------------------------------------------------------------------------------------------------

Friedel oscillations on Ag(111)... yummy!

.. image:: /images/friedel-ag111.png
    :width: 100%
    :align: center
    :alt: sailing the Fermi seas

.. _pypi: https://pypi.python.org/pypi/nanonispy/1.0.1
.. _conda: https://anaconda.org/underchemist/nanonispy
.. _github: https://github.com/underchemist/nanonispy

.. |Build Status| image:: https://travis-ci.org/underchemist/nanonispy.svg?branch=master
   :target: https://travis-ci.org/underchemist/nanonispy
.. |Coverage Status| image:: https://coveralls.io/repos/underchemist/nanonispy/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/underchemist/nanonispy?branch=master
.. |Install with conda| image:: https://anaconda.org/underchemist/nanonispy/badges/installer/conda.svg
   :target: https://anaconda.org/underchemist/nanonispy/badges/installer/conda.svg
