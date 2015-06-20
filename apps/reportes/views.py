from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Indenter

from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.datetime_safe import datetime

from skp import settings
from apps.proyectos.models import Proyecto
from apps.userstory.models import UserStory
from apps.sprint.models import Sprint


def reportes(request):
    return render_to_response('reportes/reportes.html',context_instance=RequestContext(request))

def llamada_reporte_uno(request):
    reporte_uno()
    opcion="uno"
    return render_to_response('reportes/reporte_exito.html',{'opcion':opcion},context_instance=RequestContext(request))
    
def llamada_reporte_dos(request):
    reporte_dos()
    opcion="dos"
    return render_to_response('reportes/reporte_exito.html',{'opcion':opcion},context_instance=RequestContext(request))
    
def llamada_reporte_tres(request):
    reporte_tres()
    opcion="tres"
    return render_to_response('reportes/reporte_exito.html',{'opcion':opcion},context_instance=RequestContext(request))
    
def llamada_reporte_cuatro(request):
    reporte_cuatro()
    opcion="cuatro"
    return render_to_response('reportes/reporte_exito.html',{'opcion':opcion},context_instance=RequestContext(request))

def llamada_reporte_cinco(request):
    reporte_cinco()
    opcion="cinco"
    return render_to_response('reportes/reporte_exito.html',{'opcion':opcion},context_instance=RequestContext(request))
    
def llamada_reporte_seis(request):
    proyectos = Proyecto.objects.all()
    sprints = Sprint.objects.all()
    return render_to_response('reportes/reporte_seis.html',{'proyectos':proyectos, 'sprints':sprints},
        context_instance=RequestContext(request))
    
def vista_reporte_seis(request, idSprint):
    opcion="seis"
    reporte_seis(idSprint)
    return render_to_response('reportes/reporte_exito.html',{'opcion':opcion},context_instance=RequestContext(request))


def ver_reporte_uno(request):
   
    a=file(reporte_uno())
    return StreamingHttpResponse(a,content_type='application/pdf')


def ver_reporte_dos(request):

    a=file(reporte_dos())
    return StreamingHttpResponse(a,content_type='application/pdf')


def ver_reporte_tres(request):
   
    a=file(reporte_tres())
    return StreamingHttpResponse(a,content_type='application/pdf')

def ver_reporte_cuatro(request):
   
    a=file(reporte_cuatro())
    return StreamingHttpResponse(a,content_type='application/pdf')

def ver_reporte_cinco(request):
   
    a=file(reporte_cinco())
    return StreamingHttpResponse(a,content_type='application/pdf')


def reporte_uno():
   
    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/log/reporte_uno.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)


    Story=[]
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubsubsubItems',fontName='Helvetica',fontSize=8,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubsubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=14,spaceAfter=10, spaceBefore=10))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
    contador_act=1
    titulo="<b>Proyectos del Sistema<br/>"
    Story.append(Paragraph(titulo,styles['Principal']))
    Story.append(Spacer(1, 12))
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))

    proyectos = Proyecto.objects.all()    
    for proyecto in proyectos:
        text ="<strong>Nombre: </strong>" + proyecto.Nombre +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        text ="<strong>Descripcion: </strong>" + proyecto.Descripcion +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        dateFormat = proyecto.Fecha_inicio.strftime("%d-%m-%Y")
        text ="<strong>Fecha de creacion: </strong>" + str(dateFormat) +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        dateFormat = proyecto.Fecha_finalizacion.strftime("%d-%m-%Y")
        text ="<strong>Fecha de finalizacion: </strong>" + str(dateFormat) +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        text ="<strong>Scrum Master: </strong>" + proyecto.Scrum_Master.username +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        text ="<strong>User Storys: </strong>""<br>"
        Story.append(Paragraph(text, styles["Items"]))
        
        userstorys = UserStory.objects.filter(Proyecto_asignado=proyecto)
        c=0
        for us in userstorys:
            if us.Estado!='Terminado':
                c=c+1
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- " + us.Nombre +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))           
        text ="<strong>Cantidad de trabajos en curso: </strong>" + str(c) +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        Story.append(Indenter(25))
        text ="__________________________________________________________<br>"
        Story.append(Paragraph(text, styles["Items"]))
        Story.append(Spacer(1, 12))
        Story.append(Indenter(-25))
        contador_act+=1
    doc.build(Story)
    return str(settings.BASE_DIR)+"/log/reporte_uno.pdf"


