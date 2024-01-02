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
     - Still having dependency issues from installing `kaggle environments` even in the conda environment. The package will successfully install but when importing `kaggle-environments`, the following error would arise: `Loading environment lux_ai_s2 failed: No module named 'vec_noise'` (vec_noise [pypi](https://pypi.org/project/vec-noise/)). Attempting to install `vec_noise` in either conda or `venv` results in erros. Looks like until this issue is resolved, I cannot actually experiment with creating RL agents in halite, even with kaggle.
     - UPDATE 12/31/23: I was able to confirm that the issues with the `kaggle-environments` package seem to be localized to my M2 macbook. I was able to set up and run halite with the `kaggle-environments` on my other machines (Ubuntu server & Windows laptop). I'm not sure if the problem is with Apple Silicon or with ARM chips in general. Will continue to investigate (try installing on my Raspberry Pi).
     - When running the `kaggle-environment` package on a functional system/environment, the main way example notebooks display the previous game is via `env.render()`. However, this is not possible on local machines running the py files on their own. To counter this, I exported the game with `env.toJSON()` to output to a JSON file in the replays folder. I have yet to verify that the exported JSON is compatible with the local replay projects (`fluorine` in this case).
     - UPDATE 01/01/24: I tried installing the `kaggle-environments` package in a Python docker container but saw that the `vec-noise` module was still having issues as part of the installation. Still need to verify on my raspberry pi.


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
 - Halite on Kaggle:
     - [Overview](https://www.kaggle.com/c/halite/overview)
     - [SDK Overview notebook](https://www.kaggle.com/code/sam/halite-sdk-overview/notebook)
     - [Getting Started notebook](https://www.kaggle.com/code/alexisbcook/getting-started-with-halite/notebook)
 - Kaggle Environment:
     - [Pypi](https://pypi.org/project/kaggle-environments/)
     - [Getting Started](https://www.kaggle.com/code/tarunbisht11/get-started-with-kaggle-environment)
 - Conda:
     - [Managing Environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
 - Sentdex's Tutorials:
     - PythonProgramming.net
         - Halite II:
             - [Introduction - Halite II 2017 Artificial Intelligence Competition p.1](https://pythonprogramming.net/introduction-halite-ii-artificial-intelligence-competition/)
             - [Modifying Starter Bot - Halite II 2017 Artificial Intelligence Competition p.2](https://pythonprogramming.net/modify-starter-bot-halite-ii-artificial-intelligence-competition/)
             - [Custom Bot - Halite II 2017 Artificial Intelligence Competition p.3](https://pythonprogramming.net/custom-ai-halite-ii-artificial-intelligence-competition/)
             - [Deep Learning - Halite II 2017 Artificial Intelligence Competition p.4](https://pythonprogramming.net/deep-learning-halite-ii-artificial-intelligence-competition/)
             - [Training Data Deep Learning - Halite II 2017 Artificial Intelligence Competition p.5](https://pythonprogramming.net/training-data-deep-learning-halite-ii-artificial-intelligence-competition/)
             - [Training Model Deep Learning - Halite II 2017 Artificial Intelligence Competition p.6](https://pythonprogramming.net/training-model-deep-learning-halite-ii-artificial-intelligence-competition/)
             - [Deploying Model Deep Learning - Halite II 2017 Artificial Intelligence Competition p.7](https://pythonprogramming.net/deploying-model-deep-learning-halite-ii-artificial-intelligence-competition/)
         - Halite III:
             - [Introduction - Halite III (2018) AI Coding Competition p.1](https://pythonprogramming.net/introduction-halite-iii-ai-coding-competition/)
             - [Running Locally and getting surrounding halite - Halite III (2018) AI Coding Competition p.2](https://pythonprogramming.net/run-local-collect-halite-iii-ai-coding-competition/)
             - [Moving towards most halite - Halite III (2018) AI Coding Competition p.3](https://pythonprogramming.net/moving-to-halite-iii-ai-coding-competition/)
             - [Trying to not run into ourselves - Halite III (2018) AI Coding Competition p.4](https://pythonprogramming.net/not-running-into-halite-iii-ai-coding-competition/)
             - [Moving to drop off halite - Halite III (2018) AI Coding Competition p.5](https://pythonprogramming.net/dropping-off-halite-iii-ai-coding-competition/)
             - [Cleaning up a few things - Halite III (2018) AI Coding Competition p.6](https://pythonprogramming.net/cleaning-up-halite-iii-ai-coding-competition/)
     - YouTube
         - Halite II:
             - [Introduction - Halite II 2017 Artificial Intelligence Competition p.1](https://www.youtube.com/watch?v=QjAu5lJo4zs&list=PLQVvvaa0QuDeIXLGcc7ZxHSCq8br_d1P-&index=1&ab_channel=sentdex)
             - [Modifying Starter Bot - Halite II 2017 Artificial Intelligence Competition p.2](https://www.youtube.com/watch?v=0SVkERzPCSQ&list=PLQVvvaa0QuDeIXLGcc7ZxHSCq8br_d1P-&index=2&ab_channel=sentdex)
             - [Custom Bot - Halite II 2017 Artificial Intelligence Competition p.3](https://www.youtube.com/watch?v=vC3lQ3ZJE2Y&list=PLQVvvaa0QuDeIXLGcc7ZxHSCq8br_d1P-&index=3&ab_channel=sentdex)
             - [Deep Learning - Halite II 2017 Artificial Intelligence Competition p.4](https://www.youtube.com/watch?v=KPBRWF7ALPQ&list=PLQVvvaa0QuDeIXLGcc7ZxHSCq8br_d1P-&index=4&ab_channel=sentdex)
             - [Training Data Deep Learning - Halite II 2017 Artificial Intelligence Competition p.5](https://www.youtube.com/watch?v=OByH7g6T5-A&list=PLQVvvaa0QuDeIXLGcc7ZxHSCq8br_d1P-&index=5&ab_channel=sentdex)
             - [Training Model Deep Learning - Halite II 2017 Artificial Intelligence Competition p.6](https://www.youtube.com/watch?v=kA3gC-IMZZY&list=PLQVvvaa0QuDeIXLGcc7ZxHSCq8br_d1P-&index=6&ab_channel=sentdex)
             - [Deploying Model Deep Learning - Halite II 2017 Artificial Intelligence Competition p.7](https://www.youtube.com/watch?v=7UqRgcd0GwM&list=PLQVvvaa0QuDeIXLGcc7ZxHSCq8br_d1P-&index=7&ab_channel=sentdex)
         - Halite III:
             - [Introduction - Halite III (2018) AI Coding Competition p.1](https://www.youtube.com/watch?v=IXhZLRagXNU&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=1&ab_channel=sentdex)
             - [Running Locally and getting surrounding halite - Halite III (2018) AI Coding Competition p.2](https://www.youtube.com/watch?v=cu7t-GqtTRw&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=2&ab_channel=sentdex)
             - [Moving towards most halite - Halite III (2018) AI Coding Competition p.3](https://www.youtube.com/watch?v=xm25LaJANXc&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=3&ab_channel=sentdex)
             - [Trying to not run into ourselves - Halite III (2018) AI Coding Competition p.4](https://www.youtube.com/watch?v=hgWaow7L9m8&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=4&ab_channel=sentdex)
             - [Moving to drop off halite - Halite III (2018) AI Coding Competition p.5](https://www.youtube.com/watch?v=_h3HVbH93i4&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=5&ab_channel=sentdex)
             - [Further improvements to rule-based bot - Halite III coding competition p.6](https://www.youtube.com/watch?v=aMjSJGtXdeg&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=6&ab_channel=sentdex)
             - [Overview - Deep Learning in Halite AI competition p.1](https://www.youtube.com/watch?v=1niezMc2kpM&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=7&ab_channel=sentdex)
             - [Structuring and visualizing Data - Deep Learning in Halite AI competition p.2](https://www.youtube.com/watch?v=gCNIGvYbX1c&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=8&ab_channel=sentdex)
             - [Building dataset - Deep Learning in Halite AI competition p.3](https://www.youtube.com/watch?v=TjN3XeA2wGc&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=9&ab_channel=sentdex)
             - [Checking out Data - Deep Learning in Halite AI competition p.4](https://www.youtube.com/watch?v=Zub26O7C5J0&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=10&ab_channel=sentdex)
             - [Training Model - Deep Learning in Halite AI competition p.5](https://www.youtube.com/watch?v=m0UdvFdUyZM&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=11&ab_channel=sentdex)
             - [Running with Trained Model - Deep Learning in Halite AI competition p.6](https://www.youtube.com/watch?v=dGjPfDibhHw&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=12&ab_channel=sentdex)
             - [Analyzing model improvements - Deep Learning in Halite AI competition p.7](https://www.youtube.com/watch?v=hjQLx7QW5kg&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=13&ab_channel=sentdex)
             - [Conclusion - Deep Learning in Halite AI competition p.8](https://www.youtube.com/watch?v=Ln6A4g9NNnM&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=14&ab_channel=sentdex)