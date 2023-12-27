# README

Description: My attempts/research into the Halite challenges (2 & 3 in particular) and apply different machine learning techniques to maximize my score.


### Setup

 - It is recommended that you create a python virtual environment instead of a conda due to version issues with a lot of possibly necessary packages.
 - Use python `venv` package:
     - To set up the virtual environment, install the `venv` package:
        - `pip3 install virtualenv`
     - Create the new virtual environment:
        - `python -m venv halite-env`
     - Activate the virtual environment:
        - Linux/MacOS: `source halite-env/bin/activate`
        - Windows: `.\halite-env\Scripts\activate`
     - Deactivate the virtual environment:
        - `deactivate`
     - Install the necessary packages (while the virtual environment is active):
        - `(halite-env) pip3 install -r requirements.txt`
     - Also be sure to install the necessary version of `pytorch` according to your OS (refer to the `pytorch` website but the following command will help):
        - Linux & Windows (CUDA 11.8): `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`
        - MacOS (MPS acceleration on MacOS 12.3+): `pip install torch torchvision torchaudio`
 - Use conda:
     - To set up the virtual environment, install miniconda
     - Create the new virtual environment:
         - `conda -n halite-env python=3.10`
     - Activate the conda environment:
         - `conda activate halite-env`
     - Deactivate the conda environment:
        - `conda deactivate`
     - Install all necessary packages (while the conda environment is active):
         - `conda install --file requirements.txt`
     - Alternatively, you can initialize the entire conda environment from the `environment.yml` file:
         - `conda env create -f environment.yml`
     - Also be sure to install the necessary version of `pytorch` according to your OS (refer to the `pytorch` website but the following command will help):
         - Linux & Windows (CUDA 11.8): `conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia`
         - MacOS (MPS acceleration on MacOS 12.3+): `conda install pytorch::pytorch torchvision torchaudio -c pytorch`


### Notes:

 - Halite code source is from the [HaliteChallenge GitHub](https://github.com/HaliteChallenge) which contains repos for all of the Halite challenges from TwoSigma.
 - My implementations will be in Python 3 and will primarily use python virtual environments to install the packages (see [Setup](#setup)).
     - Halite Python3 bot path: `Halite/airesources/Python/MyBot.py`
     - Halite-II Python3 bot path: `Halite-II/airesources/Python3/MyBot.py`
     - Halite-III Python3 bot path: `Halite-III/starter_kits/Python3/MyBot.py`
 - Variations of different bots will be contained within the respective `Halite` games folder in `MyBots/`. There will be an accompanying `NOTES.md` file for each to detail the notes on the different bot implementations.
 - The raw size of the repo once all submodules are initialized (with no bots implemented & the local replay viewers uninitialized) is 565 MB.
 - To build the local replay viewers (with just `npm`):
     - `cd` into the respective submodule (either `chlorine` or `fluorine`)
     - `npm install` to install the necessary modules
     - `npm install electron --save-dev --save-exact`
     - `./node_modules/.bin/electron .` to run the electron app
 - To reset the state of the submodules (either the Halite games or the local replay viewers):
     - `cd` into the respective submodule
     - `git reset --hard HEAD`
     - `git submodule update --init --recursive`
 - The `ReplayDockerfiles` folder is where I try to make scripts to use docker to build the local replay viewers. It currently does not work.
     - The `fluorine` image created would fail due to permission issues
 - Issues right now:
     - Original urls are gone. Anything that points to halite.io is now redirected to twosigma's website and the pages are gone. Using the Wayback Machine may get you the old state of the page but does not seem to be stable or may not be complete.
     - No executable. The original bundles you could download from the website came with compiled executables of the halite game. The repos currently lack those files and existing documentation in the repo doesnt provide a straight forward way to build/compile those programs.
     - Overall lack of clear documentation. There isn't much to actually explain what the different folders in each repo are for or how they work. This problem links to the other problems above.
 - I sort of found a work around with Kaggle for Halite-III. You can get the Halite-III environment and package from `kaggle-environments` package.
     - According to the `kaggle-environments` [pypi](https://pypi.org/project/kaggle-environments/), the package requires Python>=3.8 but I had issues installing it on 3.11 (so I just used Python 3.10 which I specified in the conda `environment.yml`)


### References:

 - Halite repos:
     - [Halite 1 repo](https://github.com/HaliteChallenge/Halite)
     - [Halite 2 repo](https://github.com/HaliteChallenge/Halite-II)
     - [Halite 3 repo](https://github.com/HaliteChallenge/Halite-III)
 - Local Replay Viewer (fluorine & chlorine):
     - [Chlorine repo](https://github.com/rooklift/chlorine) (Halite 2 local replay viewer from rooklift - electron)
     - [Fluorine repo](https://github.com/rooklift/fluorine) (Halite 3 local replay viewer from rooklift - electron)
     - [Chlorine prebult binaries](https://github.com/rooklift/chlorine/releases) by rooklift
     - [Fluorine dockerfile gist](https://gist.github.com/lpenz/09776db42cf5bdb5d6a2553d53f8899e) by lpenz to install fluorine & electron locally
 - Kaggle Halite
     - [Overview](https://www.kaggle.com/c/halite/overview)
     - [SDK Overview notebook](https://www.kaggle.com/code/sam/halite-sdk-overview/notebook)
     - [Getting Started notebook](https://www.kaggle.com/code/alexisbcook/getting-started-with-halite/notebook)
 - Kaggle Environment
     - [Pypi](https://pypi.org/project/kaggle-environments/)
     - [Getting Started](https://www.kaggle.com/code/tarunbisht11/get-started-with-kaggle-environment)
 - Conda
     - [Managing Environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)