from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from django.shortcuts import render,redirect
from .models import Document
from .forms import DocumentForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
 
# @method_decorator(csrf_exempt, name='dispatch')
def my_view(request):
    # print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        # print((request.FILES))
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'],desc=request.POST['desc'])
            newdoc.save()
 
            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form
 
    # Load documents for the list page
    documents = Document.objects.all()
    # print(documents)
    # Render list page with the documents and the form
    # print(form)
    context = {'documents': documents, 'form': form, 'message': message}
    # return JsonResponse(documents)
    return render(request, 'list.html', context)    




# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({"test":"hello"})

def productSerialiaze(productObj):
    return {
                "desc":productObj.desc,
                "price":productObj.price,
                "id":productObj._id,
                "img":str( productObj.image),
                "user":{
                "Email": productObj.user.email,
                "Name":str( productObj.user)
                }
                }

# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def products(request,id=-1):
    if request.method == 'GET':    #method get all
        if int(id) > -1: #get single product
            productObj= Product.objects.get(_id = id)
            return JsonResponse(productSerialiaze(productObj),safe=False)
        else: # return all
            res=[] #create an empty list
            for productObj in Product.objects.all(): #run on every row in the table...
                res.append(productSerialiaze(productObj)) #append row by to row to res list
            return JsonResponse(res,safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Product.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})
    if request.method == 'DELETE': #method delete a row
        temp= Product.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PUT': #method delete a row
        temp=Product.objects.get(_id = id)

        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()

        print(request.data['prodName'])
        return JsonResponse({'PUT': id})


