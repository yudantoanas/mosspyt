# Github Classroom Moss Checker

Big thanks to Park Ye-Joo who writes an [article](https://park.is/blog_posts/20230420_running_moss_plagiarism_checker/) about `Run MOSS Plagiarism Checker on Jupyter Notebooks`. I decided to use the script to automate moss-checker on multiple repos.

## Requirements

- Using Google Chrome
- Launch Chrome with Remote Debugging Port Enabled

    ```bash
    Windows:
    /path/to/chrome --remote-debugging-port=port_number --user-data-dir=/path/to/any/directory/where/you/want/to/set/your/chrome/profile https://yoursite.com

    Mac:
    /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=port_number --user-data-dir=/path/to/any/directory/where/you/want/to/set/your/chrome/profile https://yoursite.com
    ```

    Example:

    ```bash
    # launch chrome and open classroom homepage
    /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=8989 --user-data-dir=~/chrome-rdp <https://classroom.github.com/classrooms>
    ```

- When first launch Chrome RDP, usually chrome will ask to sync with your existing google account or not, opt for `continue without an account`

## Setup

- Clone the repo, and add new `outputs` and `sources` directories

- Register MOSS account ([reference](https://theory.stanford.edu/~aiken/moss/))

    To obtain a Moss account, send a mail message (without subject) to <moss@moss.stanford.edu>. The body of the message should appear like the format below:

    ```text
    registeruser
    mail username@domain
    ```

    **note**: change `username@domain` to your email.
- After receive reply from MOSS, proceed to copy the script from the email and save it to `moss.pl` file 

    > The email should appear like this
    ![alt text](image1.png)

- Set permission on `moss.pl` using `chmod ug+x <file>`

    ```bash
    chmod ug+x moss.pl
    ```

**notes**: Don't change/modify the folder structure of this repo

## Usage

Execute the `run.sh` file in the terminal:

```bash
./run.sh
```

>Ouput Example:
![alt text](image2.png)

## References

- [Run MOSS Plagiarism Checker on Jupyter Notebooks](https://park.is/blog_posts/20230420_running_moss_plagiarism_checker)
- [Running Selenium Tests on an Already Opened Chrome Browser Using Python and Chrome DevTools Protocol](https://www.linkedin.com/pulse/running-selenium-tests-already-opened-chrome-browser-using-kabir)
