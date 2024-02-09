from .models import *
from django.http import JsonResponse
from django.shortcuts import render

#@login_required

# AMT AL-1
def BajaTensionListView1(request):
    title = 'Listado de planos de PCH001 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension1 = BajaTension.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH001.html', {'bajaTension1': bajaTension1, 'title': title})

def BajaTensionListView2(request):
    title = 'Listado de planos de PCH002 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension2 = BajaTension2.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH002.html', {'bajaTension2': bajaTension2, 'title': title})

def BajaTensionListView3(request):
    title = 'Listado de planos de PCH003 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension3 = BajaTension3.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH003.html', {'bajaTension3': bajaTension3, 'title': title})

def BajaTensionListView4(request):
    title = 'Listado de planos de PCH004 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension4 = BajaTension4.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH004.html', {'bajaTension4': bajaTension4, 'title': title})

def BajaTensionListView5(request):
    title = 'Listado de planos de PCH005 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension5 = BajaTension5.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH005.html', {'bajaTension5': bajaTension5, 'title': title})

def BajaTensionListView6(request):
    title = 'Listado de planos de PCH006 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension6 = BajaTension6.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH006.html', {'bajaTension6': bajaTension6, 'title': title})

def BajaTensionListView7(request):
    title = 'Listado de planos de PCH007 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension7 = BajaTension7.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH007.html', {'bajaTension7': bajaTension7, 'title': title})

def BajaTensionListView8(request):
    title = 'Listado de planos de PCH008 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension8 = BajaTension8.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH008.html', {'bajaTension8': bajaTension8, 'title': title})

def BajaTensionListView9(request):
    title = 'Listado de planos de PCH009 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension9 = BajaTension9.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH009.html', {'bajaTension9': bajaTension9, 'title': title})

def BajaTensionListView10(request):
    title = 'Listado de planos de PCH010 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension10 = BajaTension10.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH010.html', {'bajaTension10': bajaTension10, 'title': title})

def BajaTensionListView62(request):
    title = 'Listado de planos de PCH062 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension62 = BajaTension62.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH062.html', {'bajaTension62': bajaTension62, 'title': title})

def BajaTensionListView64(request):
    title = 'Listado de planos de PCH064 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension64 = BajaTension64.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH064.html', {'bajaTension64': bajaTension64, 'title': title})

def BajaTensionListView65(request):
    title = 'Listado de planos de PCH065 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension65 = BajaTension65.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH065.html', {'bajaTension65': bajaTension65, 'title': title})

def BajaTensionListView66(request):
    title = 'Listado de planos de PCH066 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension66 = BajaTension66.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH066.html', {'bajaTension66': bajaTension66, 'title': title})

def BajaTensionListView67(request):
    title = 'Listado de planos de PCH067 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension67 = BajaTension67.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH067.html', {'bajaTension67': bajaTension67, 'title': title})

def BajaTensionListView68(request):
    title = 'Listado de planos de PCH068 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension68 = BajaTension68.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH068.html', {'bajaTension68': bajaTension68, 'title': title})

def BajaTensionListView69(request):
    title = 'Listado de planos de PCH069 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension69 = BajaTension69.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH069.html', {'bajaTension69': bajaTension69, 'title': title})

def BajaTensionListView70(request):
    title = 'Listado de planos de PCH070 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension70 = BajaTension70.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH070.html', {'bajaTension70': bajaTension70, 'title': title})

def BajaTensionListView71(request):
    title = 'Listado de planos de PCH071 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension71 = BajaTension71.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH071.html', {'bajaTension71': bajaTension71, 'title': title})

def BajaTensionListView72(request):
    title = 'Listado de planos de PCH072 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension72 = BajaTension72.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH072.html', {'bajaTension72': bajaTension72, 'title': title})

def BajaTensionListView73(request):
    title = 'Listado de planos de PCH073 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension73 = BajaTension73.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH073.html', {'bajaTension73': bajaTension73, 'title': title})

def BajaTensionListView120(request):
    title = 'Listado de planos de PCH120 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension120 = BajaTension120.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH120.html', {'bajaTension120': bajaTension120, 'title': title})

