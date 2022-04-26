# Django_LibraryManagement

In the LibraryManagement we have only one "books" app where the administrator can create, update, delete the books details using Django Rest Framework (DRF)
The Information of the administrator is stored in sqlite DB whereas the information of the books is stored in mysql Database [i.e we have two DB specified in settings.py]

http://localhost:8000/accounts/login/ for the Admistrator to login and the moment he login he is directed to LOGIN_REDIRECT_URL = "http://localhost:8000/books/books/all/" 
which is specified in settings.py which is a page that stores the information of all the books rules to perform the following using Django Rest Framework
1. Create
2. Update
3. Delete and
4. Show all the books available  

