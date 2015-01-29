## Step #1

### Docker management
1. Make sure to tail your logs via docker logs blog
1. If you produce an error, the docker container will stop. Correct the error and then do ```docker start blog```

### Why an author module?
We want to split the application in different components and group all the related functions and models in those folders.

### Rename the home folder to blog and create the author module and database
1. Add author init and views
1. Add author model
1. Add author.views to main ```__init__```
