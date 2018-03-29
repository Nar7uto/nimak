# ✅ *Nima Karimi* - 2018
`https://nim4.ir` <br> 

> `python 3.6`<br> 
`django 2.0.3`<br>
`nginx 11.09.2` <br>
`ubuntu 16.04 LTS`
## Self Driven application 
> Rebuild in  -  [2018-3-23] <br>
Firstborn in - [2010-3-28] 

****

### Requirments: 
 Document available in Files  🕶
```
beautifulsoup4==4.4.0
coverage==4.4
csscompressor==0.9.4
Cython==0.28.1
Django==2.0.3
django-analytical==2.4.0
django-appconf==1.0.2
django-classy-tags==0.8.0
django-compressor==2.2
django-sekizai==0.9.0
django-summernote==0.8.8.6
django-taggit==0.22.2
flake8==2.4.0
html5lib==0.9999999
Jinja2==2.7.3
MarkupSafe==1.0
mccabe==0.3.1
mock==1.0.1
pep8==1.5.7
Pillow==5.0.0
pyflakes==0.8.1
pytz==2018.3
rcssmin==1.0.6
rjsmin==1.0.12
six==1.11.0

```

```
│   .gitignore
│   db.sqlite3 --> For make data base use makemigrations , migrate
│   manage.py --> Commender 
│   README.md 
│   requirment.txt --> package list for install
│   TODO.org --> Private :D
├───app
│   │   admin.py --> Register Model in Admin Django
│   │   apps.py --> App Config
│   │   models.py --> database Models
│   │   tests.py
│   │   urls.py --> Url Include to main
│   │   views.py --> View Func and Class
│   │   __init__.py
│   │
│   ├───migrations
│   ├───static
│   │   └───app
│   │       │   favicon.ico
│   │       │
│   │       ├───css
│   │       │   ├───font-awesome
│   │       │   │   ├───css
│   │       │   │   └───fonts
│   │       │   └───micons
│   │       ├───fonts
│   │       │   ├───lora
│   │       │   └───poppins
│   │       ├───images
│   │       │   ├───portfolio
│   │       └───js
│   ├───templates --> Template Dir in app 
│   │   └───app
│   │           post_archive_year.html --> Years View
│   │           post_detail.html --> Generic Detail View
│   │           post_list.html --> Generic List view
│   │           post_tag.html --> Mixin Tag View
|
├───media --> Dir for Upload Medias from Django Panel
│   ├───django-summernote --> Text Editor
│   ├───portfolio --> Image upload for portfolio
│   ├───posts --> Image upload for post
│   └───resume --> Image upload for resume
│
├───nimak --> MAIN PROJECT FILEs
│   │   settings.py --> ** MOST IMPORTANT FILE **
│   │   urls.py --> conf url ( extents url from main app url)
│   │   wsgi.py
│   │   __init__.py
|
├───static
│   ├───admin --> collect Static for admin django
│   ├───app --> collect Static 
│   │   │   favicon.ico
│   │   │
│   │   ├───css --> 
|   |   ├─── fonts
│   │   ├───images
│   │   └───js
│   │
│   ├───CACHE --> Compressor make these Files :)
│   │   ├───css
│   │   └───js
│   └───summernote --> text Editor static
│       ├───font
│       └───lang
│
└───templates --> Main template Dir
    │   base.html  --> Base template for extent in all
    │   contact.html
    │   index.html
    │   portfolio.html
    │   resume.html
    │
    └───include  --> Include to Base template
            _menu.html --> Menu File To edit Urls

```