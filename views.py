from django.shortcuts import render
from testapp.models import Doctor
from django.core.paginator import Paginator

def home_view(request):
    return render(request,"home.html")

def doctor_read_view(request):
    doc_list=Doctor.objects.all()
    paginator=Paginator(doc_list,3)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)

    name=request.GET.get('name')
    if name!='' and name is not None:
        page_obj=doc_list.filter(doctor_name__contains=name)


    my_dict={'page_obj':page_obj}
    return render(request,"docread.html",my_dict)
