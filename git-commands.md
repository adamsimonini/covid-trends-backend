- Go to the main branch to get the latest updates
```
git checkout main
```

- Get the latest file updates from cloud branch (usually done from main)
```
git pull
```

- Create a new local working branch for yourself where branch-name = xx-yyyy (xx = your initials, yyyy = ticket number on DevOps)
```
git checkout -b <branch-name>
```

- Add your changes to the commit
```
git add .
```

- Check your desired updated files
```
git status
```

- Create your git commit along with a short description for it
```
git commit -m '<message here>'
```

- Create the remote version of your branch
```
git push --set-upstream origin <branch-name>
```

- Revert your local changes to the current remote version for that branch
```
git restore .
```