def BajaTensionListView121(request):
    title = 'Listado de planos de PCH121 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension121 = BajaTension121.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH121.html', {'bajaTension121': bajaTension121, 'title': title})

def BajaTensionListView122(request):
    title = 'Listado de planos de PCH122 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension122 = BajaTension122.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH122.html', {'bajaTension122': bajaTension122, 'title': title})

def BajaTensionListView127(request):
    title = 'Listado de planos de PCH127 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension127 = BajaTension127.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH127.html', {'bajaTension127': bajaTension127, 'title': title})

def BajaTensionListView128(request):
    title = 'Listado de planos de PCH128 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension128 = BajaTension128.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH128.html', {'bajaTension128': bajaTension128, 'title': title})

def BajaTensionListView129(request):
    title = 'Listado de planos de PCH129 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension129 = BajaTension129.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH129.html', {'bajaTension129': bajaTension129, 'title': title})

def BajaTensionListView142(request):
    title = 'Listado de planos de PCH142 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension142 = BajaTension142.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH142.html', {'bajaTension142': bajaTension142, 'title': title})

def BajaTensionListView158(request):
    title = 'Listado de planos de PCH158 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension158 = BajaTension158.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH158.html', {'bajaTension158': bajaTension158, 'title': title})

def BajaTensionListView159(request):
    title = 'Listado de planos de PCH159 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension159 = BajaTension159.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL1/PCH159.html', {'bajaTension159': bajaTension159, 'title': title})

# AMT AL-2

def BajaTensionListView11(request):
    title = 'Listado de planos de PCH011 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension11 = BajaTension11.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH011.html', {'bajaTension11': bajaTension11, 'title': title})

def BajaTensionListView12(request):
    title = 'Listado de planos de PCH012 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension12 = BajaTension12.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH012.html', {'bajaTension12': bajaTension12, 'title': title})

def BajaTensionListView13(request):
    title = 'Listado de planos de PCH013 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension13 = BajaTension13.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH013.html', {'bajaTension13': bajaTension13, 'title': title})

def BajaTensionListView14(request):
    title = 'Listado de planos de PCH014 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension14 = BajaTension14.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH014.html', {'bajaTension14': bajaTension14, 'title': title})

def BajaTensionListView15(request):
    title = 'Listado de planos de PCH015 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension15 = BajaTension15.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH015.html', {'bajaTension15': bajaTension15, 'title': title})

def BajaTensionListView16(request):
    title = 'Listado de planos de PCH016 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension16 = BajaTension16.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH016.html', {'bajaTension16': bajaTension16, 'title': title})

def BajaTensionListView17(request):
    title = 'Listado de planos de PCH017 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension17 = BajaTension17.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH017.html', {'bajaTension17': bajaTension17, 'title': title})

def BajaTensionListView18(request):
    title = 'Listado de planos de PCH018 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension18 = BajaTension18.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH018.html', {'bajaTension18': bajaTension18, 'title': title})

def BajaTensionListView19(request):
    title = 'Listado de planos de PCH019 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension19 = BajaTension19.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH019.html', {'bajaTension19': bajaTension19, 'title': title})

def BajaTensionListView20(request):
    title = 'Listado de planos de PCH020 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension20 = BajaTension20.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH020.html', {'bajaTension20': bajaTension20, 'title': title})

def BajaTensionListView21(request):
    title = 'Listado de planos de PCH021 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension21 = BajaTension21.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH021.html', {'bajaTension21': bajaTension21, 'title': title})

def BajaTensionListView22(request):
    title = 'Listado de planos de PCH022 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension22 = BajaTension22.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH022.html', {'bajaTension22': bajaTension22, 'title': title})

def BajaTensionListView23(request):
    title = 'Listado de planos de PCH023 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension23 = BajaTension23.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH023.html', {'bajaTension23': bajaTension23, 'title': title})

def BajaTensionListView24(request):
    title = 'Listado de planos de PCH024 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension24 = BajaTension24.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH024.html', {'bajaTension24': bajaTension24, 'title': title})

def BajaTensionListView25(request):
    title = 'Listado de planos de PCH025 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension25 = BajaTension25.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH025.html', {'bajaTension25': bajaTension25, 'title': title})

def BajaTensionListView26(request):
    title = 'Listado de planos de PCH026 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension26 = BajaTension26.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH026.html', {'bajaTension26': bajaTension26, 'title': title})

