# wsFEEder

A simple Japanese word salads processor.
Let's feed word salads to your CCD-0500 (or other TTS softwares)!

## Install
1. Install poetry in your local.
2. Clone this repository.

## Setup

Execute the following command.

```shell
poetry run python -m unidic download
```

## Usage

### Parse

`parse` command parses a text file and makes "pool dump file" and "sentences dump file".
These two files are used in `process` command.
"pool dump file" is a data pool of used words, and "sentences dump file" is a data of sentence structures.

View help via

```shell
poetry run parse -h
```

### Process

`process` command uses "pool dump file" and "sentences dump file" and processes/prints word salads.
These two files can be made by `parse` command.

View help via

```shell
poetry run process -h
```