def reporte_dos():
   
    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/log/reporte_dos.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)


    Story=[]
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubsubsubItems',fontName='Helvetica',fontSize=8,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubsubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=14,spaceAfter=10, spaceBefore=10))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
    
    
    titulo="<b>Usuarios del Sistema<br/>"
    Story.append(Paragraph(titulo,styles['Principal']))
    
    Story.append(Indenter(25))
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))

    usuarios = User.objects.all()
   
    for usuario in usuarios:

        userstorys = UserStory.objects.filter(Usuario_asignado__id=usuario.id)
        cont_pend=0
        cont_act=0
        cont_term=0
        
        text ="<strong>Nombre: </strong>" + usuario.username +"<br>"
        Story.append(Paragraph(text, styles["Items"]))

        for us in userstorys:
            if us.Estado=='Pendiente':
                cont_pend=cont_pend+1
                if cont_pend==1:
                    text ="<strong>Pendientes: </strong>""<br>"
                    Story.append(Paragraph(text, styles["Items"]))
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- " + us.Nombre +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
                
            elif us.Estado=='AsignadoSprint' or us.Estado=='AsignadoSprintActivo':
                cont_act=cont_act+1
                if cont_act==1:
                    text ="<strong>En curso: </strong>""<br>"
                    Story.append(Paragraph(text, styles["Items"]))
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- " + us.Nombre +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
                
            elif us.Estado=='Terminado':
                cont_term=cont_term+1
                if cont_term==1:
                    text ="<strong>Terminados: </strong>""<br>"
                    Story.append(Paragraph(text, styles["Items"])) 
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- " + us.Nombre +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
                     
    
        text ="<strong>Cantidad de trabajos en pendientes: </strong>" + str(cont_pend) +"<br>"
        Story.append(Paragraph(text, styles["Items"]))

        text ="<strong>Cantidad de trabajos en curso: </strong>" + str(cont_act) +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
    
        text ="<strong>Cantidad de trabajos terminados: </strong>" + str(cont_term) +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
    
        Story.append(Indenter(25))
        text ="__________________________________________________________<br>"
        Story.append(Paragraph(text, styles["Items"]))
        Story.append(Spacer(1, 12))
        Story.append(Indenter(-25))
    doc.build(Story)
    return str(settings.BASE_DIR)+"/log/reporte_dos.pdf"



def reporte_tres():
   
    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/log/reporte_tres.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)


    Story=[]
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubsubsubItems',fontName='Helvetica',fontSize=8,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubsubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=14,spaceAfter=10, spaceBefore=10))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
    contador_act=1
    titulo="<b>Proyectos del Sistema<br/>"
    Story.append(Paragraph(titulo,styles['Principal']))
    Story.append(Spacer(1, 12))
    
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))

    proyectos = Proyecto.objects.all()
    for proyecto in proyectos:
        text ="<strong>Nombre: </strong>" + proyecto.Nombre +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        text ="<strong>Descripcion: </strong>" + proyecto.Descripcion +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        dateFormat = proyecto.Fecha_inicio.strftime("%d-%m-%Y")
        text ="<strong>Fecha de creacion: </strong>" + str(dateFormat) +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        dateFormat = proyecto.Fecha_finalizacion.strftime("%d-%m-%Y")
        text ="<strong>Fecha de finalizacion: </strong>" + str(dateFormat) +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        text ="<strong>Scrum Master: </strong>" + proyecto.Scrum_Master.username +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        text ="<strong>Tablas: </strong>""<br>"
        Story.append(Paragraph(text, styles["Items"]))
        

        for tabla in proyecto.Tablas.all():
            text ="<strong>Nombre: </strong>"+tabla.Nombre+"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            
            for actividad in tabla.Actividades.all():
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- " + actividad.Nombre +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))           
        
        Story.append(Indenter(25))
        text ="__________________________________________________________<br>"
        Story.append(Paragraph(text, styles["Items"]))
        Story.append(Spacer(1, 12))
        Story.append(Indenter(-25))
    doc.build(Story)
    return str(settings.BASE_DIR)+"/log/reporte_tres.pdf"


def reporte_cuatro():
    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/log/reporte_cuatro.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)


    Story=[]
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubsubsubItems',fontName='Helvetica',fontSize=8,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubsubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=14,spaceAfter=10, spaceBefore=10))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
    contador_act=1
    titulo="<b>Proyectos del Sistema<br/>"
    Story.append(Paragraph(titulo,styles['Principal']))
    Story.append(Spacer(1, 12))
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))

    proyectos = Proyecto.objects.all()    
    for proyecto in proyectos:
        text ="<strong>Nombre: </strong>" + proyecto.Nombre +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        text ="<strong>Descripcion: </strong>" + proyecto.Descripcion +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        dateFormat = proyecto.Fecha_inicio.strftime("%d-%m-%Y")
        text ="<strong>Tiempo estimado: </strong>" + str(proyecto.Duracion)+" dias"+"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        text ="__________________________________________________________<br>"
        Story.append(Paragraph(text, styles["Items"]))
        
        
    doc.build(Story)
    return str(settings.BASE_DIR)+"/log/reporte_cuatro.pdf"


