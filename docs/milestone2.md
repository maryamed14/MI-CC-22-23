## Choosing and using the Task Manager

### The task managers that are going to be discussed for this project are:
-  [Invoke](https://www.pyinvoke.org/)
-  [Doit](https://pydoit.org/)

# invoke
 Invoke is a Python (2.7 and 3.4+) library for managing shell-oriented subprocesses and organizing executable Python code into CLI-invokable tasks. It draws inspiration from various sources (make/rake, Fabric 1.x, etc) to arrive at a powerful & clean feature set.
Like Ruby’s Rake tool and Invoke’s own predecessor Fabric 1.x, it provides a clean, high level API for running shell commands and defining/organizing task functions from a tasks.py file


```python
from invoke import task

@task
def build(c):
    print("Building!")

@task
def build(c, clean=False):
    if clean:
        print("Cleaning!")
    print("Building!")
```


- as Invoke is most common one I used it first but it was not working well with python 3.11 as we can see below:



<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/invoke.png">

<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/invoke2.png">

- they are talking in fix this in suport python in github (https://github.com/pyinvoke/invoke/issues/891)


# Doit

Dependencies are calculated dynamically It is based on Python, so the code form is already known
The files needed to run Doit in this project can be found in [dodo.py](https://github.com/maryamed14/MI-CC-22-23/blob/main/dodo.py)

<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/doitd.png">


<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/doittest.png">



___

## Testing and Assertion Library





Provided test case classes¶

Normal Python unit test classes extend a base class of unittest.TestCase. Django provides a few extensions of this base class:
<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/django_unittest_classes_hierarchy.svg">
### Hierarchy of Django unit testing classes
## SimpleTestCase

class SimpleTestCase¶

A subclass of unittest.TestCase that adds this functionality:

    Some useful assertions like:
        Checking that a callable raises a certain exception.
        Checking that a callable triggers a certain warning.
        Testing form field rendering and error treatment.
        Testing HTML responses for the presence/lack of a given fragment.
        Verifying that a template has/hasn't been used to generate a given response content.
        Verifying that two URLs are equal.
        Verifying an HTTP redirect is performed by the app.
        Robustly testing two HTML fragments for equality/inequality or containment.
        Robustly testing two XML fragments for equality/inequality.
        Robustly testing two JSON fragments for equality.
    The ability to run tests with modified settings.
    
## TransactionTestCase 

class TransactionTestCase¶

TransactionTestCase inherits from SimpleTestCase to add some database-specific features:

    Resetting the database to a known state at the beginning of each test to ease testing and using the ORM.
    Database fixtures.
    Test skipping based on database backend features.
    The remaining specialized assert* methods.

Django’s TestCase class is a more commonly used subclass of TransactionTestCase that makes use of database transaction facilities to speed up the process of resetting the database to a known state at the beginning of each test. A consequence of this, however, is that some database behaviors cannot be tested within a Django TestCase class. For instance, you cannot test that a block of code is executing within a transaction, as is required when using select_for_update(). In those cases, you should use TransactionTestCase.

TransactionTestCase and TestCase are identical except for the manner in which the database is reset to a known state and the ability for test code to test the effects of commit and rollback:

    A TransactionTestCase resets the database after the test runs by truncating all tables. A TransactionTestCase may call commit and rollback and observe the effects of these calls on the database.
    A TestCase, on the other hand, does not truncate tables after a test. Instead, it encloses the test code in a database transaction that is rolled back at the end of the test. This guarantees that the rollback at the end of the test restores the database to its initial state.

## TestCas
As my tests make  database queries, I use subclasses TransactionTestCase and TestCase

## TestCase¶

class TestCase¶

This is the most common class to use for writing tests in Django. It inherits from TransactionTestCase (and by extension SimpleTestCase). If your Django application doesn’t use a database, use SimpleTestCase.

The class:

    Wraps the tests within two nested atomic() blocks: one for the whole class and one for each test. Therefore, if you want to test some specific database transaction behavior, use TransactionTestCase.
    Checks deferrable database constraints at the end of each test.

It also provides an additional method:

classmethod TestCase.setUpTestData()¶

    The class-level atomic block described above allows the creation of initial data at the class level, once for the whole TestCase. This technique allows for faster tests as compared to using setUp().

    For example:
    
```

from django.test import TestCase

class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.foo = Foo.objects.create(bar="Test")
        ...

    def test1(self):
        # Some test using self.foo
        ...

    def test2(self):
        # Some other test using self.foo
        ...

```

### - An example of using Testcase for this project can be found at [tests.py](https://github.com/maryamed14/MI-CC-22-23/blob/main/skincare/tests.py)

<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/Untitled.png">

### In Python, assertions are statements that you can use to set sanity checks during the development process. Assertions allow you to test the correctness of your code by checking if some specific conditions remain true, which can come in handy while you’re debugging code.
### The TestCase class provides several assert methods to check for and report failures. The following table lists the most commonly used methods (see the tables below for more assert methods):
<img src= "https://github.com/maryamed14/MI-CC-22-23/blob/main/docs/imges/ASSERT.png">

```

 assertEqual(first, second, msg=None)

    Test that first and second are equal. If the values do not compare equal, the test will fail.

    In addition, if first and second are the exact same type and one of list, tuple, dict, set, frozenset or str or any type that a subclass registers with addTypeEqualityFunc() the type-specific equality function will be called in order to generate a more useful default error message 
```


# Configure the [cc.yaml](https://github.com/maryamed14/MI-CC-22-23/blob/main/cc.yaml) file properly for testing purposes
