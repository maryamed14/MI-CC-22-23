## Github Action


### publish image on github


<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/image%20on%20github.png">



     






       name: Docker Image CI

         on:
         push:
         branches: [ "main" ]
         pull_request:
         branches: [ "main" ]

        jobs:

        build:

    runs-on: ubuntu-latest

    steps:
      -
        name: Checkout
        uses: actions/checkout@v3
      
      -
        name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Build and push
        uses: docker/build-push-action@v3
        with:
          context: .
          push: true
          tags: maryamed14/skindr:latest
          
          
          
          
          
          
          
          
          
          
          
<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/secrets.png">
          
          









<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/actions.png">


       name: Docker Image CI

       on:
       push:
       branches: [ "main" ]
      pull_request:
       branches: [ "main" ]

     jobs:

     build:




    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Build the Docker image
      run:  docker build -t skindr .
    - name: Test
      run: docker run -t -v `pwd`:/skincare/tests.py skindr
      
      
   
   
   
   
   <img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/githubaction.png">
      
      

[githubworkflow](https://github.com/maryamed14/MI-CC-22-23/tree/main/.github/workflows)
      
      
