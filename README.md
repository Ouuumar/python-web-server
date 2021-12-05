# python-web-app

**A docker container (Docker Desktop) for a simple python Web app few unit tested**

## Simple tests

**Unittest** used to :

    - test that calls the website's url and confirms a code reply of 200 (working site)
  
    -  test that sends a GET request to the website and confirms that the website returns the correct answer (correct output)
  
    - the average response time of the site should be below 100 ms per request, when 1000 requests are sent per second (stress handled)

## Step 1

Turn on your Docker then, 
cd to the project location

      - docker-compose up

# Step 2

You can enter different urls and pass a list of numbers to calculate its mean :

- http://localhost:8080/average?list=1,2,3 (get 2.0)
- http://localhost:8080/average?list="enter any list of numbers"

Or you can just test the home url :

- http://localhost:8080 (get "success" : True)

## Step 2

Do not forget to :

    - docker-compose down

When you are done.