def BajaTensionListView27(request):
    title = 'Listado de planos de PCH027 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension27 = BajaTension27.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH027.html', {'bajaTension27': bajaTension27, 'title': title})

def BajaTensionListView28(request):
    title = 'Listado de planos de PCH028 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension28 = BajaTension28.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH028.html', {'bajaTension28': bajaTension28, 'title': title})

def BajaTensionListView30(request):
    title = 'Listado de planos de PCH030 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension30 = BajaTension30.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH030.html', {'bajaTension30': bajaTension30, 'title': title})

def BajaTensionListView31(request):
    title = 'Listado de planos de PCH031 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension31 = BajaTension31.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH031.html', {'bajaTension31': bajaTension31, 'title': title})

def BajaTensionListView32(request):
    title = 'Listado de planos de PCH032 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension32 = BajaTension32.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH032.html', {'bajaTension32': bajaTension32, 'title': title})

def BajaTensionListView33(request):
    title = 'Listado de planos de PCH033 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension33 = BajaTension33.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH033.html', {'bajaTension33': bajaTension33, 'title': title})

def BajaTensionListView34(request):
    title = 'Listado de planos de PCH034 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension34 = BajaTension34.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH034.html', {'bajaTension34': bajaTension34, 'title': title})

def BajaTensionListView74(request):
    title = 'Listado de planos de PCH074 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension74 = BajaTension74.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH074.html', {'bajaTension74': bajaTension74, 'title': title})

def BajaTensionListView75(request):
    title = 'Listado de planos de PCH075 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension75 = BajaTension75.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH075.html', {'bajaTension75': bajaTension75, 'title': title})

def BajaTensionListView76(request):
    title = 'Listado de planos de PCH076 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension76 = BajaTension76.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH076.html', {'bajaTension76': bajaTension76, 'title': title})

def BajaTensionListView77(request):
    title = 'Listado de planos de PCH077 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension77 = BajaTension77.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH077.html', {'bajaTension77': bajaTension77, 'title': title})

def BajaTensionListView78(request):
    title = 'Listado de planos de PCH078 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension78 = BajaTension78.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH078.html', {'bajaTension78': bajaTension78, 'title': title})

def BajaTensionListView79(request):
    title = 'Listado de planos de PCH079 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension79 = BajaTension79.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH079.html', {'bajaTension79': bajaTension79, 'title': title})

def BajaTensionListView80(request):
    title = 'Listado de planos de PCH080 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension80 = BajaTension80.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH080.html', {'bajaTension80': bajaTension80, 'title': title})

def BajaTensionListView81(request):
    title = 'Listado de planos de PCH081 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension81 = BajaTension81.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH081.html', {'bajaTension81': bajaTension81, 'title': title})

def BajaTensionListView86(request):
    title = 'Listado de planos de PCH086 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension86 = BajaTension86.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH086.html', {'bajaTension86': bajaTension86, 'title': title})

def BajaTensionListView90(request):
    title = 'Listado de planos de PCH090 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension90 = BajaTension90.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH090.html', {'bajaTension90': bajaTension90, 'title': title})

def BajaTensionListView91(request):
    title = 'Listado de planos de PCH091 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension91 = BajaTension91.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH091.html', {'bajaTension91': bajaTension91, 'title': title})

def BajaTensionListView92(request):
    title = 'Listado de planos de PCH092 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension92 = BajaTension92.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH092.html', {'bajaTension92': bajaTension92, 'title': title})

def BajaTensionListView93(request):
    title = 'Listado de planos de PCH093 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension93 = BajaTension93.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH093.html', {'bajaTension93': bajaTension93, 'title': title})

def BajaTensionListView94(request):
    title = 'Listado de planos de PCH094 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension94 = BajaTension94.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH094.html', {'bajaTension94': bajaTension94, 'title': title})

def BajaTensionListView95(request):
    title = 'Listado de planos de PCH095 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension95 = BajaTension95.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH095.html', {'bajaTension95': bajaTension95, 'title': title})

def BajaTensionListView106(request):
    title = 'Listado de planos de PCH106 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension106 = BajaTension106.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH106.html', {'bajaTension106': bajaTension106, 'title': title})

