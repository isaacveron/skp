from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Indenter

from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext

from django.utils.datetime_safe import datetime
from skp import settings



def reporte(request):
    mensaje="reporte creado"
    reporte_usuarios()
    return render_to_response('userstory/operacion_userstory_exito.html',{'mensaje': mensaje},context_instance=RequestContext(request))
  
def reporte_usuarios():
    '''
    Funcion que genera el reporte de usuarios del sistema
    '''

    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/log/reporte_usuarios.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=30,bottomMargin=18)

    Story=[]
    #logo = str(settings.BASE_DIR)+"/static/icono.png"
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Principal',alignment=1,spaceAfter=20, fontSize=24))
    styles.add(ParagraphStyle(name='Justify',fontName='Courier-Oblique', alignment=TA_JUSTIFY, fontSize=14,spaceAfter=5))
    styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica', fontSize=18, alignment=0, spaceAfter=25, spaceBefore=15))
    styles.add(ParagraphStyle(name='Header',fontName='Helvetica',fontSize=20))
    styles.add(ParagraphStyle(name='SubItems',fontName='Helvetica',fontSize=10,spaceAfter=3))
    styles.add(ParagraphStyle(name='Items',fontName='Helvetica',fontSize=12,spaceAfter=10, spaceBefore=10))
    styles.add(ParagraphStyle(name='Subtitulos',fontSize=12,spaceAfter=3))
    styles.add(ParagraphStyle(name='Encabezado',fontSize=10,spaceAfter=10, left=1, bottom=1))
    #im = Image(logo, width=100,height=50)
    #Story.append(im)
    contador_act=1
    titulo="<b>Usuarios del Sistema<br/>"
    Story.append(Paragraph(titulo,styles['Principal']))


    Story.append(Spacer(1, 12))
    date=datetime.now()
    dateFormat = date.strftime("%d-%m-%Y")
    Story.append(Paragraph('Fecha: ' + str(dateFormat),styles['Subtitulos']))
    usuarios=User.objects.filter().order_by('is_active').reverse()
    usuarios_activos=User.objects.filter(is_active=True)
    cantidad_act=len(usuarios_activos)
    contador=-1
    titulo = Paragraph('<b>Usuarios Activos <\b>', styles['Titulo'])
    Story.append(Spacer(1, 12))
    Story.append(titulo)
    Story.append(Indenter(25))
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))
    for usuario in usuarios:
            contador+=1
            if contador==cantidad_act:
                titulo = Paragraph('<b>Usuarios Inactivos <\b>', styles['Titulo'])
                Story.append(Spacer(1, 12))
                Story.append(titulo)
                contador_act=1
            Story.append(Indenter(25))
            text="<strong>"+str(contador_act)+".</strong>"
            Story.append(Paragraph(text, styles["Subtitulos"]))
            text ="<strong>Usuario: </strong>" + usuario.username +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Nombre: </strong>" + usuario.first_name + " "+ usuario.last_name +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>E-mail: </strong>" + usuario.email +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            dateFormat = usuario.date_joined.strftime("%d-%m-%Y %H:%M:%S")
            text ="<strong>Fecha de creacion: </strong>" + str(dateFormat) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            dateFormat = usuario.last_login.strftime("%d-%m-%Y %H:%M:%S")
            text ="<strong>Ultimo acceso: </strong>" + str(dateFormat) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Roles: </strong> <br>"
            Story.append(Paragraph(text, styles["Items"]))
            Story.append(Indenter(-25))
            roles=Group.objects.filter(user__id=usuario.id)
            for rol in roles:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- " + rol.name +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
            Story.append(Indenter(25))
            text ="__________________________________________________________<br>"
            Story.append(Paragraph(text, styles["Items"]))
            Story.append(Spacer(1, 12))
            Story.append(Indenter(-25))
            contador_act+=1
    doc.build(Story)
    return str(settings.BASE_DIR)+"/log/reporte_usuarios.pdf"

def descargar_reporteUsuarios(request):
    a=file(reporte_usuarios())

    return StreamingHttpResponse(a,content_type='application/pdf')