def reporte_cinco():
   
    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/log/reporte_cinco.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)


    Story=[]
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubsubsubItems',fontName='Helvetica',fontSize=8,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubsubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=14,spaceAfter=10, spaceBefore=10))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
    contador_act=1
    titulo="<b>Proyectos del Sistema<br/>"
    Story.append(Paragraph(titulo,styles['Principal']))
    Story.append(Spacer(1, 12))
    
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))

    proyectos = Proyecto.objects.all()
    for proyecto in proyectos:
        text ="<strong>Nombre: </strong>" + proyecto.Nombre +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        text ="<strong>Descripcion: </strong>" + proyecto.Descripcion +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        dateFormat = proyecto.Fecha_inicio.strftime("%d-%m-%Y")
        text ="<strong>Fecha de creacion: </strong>" + str(dateFormat) +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        dateFormat = proyecto.Fecha_finalizacion.strftime("%d-%m-%Y")
        text ="<strong>Fecha de finalizacion: </strong>" + str(dateFormat) +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        text ="<strong>Scrum Master: </strong>" + proyecto.Scrum_Master.username +"<br>"
        Story.append(Paragraph(text, styles["Items"]))
        text ="<strong>User Storys: </strong>""<br>"
        Story.append(Paragraph(text, styles["Items"]))
        

        userstorys = UserStory.objects.filter(Proyecto_asignado__id=proyecto.id).order_by('-Prioridad')
        

        for us in userstorys:
            text = ''
            Story.append(Indenter(42))
            Story.append(Spacer(1, 10))
            text ="- " + us.Nombre +" con prioridad: "+str(us.Prioridad)+"<br>"
            Story.append(Paragraph(text, styles["SubItems"]))
            Story.append(Indenter(-42))
            
            
        
        Story.append(Indenter(25))
        text ="__________________________________________________________<br>"
        Story.append(Paragraph(text, styles["Items"]))
        Story.append(Spacer(1, 12))
        Story.append(Indenter(-25))
    doc.build(Story)
    return str(settings.BASE_DIR)+"/log/reporte_cinco.pdf"




def reporte_seis(idSprint):
   
    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/log/reporte_seis.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)


    Story=[]
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubsubsubItems',fontName='Helvetica',fontSize=8,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubsubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=14,spaceAfter=10, spaceBefore=10))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
    

   
    titulo="<b>Sprint Backlog<br/>"
    Story.append(Paragraph(titulo,styles['Principal']))
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))
  

    sprint = Sprint.objects.get(pk=idSprint)

    text ="<strong>Nombre: </strong>" + sprint.Nombre +"<br>"
    Story.append(Paragraph(text, styles["Items"]))
    text ="<strong>Descripcion: </strong>" + sprint.Descripcion +"<br>"
    Story.append(Paragraph(text, styles["Items"]))
    text ="<strong>Creado por: </strong>" + str(sprint.Usuario_creador) +"<br>"
    Story.append(Paragraph(text, styles["Items"]))
    dateFormat = sprint.Fecha_creacion.strftime("%d-%m-%Y")
    text ="<strong>Fecha de creacion: </strong>" + str(dateFormat) +"<br>"
    Story.append(Paragraph(text, styles["Items"]))
    text ="<br>"
    Story.append(Paragraph(text, styles["Items"]))   
 

    dias = []
    dias.append('Nombre')

    cantidad = ( sprint.Fecha_finalizacion - sprint.Fecha_inicio ).days 

    for n in range( 0 , cantidad ):
        dias.append(str('Dia ' + `n + 1`) )

    dias.append('Restante')
    dias.append('Duracion')

    lista = []
    lista.append(dias)

    for us in sprint.UserStorys.all():
        registro = []

        registro.append(str(us.Nombre))
        
        
        for r in us.Registro:
            registro.append( str(r) )

        while( len(registro) - 1 < len(dias) - 3):
            registro.append(str(0))
        

        registro.append(str(us.Restante))
        registro.append(str(us.Duracion))

        lista.append(registro)

    registro = []
    registro.append( str(sprint.Nombre) )

    for r in sprint.Registro:
        registro.append( str(r) )

    while( len(registro) - 1 < len(dias) - 3):
            registro.append(str(0))  

    registro.append( str(sprint.Restante) )
    registro.append( str(sprint.Duracion) )

    lista.append( registro )

     

    #TODO: Get this line right instead of just copying it from the docs
    style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                           ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                           ('VALIGN',(0,0),(0,-1),'TOP'),
                           ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                           ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                           ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                           ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ])
     
    #Configure style and word wrap
    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    data2 = [[Paragraph(dato, s) for dato in l] for l in lista]
    t=Table(data2)
    t.setStyle(style)
    
    Story.append(t)

    Story.append(Indenter(25))
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))
    #Send the data and build the file
    
    doc.build(Story)
   
  