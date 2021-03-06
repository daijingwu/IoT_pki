# IoT_pki
Public Key Infrastructure for IoT devices built in python django

# Functionality
API interface allows clients to:

* Request new X509 certificates (subject to approval)
* Download new X509 certificates once approved
* Renew existing valid X509 certificates

Admin interface allows administrators to:

* Create self signed Certificate Authority to sign certificate requests
* View and approve X509 certificate requests
* View and revoke existing X509 certificates

# Documentation

https://docs.zibawa.com/doku.php?id=pki:start



# Quick start

Below are instructions for installing IoT_pki to an EXISTING django project.
Alternatively you can install as a stand alone django project as explained in https://docs.zibawa.com
This assumes that you already have an existing django project to which you want to add PKI module.

If you want to create an empty django project to install PKI into, then:

Create Virtual Environment for Python3
<code>
mkdir virtualenv
cd virtualenv
python3 -m venv iotpki
source iotpki/bin/activate
</code>
(iotpki)$



## Install Django and IoT-pki 

```
pip install django
pip install django-IoT-pki
```

Create empty Django Project
```
django-admin startproject mytestpki
```


## Create directory for logs (optional)

```
sudo mkdir /var/log/zibawa
sudo chmod 751 /var/log/zibawa
sudo chown -R zibawa:zibawa /var/log/zibawa
```



## Create Super User

```
python manage.py createsuperuser
```

## settings.py



Add hostname to allowed hosts

ALLOWED_HOSTS = ['localhost','127.0.0.1','.zibawa.com','.myserver.com']

Add IoT_pki and rest_framework to Installed apps

INSTALLED_APPS = [
.....
'IoT_pki',
'rest_framework',
]


Add the following settings to your settings.py if you dont have them already defined.
```
#redirects users to admin interface for login
LOGIN_URL='/admin/'
LOGIN_REDIRECT_URL = '/admin/'
#pki sends new certs to any user when defined in email request
EMAIL_HOST = 'smtp.mymail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'me@mymail.com'
EMAIL_HOST_PASSWORD = 'mypass'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL='me@mymail.com'


#used to create and renew X509 certificates.  The certificate and key used at below location will be used to sign
#all certificates generated by PKI
PKI={'host':'secret.myserver.com','port':443,
     
     'use_ssl':True,#should always be True except for testing
     'verify_certs':False,#verify identity of server should be True except for testing
     'path_to_ca_cert':'/path/to/ca.pem',
     'path_to_ca_key':'/path/to/ca.key',
     'path_to_certstore':'/home/myCA/certs/',#requires trailing slash, place to keep CA certs
     'path_to_keystore':'/home/myCA/private/',#requires trailing slash. place to keep ca keys should be permission 400
     'auto_approve_requests':False,#should be FALSE (true will automatically approve all requests)
     }

CERT_DEFAULTS={'country_name':"ES",#obligatory must be 2 letter country code 
               'state_or_province_name':"Barcelona",
               'valid_days':365,#validity of certificates generated must be integer not string
               'min_days_remaining_for_renewal':400
               
               }


#used as part of PKI
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}
```



## urls.py

If you are installing IoT_pki as a stand alone from github, the below is not necessary, since you will install urls.py as part of the github package.  However, if you are adding to an existing django project, you will need to include the following:

In your main urls.py you need to add the following (to use the Django Rest Framework)
```
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from IoT_pki import views

router = routers.DefaultRouter()


urlpatterns = [
    
    
    url(r'^admin/', admin.site.urls),
    url(r'^IoT_pki/', include('IoT_pki.urls',namespace='IoT_pki')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='zibawa_PKI'))
    
    
    
]
```


## Perform Database Migration
Move into your project directory that should have been created just below where you are.

cd mytestpki
python manage.py migrate


## Start the development server


python manage.py runserver
