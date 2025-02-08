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

TODO: Explain what each test does and why

```
Examples here
```

## Project Instructions

TODO: This section should contain all the student deliverables for this project.

## Built With

* [Item1](www.item1.com) - Description of item
* [Item2](www.item2.com) - Description of item
* [Item3](www.item3.com) - Description of item

Include all items used to build project.

## License

[License](LICENSE.txt)
