# robo-advisor application

Thanks for checking out this awesome robo-advisor! Read the steps below to learn how to set up your local environment so that you can use it to get stock trading recommendations.

## Prerequisites

+ Anaconda 3.7+
+ Python 3.7+
+ Pip

## Installation

Fork this [remote repository](https://github.com/zky44/robo-advisor) under your own control, then clone your remote copy onto your local computer.

Next, navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd robo-advisor
```

If you haven't done so yet, use anaconda to create and activate a new virtual environment. A suggestion would be to call it "stocks-env":

```sh
conda create -n stocks-env python=3.8
conda activate stocks-env
```

From inside the virtual environment, install package dependicies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws you an error, make sure you are running it from the repository's root directory where the requirements.txt file exists. Refer back to the initial `cd` step above