# Django REST framework:
 popular option for building REST APIs is Django REST framework. Django REST framework is a Django plugin that adds REST API functionality on top of an existing Django project.
 Django REST framework is a great option for building REST APIs, especially if you have an existing Django project and you want to add an API.
 as we can see in this [article](https://realpython.com/api-integration-in-python/#django-rest-framework) how we can build an api.
 ## API general design
 For API design using Django Rest Fremwork the following have been taken into account good practices:
 
 - Open up the settings.py file Add the following  to INSTALLED_APPS to tell Django about the application and Django REST framework:


 
  
  
  
 
 'skincare.apps.SkincareConfig',
 
 
 
 
    'rest_framework',
    
    
    
  
 - update models.py with 

##

 
 
 
 
 
 
    class Person(models.Model):
 
    name = models.CharField(max_length=255)
    
    age = models.IntegerField()

    def __str__(self):
        return self.name   



- we will create our serializer creating a file called [serializers.py](https://github.com/maryamed14/MI-CC-22-23/blob/main/skincare/Serializers.py)

- Below is the code for a ModelViewSet subclass called personsViewSet. This class will generate the views needed to manage persons data. Add the following code to views.py inside the skincare application:


 


       from .Serializers import PersonSerializer

       from django.http import JsonResponse

       from django.core import serializers

       from rest_framework import viewsets


      class PersonViewSet(viewsets.ModelViewSet):
      queryset = Person.objects.all()
      serializer_class = PersonSerializer
      
 In this class, serializer_class is set to personSerializer and queryset is set to person.objects.all(). This tells Django REST framework which serializer to use and how to query the database for this specific set of views.

Once the views are created, they need to be mapped to the appropriate URLs or endpoints. To do this, Django REST framework provides a DefaultRouter that will automatically generate URLs for a ModelViewSet.


- Create a [urls.py](https://github.com/maryamed14/MI-CC-22-23/blob/main/skincare/urls.py) file  in the application 

This code creates a DefaultRouter and registers personViewSet under the person URL. This will place all the URLs for personViewSet under/person/.


- Finally, we need to update the project’s base [urls.py](https://github.com/maryamed14/MI-CC-22-23/blob/main/SKINDR/urls.py) file to include all the person URLs in the project.


Now we are ready to try out our Django-backed REST API. by Run the following command in the root  directory to start the Django development server:

    $ python manage.py runserver
    
    

## Endpoints:
### persons info: depending on this [user story](https://github.com/maryamed14/MI-CC-22-23/issues/11) we made this api and get these endpoints.

The DefaultRouter you created in /urls.py provides URLs for requests to all the standard API endpoints:

    
    GET /person/
    GET /person/<person_id>/
    POST /person/
    PUT /person/<person_id>/
    PATCH /person/<person_id>/
    DELETE /person/<person_id>/
    
    
 - we will test this by using APITESTCASE from  [rest_framework.test](https://github.com/maryamed14/MI-CC-22-23/blob/main/skincare/tests.py) and by run task manager Doit that we choose befor we get
 
<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/testapi.png"> 


### - we will test the API Endpoints we have by using the URLs for requests to all the api endpoints by using [Postman API Platform](https://www.postman.com/)


<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/get.png"> 



<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/getid.png"> 





<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/post.png"> 


 
 
 
 <img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/put.png"> 
 
 
 
 
 <img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/Patch.png">
 
 
 
<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/delet.png">
    
    



 




