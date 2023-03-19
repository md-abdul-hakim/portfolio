from django.shortcuts import render, redirect, HttpResponse
from base.models import (
                    Profile, About, Skill, Service,
                    Education, Experience, Message, Location,
                    Category, Blog
                )

import os
import folium
import geocoder

# Create your views here.
def index(request):
    profiles = Profile.objects.filter(is_active=True)
    abouts = About.objects.filter(is_active=True)
    skills = Skill.objects.filter(category='technical')
    services = Service.objects.filter(is_active=True)
    t_skills = Skill.objects.filter(category='technical')
    p_skills = Skill.objects.filter(category='professional')
    educations = Education.objects.filter(is_active=True)
    experiences = Experience.objects.filter(is_active=True)
    address = Location.objects.all().last()
    categories = Category.objects.all().order_by('name')
    blogs = Blog.objects.all()
    
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')

    m = folium.Map(location=[19, -12], zoom_start=2)
    folium.Marker([lat, lng], tooltip='Click for more', popup=address).add_to(m)
    m = m._repr_html_()
    
    # shp_dir = os.path.join(os.getcwd(),'media_root','shp')
    # m = folium.Map(location=[-16.22,-71.59],zoom_start=10)
    # style_basin = {'fillColor': '#228B22', 'color': '#228B22'}
    # folium.GeoJson(os.path.join(shp_dir,'map.json'),name='basin',style_function=lambda x:style_basin).add_to(m)
    # folium.LayerControl().add_to(m)
    # m=m._repr_html_()

    context = {
        'profiles': profiles,
        'abouts': abouts,
        'skills': skills,
        'services': services,
        't_skills': t_skills,
        'p_skills': p_skills,
        'educations': educations,
        'experiences': experiences,
        'categories': categories,
        'blogs': blogs,
        'my_map': m,
    }
    return render(request, 'home.html', context)
def message(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        obj = Message(first_name=first_name, last_name=last_name, email=email, message=message)
        obj.save()
    return redirect('index')

def location(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        date = request.POST.get('date')
        obj = Location(address=address, date=date)
        obj.save()
        return redirect('index')
    return render(request, 'home.html')

def blog(request, id):
    if id == None:
        blogs = Blog.objects.all()
    else:
        blogs = Blog.objects.get(blog.category.id == id)
    context = {
        'blogs':blogs,
    }
    return render(request, 'home.html', context)