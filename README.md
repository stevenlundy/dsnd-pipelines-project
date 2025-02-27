# Fashion Forward Forecasting

Project description goes here.

## Getting Started

Instructions for how to get a copy of the project running on your local machine.

### Dependencies

This project uses Python 3.11.2. See full list of dependencies in the `requirements.txt` file.

### Installation

#### pyenv

Pyenv is a tool that allows you to manage multiple versions of Python on your machine. This project uses Python 3.11.2. To install pyenv and set the local python version, run the following commands:

```bash
# Install pyenv
brew install pyenv
pyenv install 3.11.2
pyenv virtualenv 3.11.2 dsnd-pipelines-project
# Set the local python version
pyenv local dsnd-pipelines-project
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Install pre-commit

This project uses pre-commit to ensure that code is formatted correctly before committing. To install pre-commit, run the following commands:

```bash
pip install pre-commit
pre-commit install
```

## Testing

Tests are written using the `pytest` framework. To run the tests, use the following command:

```bash
pip install pytest
pytest tests
```

### Break Down Tests

There are tests for the custom transformers. The tests test basic functionality for the text transformers and the custom transformers.

## Project Instructions

The data exploration and training is all done in the Jupyter notebook `starter/starter.ipynb`. The notebook is broken down into the following sections:

1. Data Exploration
1. Building the Pipeline
1. Training the Pipeline
1. Fine Tuning the Pipeline

The Project is deployed on Hugging Face Spaces using a Gradio Interface. The deployment can be found [here](https://huggingface.co/spaces/stevenlundy/dsnd-pipelines-project).

## Built With

* [Gradio](http://gradio.app) - The web framework used
* [Hugging Face Spaces](https://huggingface.co/spaces) - The deployment platform used
* [Seaborn](https://seaborn.pydata.org) - The visualization library used
* [Pandas](https://pandas.pydata.org) - The data manipulation library used
* [Scikit-learn](https://scikit-learn.org/stable/) - The machine learning library used

## License

[License](LICENSE.txt)
