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

## Procedure
The procedure is pretty simple.
- There is a repositories.csv file. You have to list your repositories now and maintain list onwards to take backup of those repositories.
- Make sure it is accessible from the server where this procedure is setup and runs well after setup.
- Hook script with OS-Cron service and that's it. The script will start working to make it up-to date on-going. When first time script run it will clone the new repo and fetch it onwards if it's already available on desired location.

## Setup
Follow mentioned steps to setup on your Ubuntu (Linux) server.

### Clone this repo.
git clone https://github.com/amshukla17/repository-backup-procedure.git

### List repositories to Backup as bare
Define your repository inside the repositories.csv file. This file is used to fetch the repositories.

![CSV File](images/csv-file.png?raw=true "CSV File")

### Setup in the cron-tab
To run this script on specific interval to take backups regularly you can setup in cron of your OS. Most generic linux environment have following procedure.

```
* * * * *  command to execute
│ │ │ │ │
│ │ │ │ └─── day of week (0 - 6) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)
│ │ │ └──────── month (1 - 12)
│ │ └───────────── day of month (1 - 31)
│ └────────────────── hour (0 - 23)
└─────────────────────── min (0 - 59)
```

i.e. This procedure is setup in my home folder (/home/amshukla17/rbp). So ideal way to run this script is as following.

```
[python3] [gitbackup.py] [CSV FILE] [BACKUP DESTINATION] >> [LOG FILE (optional)]
```

```
/usr/bin/python3 /home/amshukla17/rbp/src/gitbackup.py "/home/amshukla17/rbp/repositories.csv" "/home/amshukla17/rbp/bare-repositories/" >> /var/log/rbp-repo-backup.log
```

So that crontab entry will look like.

Every Hour
```
1 * * * * /usr/bin/python3 /home/amshukla17/rbp/src/gitbackup.py "/home/amshukla17/rbp/repositories.csv" "/home/amshukla17/rbp/bare-repositories/" >> /var/log/rbp-repo-backup.log
```
Every Day
```
1 0 * * * /usr/bin/python3 /home/amshukla17/rbp/src/gitbackup.py "/home/amshukla17/rbp/repositories.csv" "/home/amshukla17/rbp/bare-repositories/" >> /var/log/rbp-repo-backup.log
```

Check log in the file /var/log/rbp-repo-backup.log. It will look like following.

![Backup Successful](images/successful-backup.png?raw=true "Backup Successful")


##
> **Note:**
> 
> This procedure work is not liable for any damage in any manner. So use it properly and check things according so you do not face any surprise in the future. Please encourage me by giving 🌟 on the repository here.
##
