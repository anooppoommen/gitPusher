# gitPusher
an automatic git push/commit script in python

# How to use
Copy the file into your git directory 

Add the following rule to .gitignore("optional")
```
script.py
```
## Then try any of the following

* commit and push
```shell
python script.py
```
* commit only
```shell
python script.py n
```
* commit only with message
```shell
python script.py "commit message" n
```

* commit and push with message
```shell
python script.py "commit message"
```

## To use with npm package
add the following rule to the scripts in package.json
```JSON
 {
  "scripts" : {
    "commit-and-push" : "python script.py",
    }
 }
```
and then run 
```
npm run commit-and-push
```

All done enjoy!!

<p align="center">
  :smile:
</p>
