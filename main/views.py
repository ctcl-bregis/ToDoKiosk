# ToDoKiosk - CTCL 2023
# File: main/views.py
# Purpose: Main app views
# Created: October 31, 2023
# Modified: December 4, 2023

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from app import lib
from app.lib import printe
from markdown import markdown
import caldav
import icalendar
from datetime import date

page_cfg = lib.loadjson("config.json")

if page_cfg == None:
    printe("Configuration file missing: config.json")

dav_url = page_cfg["dav_url"]
cal_name = page_cfg["cal_name"]
username = page_cfg["username"]
password = page_cfg["password"]
strfstr = page_cfg["strftime"]
autoreload = page_cfg["autoreload"]

client = caldav.DAVClient(dav_url, username = username, password = password)
principal = client.principal()

def main(request):
    calendars = []
    tasks = []
    template = loader.get_template("main.html")
    context = lib.mkcontext()

    for todo in client.principal().calendar(cal_name).todos():
        calendars.append(icalendar.Calendar.from_ical(todo.data))

    for calendar in calendars:
        for vtask in calendar.walk("VTODO"):
            print(vtask)
            task = {}
            tcolor = str(vtask.get("COLOR"))

            try:
                task["color"] = tcolor
            except KeyError as err:
                printe(f"Color not found in config.json: {tcolor}")

            task["summary"] = str(vtask.get("SUMMARY"))
            task["created"] = vtask.get("CREATED").dt.strftime(strfstr)
            task["modified"] = vtask.get("LAST-MODIFIED").dt.strftime(strfstr)

            
            tasks.append(task)

    context["autoreload"] = autoreload
    context["tasks"] = tasks
    return HttpResponse(template.render(context, request))