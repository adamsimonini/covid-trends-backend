- Get the latest file updates from cloud branch
```
git pull
```

- Create a new local working branch for yourself
```
git checkout <branch-name>
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

- (If not already done:) Create an upstream version of your branch
```
git push --set-upstream origin <local branch name>
```

- Push your local changes to the upstream branch
```
git push
```

- Revert your local changes to the current upstream version for that branch
```
git restore .
```


