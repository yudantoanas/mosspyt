# Jupyter Notebook Moss Checker

Big thanks to Park Ye-Joo who writes an [article](https://park.is/blog_posts/20230420_running_moss_plagiarism_checker/) about `Run MOSS Plagiarism Checker on Jupyter Notebooks`. I decided to use the script to automate moss-checker on multiple repos.

## Setup

- register MOSS ([reference](https://theory.stanford.edu/~aiken/moss/))
    > To obtain a Moss account, send a mail message (without subject) to <moss@moss.stanford.edu>. The body of the message should appear exactly as follows:

    ```text
    registeruser
    mail username@domain
    ```

    **note**: the last bit in italics is your email address.
- after receive reply from MOSS, proceed to copy the script from the email and save it to `moss.pl` file
- copy and/or rename some files (remove `-example` suffix), example:

    ```text
    organization-example.txt -> organization.txt
    ```

- **important!** you must add SSH key to your github account

## File purposes

- `usernames.txt`: define target username(s)
- `organization.txt`: define repo organization/profile name
- `repoPrefix.txt`: define your repo name prefix
- `filePrefix.txt`: define your file name prefix
- `notebookExtractor.py`: will extract python codes from jupyter notebook (.ipynb)
- `scriptExtractor.py`: will extract python codes from python (.py) file

**notes**:

- extracted result(s) will be stored in `outputs/` directory

## Usage

0. Set permissions on these files using `chmod ug+x <file>`

    ```bash
    chmod ug+x clone.sh
    chmod ug+x moss.pl
    ```

1. Run `clone.sh` to clone the repo(s)

    ```bash
    ./clone.sh
    ```

2. Run `notebookExtractor.py` or `scriptExtractor.py`

    ```bash
    # example
    python notebookExtractor.py
    ```

3. Run `moss.pl` file to execute moss checker

    ```bash
    # run this command
    ./moss.pl -l python -c "Sample Assignment MOSS Results" ./outputs/*.py
    ```
