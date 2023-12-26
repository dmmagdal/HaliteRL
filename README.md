# README

Description: My attempts/research into the Halite challenges (2 & 3 in particular) and apply different machine learning techniques to maximize my score.


### Setup

 - It is recommended that you create a python virtual environment instead of a conda due to version issues with a lot of possibly necessary packages.
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


### Notes:

 - Halite code source is from the [HaliteChallenge GitHub](https://github.com/HaliteChallenge) which contains repos for all of the Halite challenges from TwoSigma.
 - My implementations will be in Python 3 and will primarily use python virtual environments to install the packages (see [Setup](#setup)).
     - Halite Python3 bot path: `Halite/airesources/Python/MyBot.py`
     - Halite-II Python3 bot path: `Halite-II/airesources/Python3/MyBot.py`
     - Halite-III Python3 bot path: `Halite-III/starter_kits/Python3/MyBot.py`
 - Variations of different bots will be contained within the respective `Halite` games folder in `MyBots/`. There will be an accompanying `NOTES.md` file for each to detail the notes on the different bot implementations.
 - The raw size of the repo once all submodules are initialized (with no bots implemented & the local replay viewers uninitialized) is 565 MB.


### References:

 - [Halite 1 repo](https://github.com/HaliteChallenge/Halite)
 - [Halite 2 repo](https://github.com/HaliteChallenge/Halite-II)
 - [Halite 3 repo](https://github.com/HaliteChallenge/Halite-III)
 - [Chlorine repo](https://github.com/rooklift/chlorine) (Halite 2 local replay viewer from rooklift - electron)
 - [Fluorine repo](https://github.com/rooklift/fluorine) (Halite 3 local replay viewer from rooklift - electron)