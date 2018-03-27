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
six==1.11.0

```
## Self Driven application 
> Rebuild in  -  [2018-3-23] <br>
Firstborn in - [2010-3-28] 


```
│   .gitignore
│   db.sqlite3
│   manage.py
│   README.md
│   TODO.org
│
├───.idea
│   │   dataSources.local.xml
│   │   dataSources.xml
│   │   misc.xml
│   │   modules.xml
│   │   nimak.iml
│   │   vcs.xml
│   │   workspace.xml
│   │
│   ├───dataSources
│   │   │   e478ae7f-ecc1-4ed9-ac3e-16fd9d0cf0de.xml
│   │   │
│   │   └───e478ae7f-ecc1-4ed9-ac3e-16fd9d0cf0de
│   │       └───storage_v2
│   │           └───_src_
│   │               └───schema
│   │                       main.uQUzAA.meta
│   │
│   └───inspectionProfiles
├───app
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   0001_initial.py
│   │   │   0002_auto_20180323_1323.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           0001_initial.cpython-36.pyc
│   │           0002_auto_20180323_1323.cpython-36.pyc
│   │           __init__.cpython-36.pyc
│   │
│   ├───static
│   │   └───app
│   │       │   favicon.ico
│   │       │
│   │       ├───css
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
│   │       ├───images
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
│   │       │   │   │   │
│   │       │   │   │   └───_notes
│   │       │   │   └───_notes
│   │       │   └───_notes
│   │       ├───inc
│   │       │   │   sendEmail.php
│   │       │   │
│   │       │   └───_notes
│   │       └───js
│   │           │   jquery-2.1.3.min.js
│   │           │   main.js
│   │           │   modernizr.js
│   │           │   pace.min.js
│   │           │   plugins.js
│   │           │
│   │           └───_notes
│   ├───templates
│   │   └───app
│   │           post_detail.html
│   │           post_list.html
│   │
│   └───__pycache__
│           admin.cpython-36.pyc
│           apps.cpython-36.pyc
│           models.cpython-36.pyc
│           urls.cpython-36.pyc
│           views.cpython-36.pyc
│           __init__.cpython-36.pyc
│
├───media
│   └───posts
│           123.png
│           123_sUtBGEo.png
│
├───nimak
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│   │
│   └───__pycache__
│           settings.cpython-36.pyc
│           urls.cpython-36.pyc
│           wsgi.cpython-36.pyc
│           __init__.cpython-36.pyc
│
├───static
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
│           └───vendor
│               ├───jquery
│               │       jquery.js
│               │       jquery.min.js
│               │       LICENSE-JQUERY.txt
│               │
│               ├───select2
│               │   │   LICENSE-SELECT2.md
│               │   │   select2.full.js
│               │   │   select2.full.min.js
│               │   │
│               │   └───i18n
│               │           ar.js
│               │           az.js
│               │           bg.js
│               │           ca.js
│               │           cs.js
│               │           da.js
│               │           de.js
│               │           el.js
│               │           en.js
│               │           es.js
│               │           et.js
│               │           eu.js
│               │           fa.js
│               │           fi.js
│               │           fr.js
│               │           gl.js
│               │           he.js
│               │           hi.js
│               │           hr.js
│               │           hu.js
│               │           id.js
│               │           is.js
│               │           it.js
│               │           ja.js
│               │           km.js
│               │           ko.js
│               │           lt.js
│               │           lv.js
│               │           mk.js
│               │           ms.js
│               │           nb.js
│               │           nl.js
│               │           pl.js
│               │           pt-BR.js
│               │           pt.js
│               │           ro.js
│               │           ru.js
│               │           sk.js
│               │           sr-Cyrl.js
│               │           sr.js
│               │           sv.js
│               │           th.js
│               │           tr.js
│               │           uk.js
│               │           vi.js
│               │           zh-CN.js
│               │           zh-TW.js
│               │
│               └───xregexp
│                       LICENSE-XREGEXP.txt
│                       xregexp.js
│                       xregexp.min.js
│
└───templates
    │   base.html
    │   index.html
    │   portfolio.html
    │   resume.html
    │
    └───include
            _menu.html

```