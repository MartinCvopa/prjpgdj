from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse


from django.db import connection
def uptime_info(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT date_trunc('second', current_timestamp - pg_postmaster_start_time()) as uptime")
        uptime_value = str(cursor.fetchone()[0])
        uptime_value = uptime_value.replace(",", "")
    return JsonResponse({ "pgsql": { "uptime": uptime_value } })