def BajaTensionListView107(request):
    title = 'Listado de planos de PCH107 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension107 = BajaTension107.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH107.html', {'bajaTension107': bajaTension107, 'title': title})

def BajaTensionListView109(request):
    title = 'Listado de planos de PCH109 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension109 = BajaTension109.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH109.html', {'bajaTension109': bajaTension109, 'title': title})

def BajaTensionListView110(request):
    title = 'Listado de planos de PCH110 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension110 = BajaTension110.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH110.html', {'bajaTension110': bajaTension110, 'title': title})

def BajaTensionListView111(request):
    title = 'Listado de planos de PCH111 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension111 = BajaTension111.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH111.html', {'bajaTension111': bajaTension111, 'title': title})

def BajaTensionListView112(request):
    title = 'Listado de planos de PCH112 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension112 = BajaTension112.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH112.html', {'bajaTension112': bajaTension112, 'title': title})

def BajaTensionListView113(request):
    title = 'Listado de planos de PCH113 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension113 = BajaTension113.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH113.html', {'bajaTension113': bajaTension113, 'title': title})

def BajaTensionListView114(request):
    title = 'Listado de planos de PCH114 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension114 = BajaTension114.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH114.html', {'bajaTension114': bajaTension114, 'title': title})

def BajaTensionListView125(request):
    title = 'Listado de planos de PCH125 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension125 = BajaTension125.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH125.html', {'bajaTension125': bajaTension125, 'title': title})

def BajaTensionListView126(request):
    title = 'Listado de planos de PCH126 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension126 = BajaTension126.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH126.html', {'bajaTension126': bajaTension126, 'title': title})

def BajaTensionListView130(request):
    title = 'Listado de planos de PCH130 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension130 = BajaTension130.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH130.html', {'bajaTension130': bajaTension130, 'title': title})

def BajaTensionListView131(request):
    title = 'Listado de planos de PCH131 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension131 = BajaTension131.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'AL2/PCH131.html', {'bajaTension131': bajaTension131, 'title': title})

#SPP001

def BajaTensionListView41(request):
    title = 'Listado de planos de PCH041 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension41 = BajaTension41.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH041.html', {'bajaTension41': bajaTension41, 'title': title})

def BajaTensionListView42(request):
    title = 'Listado de planos de PCH042 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension42 = BajaTension42.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH042.html', {'bajaTension42': bajaTension42, 'title': title})

def BajaTensionListView43(request):
    title = 'Listado de planos de PCH043 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension43 = BajaTension43.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH043.html', {'bajaTension43': bajaTension43, 'title': title})

def BajaTensionListView46(request):
    title = 'Listado de planos de PCH046 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension46 = BajaTension46.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH046.html', {'bajaTension46': bajaTension46, 'title': title})

def BajaTensionListView47(request):
    title = 'Listado de planos de PCH047 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension47 = BajaTension47.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH047.html', {'bajaTension47': bajaTension47, 'title': title})

def BajaTensionListView48(request):
    title = 'Listado de planos de PCH048 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension48 = BajaTension48.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH048.html', {'bajaTension48': bajaTension48, 'title': title})

def BajaTensionListView50(request):
    title = 'Listado de planos de PCH050 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension50 = BajaTension50.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH050.html', {'bajaTension50': bajaTension50, 'title': title})

def BajaTensionListView51(request):
    title = 'Listado de planos de PCH051 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension51 = BajaTension51.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH051.html', {'bajaTension51': bajaTension51, 'title': title})

def BajaTensionListView52(request):
    title = 'Listado de planos de PCH052 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension52 = BajaTension52.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH052.html', {'bajaTension52': bajaTension52, 'title': title})

def BajaTensionListView53(request):
    title = 'Listado de planos de PCH053 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension53 = BajaTension53.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH053.html', {'bajaTension53': bajaTension53, 'title': title})

def BajaTensionListView54(request):
    title = 'Listado de planos de PCH054 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension54 = BajaTension54.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH054.html', {'bajaTension54': bajaTension54, 'title': title})

def BajaTensionListView55(request):
    title = 'Listado de planos de PCH055 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension55 = BajaTension55.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH055.html', {'bajaTension55': bajaTension55, 'title': title})

