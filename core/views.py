from django.http import JsonResponse

# from django.shortcuts import render


def health(_request):
    return JsonResponse({"status": "ok"})
