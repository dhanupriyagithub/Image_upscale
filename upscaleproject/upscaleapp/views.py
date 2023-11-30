from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import io
from .forms import ImageUploadForm

def upscale_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded image from the form
            uploaded_image = form.cleaned_data['image']
            # Open the uploaded image with Pillow
            image = Image.open(uploaded_image)
            # Upscale the image
            if 'btn1' in request.POST:
                if image.width > 1200 or image.height > 1200:
                   return render(request, 'upscale.html', {'error_message':'***Image size exceeds the maximum limit of 1200 x 1200.***'})
                upscaled_image = image.resize((image.width * 2, image.height * 2), resample=Image.BICUBIC)
                buffer = io.BytesIO()
                file_format = 'JPEG' if upscaled_image.format == 'JPEG' else 'PNG'
                upscaled_image.save(buffer, format=file_format)
                content_type = 'image/jpeg' if file_format == 'JPEG' else 'image/png'
                response = HttpResponse(buffer.getvalue(), content_type=content_type)
                response['Content-Disposition'] = 'attachment; filename="{}"'.format('upscale2_'+ uploaded_image.name)
                return response  
            elif 'btn2' in request.POST:
                if image.width > 1200 or image.height > 1200:
                   return render(request, 'upscale.html', {'error_message':'***Image size exceeds the maximum limit of 1200 x 1200.***'})
                upscaled_image = image.resize((image.width * 4, image.height * 4), resample=Image.BICUBIC)
                buffer = io.BytesIO()
                file_format = 'JPEG' if upscaled_image.format == 'JPEG' else 'PNG'
                upscaled_image.save(buffer, format=file_format)
                content_type = 'image/jpeg' if file_format == 'JPEG' else 'image/png'
                response = HttpResponse(buffer.getvalue(), content_type=content_type)
                response['Content-Disposition'] = 'attachment; filename="{}"'.format('upscale3_'+ uploaded_image.name)
                return response
            elif 'btn3' in request.POST:
                if image.width > 1200 or image.height > 1200:
                   return render(request, 'upscale.html', {'error_message':'***Image size exceeds the maximum limit of 1200 x 1200.***'})
                upscaled_image = image.resize((image.width * 6, image.height * 6), resample=Image.BICUBIC) 
                buffer = io.BytesIO()
                file_format = 'JPEG' if upscaled_image.format == 'JPEG' else 'PNG'
                upscaled_image.save(buffer, format=file_format)
                content_type = 'image/jpeg' if file_format == 'JPEG' else 'image/png'
                response = HttpResponse(buffer.getvalue(), content_type=content_type)
                response['Content-Disposition'] = 'attachment; filename="{}"'.format('upscale4_'+ uploaded_image.name) 
                return response
            else:
                if image.width > 900 or image.height > 900:
                   return render(request, 'upscale.html', {'error_message':'***Image size exceeds the maximum limit of 900 x 900.***'})
                upscaled_image = image.resize((image.width * 10, image.height * 10), resample=Image.BICUBIC) 
                buffer = io.BytesIO()
                file_format = 'JPEG' if upscaled_image.format == 'JPEG' else 'PNG'
                upscaled_image.save(buffer, format=file_format)
                content_type = 'image/jpeg' if file_format == 'JPEG' else 'image/png'
                response = HttpResponse(buffer.getvalue(), content_type=content_type)
                response['Content-Disposition'] = 'attachment; filename="{}"'.format('upscale8_'+ uploaded_image.name)
                if response == 0:
                   return HttpResponse('success')
                return response
             
                # return render(request, 'success.html', {'response': response})        
                    
    else:
        form = ImageUploadForm()
    
    return render(request, 'upscale.html', {'form': form})