def BajaTensionListView56(request):
    title = 'Listado de planos de PCH056 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension56 = BajaTension56.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH056.html', {'bajaTension56': bajaTension56, 'title': title})

def BajaTensionListView57(request):
    title = 'Listado de planos de PCH057 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension57 = BajaTension57.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH057.html', {'bajaTension57': bajaTension57, 'title': title})

def BajaTensionListView58(request):
    title = 'Listado de planos de PCH058 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension58 = BajaTension58.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH058.html', {'bajaTension58': bajaTension58, 'title': title})

def BajaTensionListView59(request):
    title = 'Listado de planos de PCH059 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension59 = BajaTension59.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH059.html', {'bajaTension59': bajaTension59, 'title': title})

def BajaTensionListView60(request):
    title = 'Listado de planos de PCH060 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension60 = BajaTension60.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH060.html', {'bajaTension60': bajaTension60, 'title': title})

def BajaTensionListView61(request):
    title = 'Listado de planos de PCH061 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension61 = BajaTension61.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH061.html', {'bajaTension61': bajaTension61, 'title': title})

def BajaTensionListView89(request):
    title = 'Listado de planos de PCH089 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension89 = BajaTension89.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH089.html', {'bajaTension89': bajaTension89, 'title': title})

def BajaTensionListView96(request):
    title = 'Listado de planos de PCH096 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension96 = BajaTension96.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH096.html', {'bajaTension96': bajaTension96, 'title': title})

def BajaTensionListView97(request):
    title = 'Listado de planos de PCH097 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension97 = BajaTension97.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH097.html', {'bajaTension97': bajaTension97, 'title': title})

def BajaTensionListView98(request):
    title = 'Listado de planos de PCH098 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension98 = BajaTension98.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH098.html', {'bajaTension98': bajaTension98, 'title': title})

def BajaTensionListView99(request):
    title = 'Listado de planos de PCH099 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension99 = BajaTension99.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH099.html', {'bajaTension99': bajaTension99, 'title': title})

def BajaTensionListView100(request):
    title = 'Listado de planos de PCH100 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension100 = BajaTension100.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH100.html', {'bajaTension100': bajaTension100, 'title': title})

def BajaTensionListView101(request):
    title = 'Listado de planos de PCH101 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension101 = BajaTension101.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH101.html', {'bajaTension101': bajaTension101, 'title': title})

def BajaTensionListView102(request):
    title = 'Listado de planos de PCH102 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension102 = BajaTension102.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH102.html', {'bajaTension102': bajaTension102, 'title': title})

def BajaTensionListView153(request):
    title = 'Listado de planos de PCH153 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension153 = BajaTension153.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH153.html', {'bajaTension153': bajaTension153, 'title': title})

def BajaTensionListView157(request):
    title = 'Listado de planos de PCH157 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension157 = BajaTension157.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SPP001/PCH157.html', {'bajaTension157': bajaTension157, 'title': title})

#SSJ001

def BajaTensionListView36(request):
    title = 'Listado de planos de PCH036 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension36 = BajaTension36.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SSJ001/PCH036.html', {'bajaTension36': bajaTension36, 'title': title})

def BajaTensionListView37(request):
    title = 'Listado de planos de PCH037 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension37 = BajaTension37.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SSJ001/PCH037.html', {'bajaTension37': bajaTension37, 'title': title})

def BajaTensionListView38(request):
    title = 'Listado de planos de PCH038 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension38 = BajaTension38.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SSJ001/PCH038.html', {'bajaTension38': bajaTension38, 'title': title})

def BajaTensionListView39(request):
    title = 'Listado de planos de PCH039 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension39 = BajaTension39.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SSJ001/PCH039.html', {'bajaTension39': bajaTension39, 'title': title})

def BajaTensionListView40(request):
    title = 'Listado de planos de PCH040 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension40 = BajaTension40.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SSJ001/PCH040.html', {'bajaTension40': bajaTension40, 'title': title})

def BajaTensionListView63(request):
    title = 'Listado de planos de PCH063 en Baja Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    bajaTension63 = BajaTension63.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'SSJ001/PCH063.html', {'bajaTension63': bajaTension63, 'title': title})
