# ToDoKiosk - CTCL 2023-2024
# File: main/views.py
# Purpose: Main app views
# Created: October 31, 2023
# Modified: January 5, 2024

from django.template.defaulttags import register
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from app import __version__
from app import lib
from app.lib import printe
from markdown import markdown
import caldav
import icalendar
import os
from datetime import date

if os.path.exists("config_private.json"):
    page_cfg = lib.loadjson("config_private.json")
elif os.path.exists("config.json"):
    page_cfg = lib.loadjson("config.json")
else:
    printe("Configuration file missing: config.json")

dav_url = page_cfg["dav_url"]
cal_name = page_cfg["cal_name"]
username = page_cfg["username"]
password = page_cfg["password"]
strfstr = page_cfg["strftime"]
autoreload = page_cfg["autoreload"]

try:
    client = caldav.DAVClient(dav_url, username = username, password = password)
except Exception as err:
    printe(err)

try:
    principal = client.principal()
except Exception as err:
    printe(err)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def main(request):
    calendars = []
    tasks = []
    template = loader.get_template("main.html")
    context = lib.mkcontext()

    try:
        for todo in client.principal().calendar(cal_name).todos():
            calendars.append(icalendar.Calendar.from_ical(todo.data))
    except Exception as err:
        printe(err)

    for calendar in calendars:
        for vtask in calendar.walk("VTODO"):
            task = {}
            tcolor = str(vtask.get("COLOR"))

            if tcolor != "None":
                try:
                    task["color"] = page_cfg["colors"][tcolor]
                except KeyError:
                    printe(f"Color not found in config.json: {tcolor}")
            else:
                task["color"] = "#ffffff"

            tstatus = str(vtask.get("STATUS"))
            if tstatus != "None":
                try:
                    task["status"] = page_cfg["status"][tstatus]
                except KeyError:
                    printe(f"Status type not found in config.json: {tstatus}")
            else:
                task["status"] = "No Status"

            task["priority"] = str(vtask.get("PRIORITY"))
            task["summary"] = str(vtask.get("SUMMARY"))
            task["created"] = vtask.get("CREATED").dt.strftime(strfstr)
            task["modified"] = vtask.get("LAST-MODIFIED").dt.strftime(strfstr)

            tasks.append(task)


    # Get list of tasks without a priority and a list of tasks that do have a priority
    taskswithpriority = []
    taskswithoutpriority = []
    for task in tasks:
        if task["priority"] == "0":
            taskswithoutpriority.append(task)
        else:
            taskswithpriority.append(task)

    # Defaults to descending order if an invalid configuration option is given
    if page_cfg["priority_sort"] == "descending":
        taskswithpriority = sorted(taskswithpriority, key=lambda d: d["priority"], reverse = False)
    elif page_cfg["priority_sort"] == "ascending":
        taskswithpriority = sorted(taskswithpriority, key=lambda d: d["priority"], reverse = True)
    elif page_cfg["priority_sort"] == "none":
        pass
    else:
        taskswithpriority = sorted(taskswithpriority, key=lambda d: d["priority"], reverse = False)

    tasks = taskswithpriority + taskswithoutpriority

    context["cal_name"] = cal_name
    context["title"] = cal_name
    context["autoreload"] = autoreload
    context["tasks"] = tasks
    context["version"] = __version__

    context["priority"] = page_cfg["priority"]

    return HttpResponse(template.render(context, request))
