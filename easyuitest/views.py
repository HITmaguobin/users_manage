from django.shortcuts import render,HttpResponse, HttpResponseRedirect
import importlib, sys
from easyuitest import models
import json
importlib.reload(sys)

# Create your views here.
# def index(request):
#     return render(request,'info.html')
#     # return HttpResponseRedirect("http://127.0.0.1:8000/start/")
def app_start(request):
    if request.method=="POST":
        print("POST")
        print(request.POST)
        name=request.POST.get('name')
        password = request.POST.get('password')
        role = request.POST.get('role')
        creator = request.POST.get('creator')
        createTime = request.POST.get('createTime')
        editor=request.POST.get('editor')
        editTime = request.POST.get('editTime')
        isValid = request.POST.get('isValid')
        dic={"name":name,"password":password,"role":role,"creator":creator,
             "createTime":createTime,"editor":editor,"editTime":editTime,"isValid":isValid}
        models.users_msg.objects.create(**dic)
        return HttpResponse("save")
    else:
        print("isnull!")
    return render(request,'info.html')

def read_all_sql(request):
    obj_all=models.users_msg.objects.all()
    # print(obj_all)
    ealist=[]
    for li in obj_all:
        ealist.append({"name":li.name,"password":li.password,"role":li.role,"creator":li.creator,
             "createTime":li.createTime,"editor":li.editor,"editTime":li.editTime,"isValid":li.isValid,"id":li.id})
    ealist_len=json.dumps(len(ealist))
    json_data_list = {'rows': ealist, 'total': ealist_len}
    easyList = json.dumps(json_data_list)
    return HttpResponse(easyList)
def Edit_user(request, id):
    print("这是编辑的："+id)
    print(request.method)
    if request.method=='POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        role = request.POST.get('role')
        creator = request.POST.get('creator')
        createTime = request.POST.get('createTime')
        editor = request.POST.get('editor')
        editTime = request.POST.get('editTime')
        isValid = request.POST.get('isValid')
        dic = {"name": name, "password": password, "role": role, "creator": creator,
               "createTime": createTime, "editor": editor, "editTime": editTime, "isValid": isValid}
        print(dic)
        models.users_msg.objects.filter(id=id).update(**dic)
        return HttpResponse("edit_ok")

def Remove_user_id(request):
    if request.method=="POST":
        print("REMOVE POST")
        id=request.POST.get('id')
        print(id)
        models.users_msg.objects.filter(id=id).delete()
    return HttpResponse("REMOVE")

def login(request):
    return render(request,"login.html")

def read_all_sql_urlmanage(request):
    obj_all=models.url_manage.objects.all()
    # print(obj_all)
    ealist=[]
    for li in obj_all:
        ealist.append({"url_source":li.url_source,"link":li.link,"createTime":li.createTime,"creator":li.creator,
             "timeconfig":li.timeconfig,"isValid":li.isValid,"id":li.id})
    ealist_len=json.dumps(len(ealist))
    json_data_list = {'rows': ealist, 'total': ealist_len}
    easyList = json.dumps(json_data_list)
    return HttpResponse(easyList)

def url_start(request):
    if request.method=="POST":
        print("POST")
        print(request.POST)
        url_source=request.POST.get('url_source')
        link = request.POST.get('link')
        creator = request.POST.get('creator')
        createTime = request.POST.get('createTime')
        timeconfig=request.POST.get('timeconfig')
        isValid = request.POST.get('isValid')
        dic={"url_source":url_source,"link":link,"creator":creator,
             "createTime":createTime,"timeconfig":timeconfig,"isValid":isValid}
        models.url_manage.objects.create(**dic)
        return HttpResponse("save")
    else:
        print("isnull!")
    return render(request,'spiderdata.html')

def Edit_url(request,id):
    print("这是编辑的数据源：" + id)
    print(request.method)
    if request.method == 'POST':
        url_source = request.POST.get('url_source')
        link = request.POST.get('link')
        creator = request.POST.get('creator')
        createTime = request.POST.get('createTime')
        timeconfig = request.POST.get('timeconfig')
        isValid = request.POST.get('isValid')
        dic = {"url_source": url_source, "link": link, "creator": creator,
               "createTime": createTime, "timeconfig": timeconfig, "isValid": isValid}
        print(dic)
        models.url_manage.objects.filter(id=id).update(**dic)
        return HttpResponse("edit_ok")
def remove_url(request):
    if request.method=="POST":
        print("REMOVE POST")
        id=request.POST.get('id')
        print(id)
        models.url_manage.objects.filter(id=id).delete()
    return HttpResponse("REMOVE")












