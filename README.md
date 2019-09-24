Python 3 : Learnt by Madhav  [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PseudoCodeNerd/learning-python/master)
=========================
## Resources and Guides Used:

-  __Complete Python Bootcamp: Go from zero to hero in Python 3__ on _Udemy_
-  [__CMU 15-112: Fundamentals of Programming and Computer Science__](https://www.cs.cmu.edu/~112/) by _Carnegie Mellon University_
- [ __Introduction to Computer Science and Programming Using Python__](https://courses.edx.org/certificates/a58a0b7523f84a9dbea0e1830a80116d) provided by _Massachusetts Institute of Technology (MITx)_

- __Learn Python 3 The Hard Way__ by _Zed A. Shaw_
<hr>

### Pythonly Active on:
* CodeWars <br>![](cwlarge.svg)<br>
* [HackerRank](https://www.hackerrank.com/Sharma_dhav)
* [CodeChef](https://www.codechef.com/users/sharma_dhav03)<br>*Still a CP nUb*
## Implementation of some useful Algos/DS/MLConcepts in Python
### ML Stuff
* [newton-raphson method](Algos/newtonraphson.py)
* - [ ] (traditional) Gradient Descent
* - [ ] Random Forest Classifier/Regressiom
* - [ ] cool neural network
### Sorts/Searches
* [bubblesort](Algos/bubblesort.py)
* To add many more...
## Installation

Simply open the [Jupyter](http://jupyter.org/) notebooks you are interested in:

* Using [jupyter.org's notebook viewer](http://nbviewer.jupyter.org/github/ageron/handson-ml/blob/master/index.ipynb)
    * note: [github.com's notebook viewer](https://github.com/ageron/handson-ml/blob/master/index.ipynb) also works but it is slower and the math formulas are not displayed correctly,
* or by cloning this repository and running Jupyter locally. This option lets you play around with the code. In this case, follow the installation instructions below.
First, you will need to install [git](https://git-scm.com/), if you don't have it already.

Next, clone this repository by opening a terminal and typing the following commands:

    $ cd $HOME  # or any other development directory you prefer
    $ git clone https://github.com/ageron/handson-ml.git
    $ cd handson-ml

If you do not want to install git, you can instead download [master.zip](https://github.com/ageron/handson-ml/archive/master.zip), unzip it, rename the resulting directory to `handson-ml` and move it to your development directory.

If you want to go through chapter 16 on Reinforcement Learning, you will need to [install OpenAI gym](https://gym.openai.com/docs) and its dependencies for Atari simulations.

If you are familiar with Python and you know how to install Python libraries, go ahead and install the libraries listed in `requirements.txt` and jump to the [Starting Jupyter](#starting-jupyter) section.

## Using Anaconda
When using Anaconda, you can optionally create an isolated Python environment dedicated to this project. This is recommended as it makes it possible to have a different environment for each project (e.g. one for this project), with potentially different libraries and library versions:

    $ conda create -n mlbook python=3.5 anaconda
    $ conda activate mlbook

This creates a fresh Python 3.5 environment called `mlbook` (you can change the name if you want to), and it activates it. This environment contains all the scientific libraries that come with Anaconda. This includes all the libraries we will need (NumPy, Matplotlib, Pandas, Jupyter and a few others), except for TensorFlow, so let's install it:

    $ conda install -n mlbook -c conda-forge tensorflow

This installs the latest version of TensorFlow available for Anaconda (which is usually *not* the latest TensorFlow version) in the `mlbook` environment (fetching it from the `conda-forge` repository). If you chose not to create an `mlbook` environment, then just remove the `-n mlbook` option.

Next, you can optionally install Jupyter extensions. These are useful to have nice tables of contents in the notebooks, but they are not required.

    $ conda install -n mlbook -c conda-forge jupyter_contrib_nbextensions

You are all set! Next, jump to the [Starting Jupyter](#starting-jupyter) section.


## Starting Jupyter
Okay! You can now start Jupyter, simply type:

    $ jupyter notebook

This should open up your browser, and you should see Jupyter's tree view, with the contents of the current directory. If your browser does not open automatically, visit [127.0.0.1:8888](http://127.0.0.1:8888/tree). Click on `index.ipynb` to get started!

Congrats! You are ready to learn Machine Learning, hands on!

# Contributors
@PseudoCodeNerd
