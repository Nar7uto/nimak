# **Nima Karimi** 
`https://nim4.ir` <br> 

> `python 3.6`<br> 
`django 2.0.3`<br>
`nginx 11.09.2` <br>
`ubuntu 16.04 LTS`

* Document available in Files :)
```
beautifulsoup4==4.4.0
coverage==4.4
csscompressor==0.9.4
Cython==0.28.1
Django==2.0.3
django-appconf==1.0.2
django-classy-tags==0.8.0
django-compressor==2.2
django-sekizai==0.9.0
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
## Self Driven application 
> Rebuild in  -  [2018-3-23] <br>
Firstborn in - [2010-3-28] 


```

├───app
│   │   admin.py --> Register Model in Admin Django
│   │   apps.py --> App Config
│   │   models.py --> database Models
│   │   tests.py
│   │   urls.py --> Url Include to main
│   │   views.py --> View Func and Class
│   │   __init__.py
│   │
│   ├───static
│   │   └───app --> App Static Files
│   │       │   favicon.ico
│   │       │
│   │       ├───css --> include all Stylesheet
│   │       │   │   base.css
│   │       │   │   fonts.css
│   │       │   │   main.css
│   │       │   │   style.css
│   │       │   │   vendor.css
│   │       │   │
│   │       │   ├───font-awesome
│   │       │   │   ├───css
│   │       │   │   │   │   font-awesome.css
│   │       │   │   │   │   font-awesome.min.css
│   │       │   │   │   │
│   │       │   │   │   └───_notes
│   │       │   │   └───fonts
│   │       │   │       │   fontawesome-webfont.eot
│   │       │   │       │   fontawesome-webfont.svg
│   │       │   │       │   fontawesome-webfont.ttf
│   │       │   │       │   fontawesome-webfont.woff
│   │       │   │       │   FontAwesome.otf
│   │       │   │       │
│   │       │   │       └───_notes
│   │       │   └───micons
│   │       │       │   micons.css
│   │       │       │
│   │       │       ├───fonts
│   │       │       │   │   icomoon.eot
│   │       │       │   │   icomoon.svg
│   │       │       │   │   icomoon.ttf
│   │       │       │   │   icomoon.woff
│   │       │       │   │
│   │       │       │   └───_notes
│   │       │       └───_notes
│   │       ├───fonts
│   │       │   ├───lora
│   │       │   │   │   lora-bold-webfont.eot
│   │       │   │   │   lora-bold-webfont.svg
│   │       │   │   │   lora-bold-webfont.ttf
│   │       │   │   │   lora-bold-webfont.woff
│   │       │   │   │   lora-bolditalic-webfont.eot
│   │       │   │   │   lora-bolditalic-webfont.svg
│   │       │   │   │   lora-bolditalic-webfont.ttf
│   │       │   │   │   lora-bolditalic-webfont.woff
│   │       │   │   │   lora-italic-webfont.eot
│   │       │   │   │   lora-italic-webfont.svg
│   │       │   │   │   lora-italic-webfont.ttf
│   │       │   │   │   lora-italic-webfont.woff
│   │       │   │   │   lora-regular-webfont.eot
│   │       │   │   │   lora-regular-webfont.svg
│   │       │   │   │   lora-regular-webfont.ttf
│   │       │   │   │   lora-regular-webfont.woff
│   │       │   │   │   stylesheet.css
│   │       │   │   │
│   │       │   │   └───_notes
│   │       │   └───poppins
│   │       │       │   poppins-bold-webfont.eot
│   │       │       │   poppins-bold-webfont.svg
│   │       │       │   poppins-bold-webfont.ttf
│   │       │       │   poppins-bold-webfont.woff
│   │       │       │   poppins-bold-webfont.woff2
│   │       │       │   poppins-light-webfont.eot
│   │       │       │   poppins-light-webfont.svg
│   │       │       │   poppins-light-webfont.ttf
│   │       │       │   poppins-light-webfont.woff
│   │       │       │   poppins-light-webfont.woff2
│   │       │       │   poppins-medium-webfont.eot
│   │       │       │   poppins-medium-webfont.svg
│   │       │       │   poppins-medium-webfont.ttf
│   │       │       │   poppins-medium-webfont.woff
│   │       │       │   poppins-medium-webfont.woff2
│   │       │       │   poppins-regular-webfont.eot
│   │       │       │   poppins-regular-webfont.svg
│   │       │       │   poppins-regular-webfont.ttf
│   │       │       │   poppins-regular-webfont.woff
│   │       │       │   poppins-regular-webfont.woff2
│   │       │       │   poppins-semibold-webfont.eot
│   │       │       │   poppins-semibold-webfont.svg
│   │       │       │   poppins-semibold-webfont.ttf
│   │       │       │   poppins-semibold-webfont.woff
│   │       │       │   poppins-semibold-webfont.woff2
│   │       │       │   stylesheet.css
│   │       │       │
│   │       │       └───_notes
│   │       ├───images --> Static Images
│   │       │   │   Avatar.jpg
│   │       │   │   bg.jpg
│   │       │   │   intro-bg1.jpg
│   │       │   │   logo3.png
│   │       │   │   nima-karimi.png
│   │       │   │   sample-image.jpg
│   │       │   │
│   │       │   ├───portfolio
│   │       │   │   │   dev.jpg
│   │       │   │   │   sof.jpg
│   │       │   │   │   ux.jpg
│   │       │   │   │   wb.jpg
│   │       │   │   │
│   │       │   │   ├───modals
│   │       │   │   │   │   m-dev.jpg
│   │       │   │   │   │   m-ux.jpg
│   │       │   │   │   │   m-wb.jpg
│   │       └───js --> include all Js 
│   │           │   jquery-2.1.3.min.js
│   │           │   main.js
│   │           │   modernizr.js
│   │           │   pace.min.js
│   │           │   plugins.js
│   │           
│   │ 
│   ├───templates --> App Template 
│   │   └───app
│   │           post_detail.html --> Post Detail View
│   │           post_list.html --> Post List View
│               post_tag.html --> Post Tag View
│
├───media --> Upload Dir from Admin Panel
│   └───posts
│           123.png
│           123_sUtBGEo.png
│
├───nimak --> MAIN PROJECT FILEs
│   │   settings.py --> ** Most Important 
│   │   urls.py --> Urls 
│   │   wsgi.py
│   │   __init__.py
│   │
│
├───static --> Collected Static File 
│   └───admin
│       ├───css
│       │   │   autocomplete.css
│       │   │   base.css
│       │   │   changelists.css
│       │   │   dashboard.css
│       │   │   fonts.css
│       │   │   forms.css
│       │   │   login.css
│       │   │   responsive.css
│       │   │   responsive_rtl.css
│       │   │   rtl.css
│       │   │   widgets.css
│       │   │
│       │   └───vendor
│       │       └───select2
│       │               LICENSE-SELECT2.md
│       │               select2.css
│       │               select2.min.css
│       │
│       ├───fonts
│       │       LICENSE.txt
│       │       README.txt
│       │       Roboto-Bold-webfont.woff
│       │       Roboto-Light-webfont.woff
│       │       Roboto-Regular-webfont.woff
│       │
│       ├───img
│       │   │   calendar-icons.svg
│       │   │   icon-addlink.svg
│       │   │   icon-alert.svg
│       │   │   icon-calendar.svg
│       │   │   icon-changelink.svg
│       │   │   icon-clock.svg
│       │   │   icon-deletelink.svg
│       │   │   icon-no.svg
│       │   │   icon-unknown-alt.svg
│       │   │   icon-unknown.svg
│       │   │   icon-yes.svg
│       │   │   inline-delete.svg
│       │   │   LICENSE
│       │   │   README.txt
│       │   │   search.svg
│       │   │   selector-icons.svg
│       │   │   sorting-icons.svg
│       │   │   tooltag-add.svg
│       │   │   tooltag-arrowright.svg
│       │   │
│       │   └───gis
│       │           move_vertex_off.svg
│       │           move_vertex_on.svg
│       │
│       └───js
│           │   actions.js
│           │   actions.min.js
│           │   autocomplete.js
│           │   calendar.js
│           │   cancel.js
│           │   change_form.js
│           │   collapse.js
│           │   collapse.min.js
│           │   core.js
│           │   inlines.js
│           │   inlines.min.js
│           │   jquery.init.js
│           │   popup_response.js
│           │   prepopulate.js
│           │   prepopulate.min.js
│           │   prepopulate_init.js
│           │   SelectBox.js
│           │   SelectFilter2.js
│           │   timeparse.js
│           │   urlify.js
│           │
│           ├───admin
│           │       DateTimeShortcuts.js
│           │       RelatedObjectLookups.js
│           │
│
└───templates --> Main Template 
    │   base.html --> Base template for extends
    │   index.html
    │   portfolio.html
    │   resume.html
    │
    └───include
            _menu.html --> Include to Base template

```