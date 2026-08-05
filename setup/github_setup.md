# GitHub Setup

## Terminal cheat sheet

The terminal is a text based interface used to control a computer.  It is commonly used in software development for it's power and flexibility.

> NOTE when an example has square brackets it indicates input and they are not included in the entered command.

- `git clone [URL To Repo]` - Download a git repository into the current directory
- `git status`              - Status of the current git repository (must be run from within repo directory)
- `git add .`               - Add all new files to git repository
- `git commit -a -m"[commit message]"`           - Commit all uncommitted changes as a 'ChangeSet'.
- `git push`                - Push all local change sets to git repo
  - you will need github account and write access to repo
- `git pull`                - Pull all changes to repo from server into your local copy of the repo

## Create a GitHub account

If you haven't already create a free account at [GitHub](https://github.com)

## Setting Up Git to use GitHub

### Configure user name and email

Enter the following commands in the terminal using your name and email.

```bash
git config --global user.name "My Name"

git config --global user.email "myemail@example.com"
```

> NOTE you should not use your real email address.  got to the [github settings](https://github.com/settings/emails) and use your private email

Once you have set your username and email check that they are set correctly using the list command.

```bash
git config --list
```

### Login to github from terminal

Install github command line by entering the following in the terminal

```bash
sudo apt install gh
```

Entery `y` when asked

Use the `gh` command to login enter the following in the terminal

```bash
gh auth login
```

Choose these answers when asked

- What account do you want to log into? 
  - Answer: GitHub.com
- What is your preferred protocol for Git operations on this host?
  - Answer: HTTPS
- Authenticate Git with your GitHub credentials?
  - Answer: Yes
- How would you like to authenticate GitHub CLI?
  - Answer: Login with a web browser

Follow the instructions in the terminal and login via the web page opened.