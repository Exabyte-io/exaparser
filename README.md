# Exabyte DFT Parser (ExaParser)

Exabyte DFT parser is a python package to extract and convert DFT data on disk to EDC format.

## Functionality

As below:

- Extract structural information and material properties from simulation data
- Serialize extracted information according to ESSE/EDC
- Store serialized data on disk or remote databases
- Support for multiple simulation engines, including:
  - [VASP](#links)
  - [Quantum ESPRESSO](#links)
  - others, to be added

The package is written in a modular way easy to extend for additional applications and properties of interest. Contributions can be in the form of additional [functionality](#todo-list) and [bug/issue reports](https://help.github.com/articles/creating-an-issue/).

## Architecture

The following diagram presents the package architecture.

![ExaParser](https://user-images.githubusercontent.com/10528238/53663156-dd876e00-3c19-11e9-868f-41946199eca4.png)

## Installation

ExaParser can be installed as below.

0. Install [git-lfs](https://help.github.com/articles/installing-git-large-file-storage/) in order to pull the files stored on Git LFS.

1. Clone repository:
    
    ```bash
    git clone git@github.com:Exabyte-io/exaprser.git
    ```

2. Install [virtualenv](https://virtualenv.pypa.io/en/stable/) using [pip](https://pip.pypa.io/en/stable/) if not already present:

    ```bash
    pip install virtualenv
    ```

3. Create virtual environment and install required packages:

    ```bash
    cd exaprser
    virtualenv venv
    source venv/bin/activate
    export GIT_LFS_SKIP_SMUDGE=1
    pip install -r requirements.txt
    ```

## Usage

```bash
source venv/bin/activate
./bin/exaperser -w PATH_TO_JOB_WORKING_DIRECTORY
```

## Tests

Run the following command to run the tests.

```bash
sh run-tests.sh
```

## Contribution

This repository is an [open-source](LICENSE.md) work-in-progress and we welcome contributions. We suggest forking this repository and introducing the adjustments there, the changes in the fork can further be considered for merging into this repository as explained in [GitHub Standard Fork and Pull Request Workflow](https://gist.github.com/Chaser324/ce0505fbed06b947d962).

## TODO List

Desirable features for implementation:

- Implement PBS/Torque and SLURM compute parsers
- Implement VASP and Espresso execution unit parsers
- Add other data handlers
- Add complex workflow templates

## Links

1. [Exabyte Source of Schemas and Examples (ESSE), Github Repository](https://github.com/exabyte-io/exabyte-esse)
1. [Vienna Ab-initio Simulation Package (VASP), official website](https://cms.mpi.univie.ac.at/vasp/)
1. [Quantum ESPRESSO, Official Website](https://www.quantum-espresso.org/)
