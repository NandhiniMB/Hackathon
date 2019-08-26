from django.shortcuts import render
from django.db.models import F
from django.conf import settings
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Utilities,Utility_Category
from django.contrib.gis.db.models import PointField
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance  


# distance_miles_to_search = 50
# point = PointField()  # get a point of a particular place (usually by latitude/longitude)
# ans = Utilities.objects.filter(utilities__location__distance_lte=(point, D(mi=distance_miles_to_search))).annotate(closest_utilit_id=F('places__city'))

# Create your views here.
@login_required
def myapp(request):
    return render(request, "login.html", {'status': 200})

def myhome(request):
    #import ipdb;ipdb.set_trace()
    u_cat=Utility_Category.objects.all().values('name')
    args={
    'u' : u_cat
    }
    return render(request, "home.html", args)

def findplaces(request):
   # # import ipdb;ipdb.set_trace()
   #  # if request.method == 'POST':
   #  #     data=request.POST
   #  point=[]
   #  pdict={}
   #  option = 'Theaters'
   #  u_cat=Utility_Category.objects.filter(name = 'Theaters').values('id')
   #  utilities=Utilities.objects.filter(utility__id__in=u_cat).values('location')
   #  for utility in utilities:
   #      pdict['lat']=utility['location'].x
   #      pdict['lon']=utility['location'].y
   #      point.append(pdict)
    return JsonResponse(point,safe=False)
def closest(request):
    #import ipdb;ipdb.set_trace()
    # data={}
    # closest=[]
    # closestdict={}
    # data['lat']=13.021722
    # data['long']=77.643439
    # u_cat=Utility_Category.objects.filter(name = 'Theaters').values('id')
    # location=Utilities.objects.filter(utility__id__in=u_cat).values('location')    
    # for loc in location:
    #     if((loc['location'].y > (data['lat']-1)) and (loc['location'].y < (data['lat']+1 ))):
    #           if((loc['location'].x > (data['long']-1)) and (loc['location'].x < (data['long']+1 ))):
    #               closestdict['lat']=loc['location'].x
    #               closestdict['lon']=loc['location'].y
    #               closest.append(closestdict.copy())
    data=request.POST
    # lat=13.021722
    # lng=77.643439
    lat = data['c_lat']
    lng = data['c_lng']
    option=data['option']
    dist=data['distance']
    places_list=[]
    places_dict={}
    if (data['distance']=='2 kms'):
        radius = 10
    elif(data['distance']=='3 kms'):
        radius = 15
    elif(data['distance']=='5 kms'):
         radius = 25
    else:
        point = Point(float(lng),float(lat))   
        u_cat=Utility_Category.objects.filter(name = option).values('id')
        utilities=Utilities.objects.filter(utility__id__in=u_cat).values('location','name')
        for utility in utilities:
            places_dict['lat']=utility['location'].x
            places_dict['lng']=utility['location'].y
            places_dict['name']=utility['name']
            places_list.append(places_dict.copy())
        return JsonResponse(places_list,safe=False)

    point = Point(float(lng),float(lat))   
    u_cat=Utility_Category.objects.filter(name = option).values('id')
    utilities=Utilities.objects.filter(utility__id__in=u_cat,location__distance_lt=(point, Distance(km=radius))).values('location','name')
    for utility in utilities:
        places_dict['lat']=utility['location'].x
        places_dict['lng']=utility['location'].y
        places_dict['name']=utility['name']
        places_list.append(places_dict.copy())
    return JsonResponse(places_list,safe=False)
                 




    