from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from datetime import datetime, timedelta
import math
from django.db.models import Q

from apps.usuario.models import User
from apps.sprint.models import Sprint
from apps.proyectos.models import Proyecto
from apps.userstory.models import UserStory



def ver_burdownchart(request, idSprint):

    sprint = Sprint.objects.get(pk=idSprint)

    if( int(sprint.Duracion%8) == 0):
    	duracion = sprint.Duracion // 8
    else:
    	duracion = (sprint.Duracion // 8) + 1

    dias = ['inicio']
    ideal = [sprint.Duracion]
    

    for i in range(0,duracion):
    	dias.append( 'Dia ' + `i+1` )
    
    i=1
    for d in dias:
    	if( sprint.Duracion - (i*8) >= 0 ):
    		ideal.append( sprint.Duracion - (i*8) )
    	else:
    		ideal.append( 0 )
    	i = i + 1

    puntos = [sprint.Duracion]
    suma = 0
    for i in sprint.Registro:
    	suma += i
    	puntos.append( sprint.Duracion - suma )


    dias_s = ""
    puntos_s = ""
    ideal_s = ""

    for i in puntos:
    	if( puntos_s == "" ):
    		puntos_s = `i` + ','
    	else:
    		puntos_s += `i` + ','

    for i in range( 0 , len( dias ) ):

        if(dias_s == ""):
            dias_s = dias[i] + ','
            ideal_s = `ideal[i]` + ','

        else:
            dias_s += dias[i] + ','
            ideal_s += `ideal[i]` + ','

    puntos_s = puntos_s.rstrip(',')
    dias_s = dias_s.rstrip(',')
    ideal_s = ideal_s.rstrip(',')

    return render_to_response('graficos/index.html', {'dias':dias_s, 'puntos':puntos_s, 'ideal':ideal_s},context_instance=RequestContext(request))

def ver_burdownchart_proyecto(request, idProyecto):

    proyecto = Proyecto.objects.get( pk=idProyecto )

    dias = ['inicio']
    ideal = [proyecto.Duracion]
    
    duracion = (proyecto.Fecha_finalizacion - proyecto.Fecha_inicio).days
    for i in range(0,duracion):
    	dias.append( 'Dia ' + `i+1` )
    
    i=1

    for d in dias:
    	if( proyecto.Duracion - (i*8) >= 0 ):
    		ideal.append( proyecto.Duracion - (i*8) )
    	else:
    		ideal.append( 0 )
    	i = i + 1

    puntos = [proyecto.Duracion]
    suma = 0
    for i in proyecto.Registro:
    	suma += i
    	puntos.append( proyecto.Duracion - suma )


    dias_s = ""
    puntos_s = ""
    ideal_s = ""

    for i in puntos:
    	if( puntos_s == "" ):
    		puntos_s = `i` + ','
    	else:
    		puntos_s += `i` + ','

    for i in range( 0 , len( dias ) ):

        if(dias_s == ""):
            dias_s = dias[i] + ','
            ideal_s = `ideal[i]` + ','

        else:
            dias_s += dias[i] + ','
            ideal_s += `ideal[i]` + ','

    puntos_s = puntos_s.rstrip(',')
    dias_s = dias_s.rstrip(',')
    ideal_s = ideal_s.rstrip(',')

    return render_to_response('graficos/index.html', {'dias':dias_s, 'puntos':puntos_s, 'ideal':ideal_s},context_instance=RequestContext(request))

def ver_backlog(request,idSprint):

    sprint = Sprint.objects.get(pk=idSprint)
    proyecto = sprint.Proyecto_asignado
    usuario_actor = request.user

    dias = []
    dias.append('Nombre')

    cantidad = ( sprint.Fecha_finalizacion - sprint.Fecha_inicio ).days 

    for n in range( 0 , cantidad ):
    	dias.append('Dia ' + `n + 1` )

    dias.append('Restante')
    dias.append('Duracion')

    lista = []
    lista.append(dias)

    for us in sprint.UserStorys.all():
    	registro = []

    	registro.append(us.Nombre)
    	
    	
    	for r in us.Registro:
    		registro.append( r )

    	while( len(registro) - 1 < len(dias) - 3):
    		registro.append(0)
    	

    	registro.append(us.Restante)
    	registro.append(us.Duracion)

    	lista.append(registro)

    registro = []
    registro.append( sprint.Nombre )

    for r in sprint.Registro:
    	registro.append( r )

    while( len(registro) - 1 < len(dias) - 3):
    		registro.append(0)	

    registro.append( sprint.Restante )
    registro.append( sprint.Duracion )

    lista.append( registro )
    print lista

    return render_to_response('sprint/sprint_backlog.html',{'dias':dias,'sprint':sprint,'lista':lista, 'usuario_actor': usuario_actor}, 
                            context_instance=RequestContext(request))


