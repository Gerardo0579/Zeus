#######################################################
# 
# ContenidosAgregados.py
# Python implementation of the Class ContenidosAgregados
# Generated by Enterprise Architect
# Created on:      07-sep.-2016 11:09:48 p. m.
# Original author: Luis Fernando Gomez Alejandre
# 
#######################################################
from Dominio.ContenidosAgregadosInformativos import ContenidosAgregadosInformativos
from Dominio.ContenidosAgregadosGenerales import ContenidosAgregadosGenerales

class ContenidosAgregados:
    __fechaInicio = " "
    __nombreCompletoDocente = " "
    __numeroSecuencia = 0
    __numeroSesiones = 0
    __periodoEscolar = " "
    m_ContenidosAgregadosGenerales= ContenidosAgregadosGenerales()

    m_ContenidosAgregadosInformativos= ContenidosAgregadosInformativos()

    def getContenidosGenerales():
        pass

    def getContenidosInformativos():
        pass

    def getFechaInicio():
        pass

    def getNombreCompletoDocente():
        pass

    def getNumeroSecuencia():
        pass

    def getNumeroSesiones():
        pass

    def getPeriodoEscolar():
        pass

    def setContenidosAgregadosCierre(aprendizaje, ensenianza):
        pass

    def setContenidosAgregadosDesarrollo(aprendizaje, ensenianza):
        pass

    def setContenidosAgregadosInicio(aprendizaje, ensenianza):
        pass

    def setContenidosInformativos(listaAsignaturasRelacionadas, listaFuentesInformacion, listaObservaciones, propositoSecuencia, recursosMateriales):
        pass

    def setFechaInicio(fecha):
        pass

    def setNombreCompletoDocente(nombre):
        pass

    def setNumeroSecuencia(numero):
        pass

    def setNumeroSesiones(numeroSesiones):
        pass

    def setPeriodoEscolar(periodo):
        pass