from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm': '2406405720',  # Ubah sesuai dengan npm kamu
        'name': 'Daffa Abhinaya Avesinanoor',  # U
        'class': 'PBP C'  # Ubah sesuai dengan kelas kamu
    }
    return render(request, 'main.html', context)