def reporte_proyectos():
   
    doc = SimpleDocTemplate(str(settings.BASE_DIR)+"/log/reporte_proyectos.pdf",pagesize=letter,
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
    date=datetime.now()
    dateFormat = date.strftime("%d-%m-%Y")
    Story.append(Paragraph('Fecha: ' + str(dateFormat),styles['Subtitulos']))
    proyectos_fin=Proyecto.objects.filter(estado='Terminado')
    proyectos_pen=Proyecto.objects.filter(estado='Pendiente')
    proyectos_anu=Proyecto.objects.filter(estado='Camcelado')
    proyectos=[]
    for p in proyectos_pen:
        proyectos.append(p)
    for p in proyectos_fin:
        proyectos.append(p)
    for p in proyectos_anu:
        proyectos.append(p)
    cantidad_pen=len(proyectos_pen)
    cantidad_act=len(proyectos_activos)
    cantidad_fin=len(proyectos_fin)
    contador1=0
    contador2=0
    contador3=0
    contador=0
    titulo = Paragraph('<b>Proyectos Pendientes <\b>', styles['Titulo'])
    Story.append(Spacer(1, 12))
    Story.append(titulo)
    Story.append(Indenter(25))
    text ="__________________________________________________________<br>"
    Story.append(Paragraph(text, styles["Items"]))
    Story.append(Spacer(1, 12))
    Story.append(Indenter(-25))
    for proyecto in proyectos:
            contador+=1
            if proyecto.estado=='ACT' and contador1==0:
                titulo = Paragraph('<b>Proyectos Activos <\b>', styles['Titulo'])
                Story.append(Spacer(1, 12))
                Story.append(titulo)
                contador1=1
                contador=1
            if proyecto.estado=='FIN' and contador2==0:
                titulo = Paragraph('<b>Proyectos Finalizados <\b>', styles['Titulo'])
                Story.append(Spacer(1, 12))
                Story.append(titulo)
                contador2=1
                contador=1
            if proyecto.estado=='ANU' and contador3==0:
                titulo = Paragraph('<b>Proyectos Anulados <\b>', styles['Titulo'])
                Story.append(Spacer(1, 12))
                Story.append(titulo)
                contador3=1
                contador=1

            Story.append(Indenter(25))
            text="<strong>"+str(contador)+".</strong>"
            Story.append(Paragraph(text, styles["Subtitulos"]))
            text ="<strong>Nombre: </strong>" + proyecto.nombre +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Descripcion: </strong>" + proyecto.descripcion +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            dateFormat = proyecto.fecha_ini.strftime("%d-%m-%Y")
            text ="<strong>Fecha de creacion: </strong>" + str(dateFormat) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            dateFormat = proyecto.fecha_fin.strftime("%d-%m-%Y")
            text ="<strong>Fecha de finalizacion: </strong>" + str(dateFormat) +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Observaciones: </strong>" + proyecto.observaciones +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            text ="<strong>Lider: </strong>" + proyecto.lider.username +"<br>"
            Story.append(Paragraph(text, styles["Items"]))
            """
            text ="<strong>Fases: </strong> <br>"
            Story.append(Paragraph(text, styles["SubItems"]))
            Story.append(Indenter(-25))
            fases=Fase.objects.filter(proyecto=proyecto)
            for fase in fases:
                text = ''
                Story.append(Indenter(42))
                Story.append(Spacer(1, 10))
                text ="- " + fase.nombre +"<br>"
                Story.append(Paragraph(text, styles["SubItems"]))
                Story.append(Indenter(-42))
                tipoi=TipoItem.objects.filter(fase=fase)
                Story.append(Indenter(50))
                text ="<strong>Tipos de Item: </strong> <br>"
                Story.append(Paragraph(text, styles["SubsubItems"]))
                Story.append(Indenter(-50))
                for ti in tipoi:
                    text = ''
                    Story.append(Indenter(50))

                    text ="- " + ti.nombre +"<br>"
                    Story.append(Paragraph(text, styles["SubsubItems"]))
                    Story.append(Indenter(-50))
                    atributos=Atributo.objects.filter(tipoItem__id=ti.id)
                    Story.append(Indenter(60))
                    text ="<strong>Tipos de Atributo: </strong> <br>"
                    Story.append(Paragraph(text, styles["SubsubsubItems"]))
                    Story.append(Indenter(-60))
                    for atributo in atributos:
                        text = ''
                        Story.append(Indenter(70))
                        text ="- " + atributo.nombre + ", Tipo "+ atributo.tipo + "<br>"
                        Story.append(Paragraph(text, styles["SubsubsubItems"]))
                        Story.append(Indenter(-70))
                        """


            Story.append(Indenter(25))
            text ="__________________________________________________________<br>"
            Story.append(Paragraph(text, styles["Items"]))
            Story.append(Spacer(1, 12))
            Story.append(Indenter(-25))
            contador_act+=1
    doc.build(Story)
    return str(settings.BASE_DIR)+"/log/reporte_proyectos.pdf"


def descargar_reporteProyectos(request):
    '''
    Vista para descargar el reporte de lineas base de un proyecto especifico
    '''
    if request.user.is_superuser!=True:
        return HttpResponseRedirect('/denegado')
    a=file(reporte_proyectos())

    return StreamingHttpResponse(a,content_type='application/pdf')

