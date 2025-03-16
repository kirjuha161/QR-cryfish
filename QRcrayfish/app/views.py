from django.http import HttpResponse
from django.shortcuts import render
import qrcode
from io import BytesIO


def index(request):
    return render(request, "app/index.html")


def generate_qr(request):
    url = request.GET.get("url")
    if url:
        qr = qrcode.make(url)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)
        return HttpResponse(buffer, content_type="image/png")
    else:
        return HttpResponse("No URL provided", status=400)
