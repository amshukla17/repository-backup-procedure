# RBP (repository-backup-procedure)
This repository contains organized procedure to take git bare repository as a backup on fix time interval bases on Ubuntu(Linux) environment. If you are setting up on other environment minor adjustment required. Drop me an email on "amshukla17 at gmail.com" to request enhancements you like to see with this procedure.

<details><summary>more...</summary><p/>
<p>The procedure is useful when you have multiple git repositories and you want to store it safe as a backup.</p>

<p>This procedure uses only ssh: protocol as of now. You have to set-up private/public key authentication and that's it, no need to share and credentials with any code procedure.</p>

<h3> Why? </h3>
There is no loss with backing up git repositories. No one cannot be so sure that the platform they use gonna stay the same forever. Maybe the platform they use stop serving or banned or became unresponsive or they cannot afford anything like that. No one can predict, right? So it is necessary to start backup your git repositories on-wards before something strenge happen.

<h3> Why bare? </h3>
<p>You can backup normal git repository, but to make it very simple what we require in the the backup. We need history and our latest version code base, right? So you can backup only the git bare repository. Simply git bare is a .git directory without a working tree in it. We are storing for backup purpose so you cannot work insida a bare repository directly, but it can be used when we want to restore it and start working normally.</p>

<p>If we clone the git bare instead of the full git repository, we can get all commit history and all the branches on our git repositories without actually downloading all files so that the git bare repository size is much smaller.</p>

<p>So simply with bare repository, you are storing all your commits and history and when you decide to upload this git repository, you can on any git supported platform even on your server too. You just need to follow some push instructions and your new git repository is ready to use.</p>

</details>

---

TODO
## Procedure
The procedure is pretty simple.
- There is one .csv file you list your repositories now and maintain list onwards.
- Make sure it is accessible from the server where this procedure is setup.
- Hook script with OS-Cron service and that's it, the script will start working to make it up-to date.

## Setup
Follow mentioned steps to setup on your Ubuntu (Linux) server.

### Clone this repo.
git clone 

### List repositories to Backup as bare
Define your repository inside the repositories.csv file. This file is used to fetch the repositories.

##
> **Note:**
> 
> This procedure work is not liable for any damage in any manner. So use it properly and check things according so you do not face any surprise in the future. Please encourage me by giving 🌟 on the repository here.
##
