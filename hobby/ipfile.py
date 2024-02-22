from django.shortcuts import render
from ip2geotools.databases.noncommercial import DbIpCity
def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    ip = "i do not know "
    res =None
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
        res = DbIpCity.get(ip, api_key="free")


    else:
        ip = request.META.get("REMOTE_ADDR")
        res = DbIpCity.get(ip, api_key="free")

    return render(request, "index.html", {"ip": ip ,"country" :res.country,"city":res.city})
