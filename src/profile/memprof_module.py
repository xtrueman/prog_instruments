from memory_profiler import profile

@profile
def import_modules():
    import flask
    del flask
    from django.http import HttpResponse
    from django.urls import path

import_modules()
