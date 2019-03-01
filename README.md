# Exabyte Parser (ExaParser)

Exabyte parser is a python package to extract and convert (DFT) data on disk to EDC format.

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

The following diagram presents the package architecture that works as below:

- User invokes the parser with a path to a job working directory.

- The parser initializes a [`Job`](src/job/__init__.py) class to extract and serialize the job in EDC format.
 
- Job class uses [`Workflow`](src/workflow/workflow.py) parser to extract and serialize the workflow.

- The Workflow is initialized with a [Template](#templates) to help the parser to construct the workflow.

    - Users can add new templates or adjust the current ones to support complex workflows.

- Workflow parser iterates over the [Units](src/workflow/units) to extract 

    - application-related data
    - input and output files
    - materials (initial/final structures) and properties

- The job utilizes [Compute](src/job/compute) classes to extract compute configuration from the resource management system.

- Once the job is formed it is passed to [Data Handler](src/data/handlers) classes to handle data, e.g. storing data in Exabyte platform.

![ExaParser](https://user-images.githubusercontent.com/10528238/53663156-dd876e00-3c19-11e9-868f-41946199eca4.png)

## Installation

ExaParser can be installed as below.

1. Install [git-lfs](https://help.github.com/articles/installing-git-large-file-storage/) in order to pull the files stored on Git LFS.

1. Clone repository:
    
    ```bash
    git clone git@github.com:Exabyte-io/exaprser.git
    ```

1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/) using [pip](https://pip.pypa.io/en/stable/) if not already present:

    ```bash
    pip install virtualenv
    ```

1. Create virtual environment and install required packages:

    ```bash
    cd exaprser
    virtualenv venv
    source venv/bin/activate
    export GIT_LFS_SKIP_SMUDGE=1
    pip install -r requirements.txt
    ```

## Usage

1. Open [settings](src/settings.py) and adjust parameters as necessary. The most ones are listed below.

    - Add `ExabyteRESTfulAPI` to `DATA_HANDLERS` parameter to upload the data into your Exabyte.io account.
    
        - New users can register [here](https://platform.exabyte.io/register) to obtain an Exabyte.io account.
    
    - Set `OWNER_SLUG`, `PROJECT_SLUG`, `API_ACCOUNT_ID`, and `API_AUTH_TOKEN` if `ExabyteRESTfulAPI` is enabled.
    
        - See [RESTful API Documentation](https://docs.exabyte.io/rest-api/overview/) to learn how obtain authentication parameters.
    
    - Adjust `WORKFLOW_TEMPLATE_NAME` parameter if different template should be used.
    
        - By default a [Shell Workflow](src/templates/shell.json) is constructed. See [Templates](#templates) section for more details.
    
    - Adjust `PROPERTIES` parameter to extract properties that make sense, otherwise all listed properties will be extracted.

1. Run the below commands to extract the data.

```bash
source venv/bin/activate
./bin/exaperser -w PATH_TO_JOB_WORKING_DIRECTORY
```

## Templates

Workflow templates are used to help the parser extracting the data as users follow different approaches to name their input/output files and organize their job directories. Readers are referred to [Exabyte.io Documentation](https://docs.exabyte.io/workflows/overview/) for more information about the structure of workflows. As explain above a [Shell Workflow Template](src/templates/shell.json) is used by default to construct the workflow. Fr each unit of the workflow one should specify `stdoutFile`, the relative path to the file containing the standard output of the job, `workDir`, the relative path to directory containing data for the unit and the name of `input` files.

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
