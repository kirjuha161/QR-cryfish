from django.http import HttpResponse
from django.shortcuts import render
import qrcode
from io import BytesIO
import base64


def index(request):
    return render(request, "app/index.html")


def generate_qr(request):
    url = request.GET.get("url")
    if url:
        qr = qrcode.make(url)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)
        qr_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return render(request, "app/qr_result.html", {"qr_image": qr_image})
    else:
        return HttpResponse("No URL provided", status=400)
