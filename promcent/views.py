from prominfo.models import PromCentInfo
from django.shortcuts import render
from django.db import models
# Create your views here.
from sklepy.models import BazyRach
from promcent.models import Nag_rach, Poz_rach
from promcent.serializers import PromCentSerializer, SzczPromCentSerializer
from promocje.serializers import SzczPromSerializer


from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from datetime import date


@csrf_exempt
@api_view(['GET'])
def promcent_oddo(request, data_od, data_do):
    if request.method == 'GET':
        promcent_li = Nag_rach.objects.using('centrala').select_related('NagRach').filter(
            do_dnia__gt=data_od, od_dnia__lte=data_do)  # .filter(Q(NagRach__status__isnull=True) | Q(NagRach__status=0))

    lista_promcent = []

    for promc in promcent_li:
        try:
            lista_promcent.append({
                'status': promc.status,
                'typ_rach': promc.typ_rach,
                'id_prom': promc.id_nagrach,
                'data_b_prom': promc.od_dnia,
                'data_e_prom': promc.do_dnia,
                'data_d_prom': promc.data_operacji,
                'uwagi_prom': promc.uwagi,
                'nr_prom': promc.numer_rach,
                'stat_prom': promc.stat_prom,
                'datazak_od': promc.NagRach.datazak_od,
                'datazak_do': promc.NagRach.datazak_do,
                'uwagi': promc.NagRach.uwagi,
                'id_uwagi': promc.NagRach.id,
            })

        except ObjectDoesNotExist:
            lista_promcent.append({
                'status': promc.status,
                'typ_rach': promc.typ_rach,
                'id_prom': promc.id_nagrach,
                'data_b_prom': promc.od_dnia,
                'data_e_prom': promc.do_dnia,
                'data_d_prom': promc.data_operacji,
                'uwagi_prom': promc.uwagi,
                'nr_prom': promc.numer_rach,
                'stat_prom': promc.stat_prom,
                'datazak_od': None,
                'datazak_do': None,
                'uwagi': None,
                'id_uwagi': None,
            })

    promocent_serializer = PromCentSerializer(lista_promcent, many=True)
    odpowiedz = {
        'wiadomosc': "Sukces - Pobrano dane z promocje centralne",
        'promocje': promocent_serializer.data,
        'error':  ""
    }
    return JsonResponse(odpowiedz, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def promcent_dzis(request):
    dzisiaj = date.today()
    if request.method == 'GET':
        promcent_li = Nag_rach.objects.using('centrala').select_related('NagRach').filter(
            do_dnia__gt=dzisiaj, od_dnia__lte=dzisiaj)  # .filter(Q(NagRach__status__isnull=True) | Q(NagRach__status=0))

    lista_promcent = []

    for promc in promcent_li:
        try:
            lista_promcent.append({
                # 'status': promc.NagRach.status,
                'status': promc.status,
                'typ_rach': promc.typ_rach,
                'id_prom': promc.id_nagrach,
                'data_b_prom': promc.od_dnia,
                'data_e_prom': promc.do_dnia,
                'data_d_prom': promc.data_operacji,
                'uwagi_prom': promc.uwagi,
                'nr_prom': promc.numer_rach,
                'stat_prom': promc.stat_prom,
                'datazak_od': promc.NagRach.datazak_od,
                'datazak_do': promc.NagRach.datazak_do,
                'uwagi': promc.NagRach.uwagi,
                'id_uwagi': promc.NagRach.id,
            })

        except ObjectDoesNotExist:
            lista_promcent.append({
                # 'status': None,
                'status': promc.status,
                'typ_rach': promc.typ_rach,
                'id_prom': promc.id_nagrach,
                'data_b_prom': promc.od_dnia,
                'data_e_prom': promc.do_dnia,
                'data_d_prom': promc.data_operacji,
                'uwagi_prom': promc.uwagi,
                'nr_prom': promc.numer_rach,
                'stat_prom': promc.stat_prom,
                'datazak_od': None,
                'datazak_do': None,
                'uwagi': None,
                'id_uwagi': None,
            })

    promocent_serializer = PromCentSerializer(lista_promcent, many=True)
    odpowiedz = {
        'wiadomosc': "Sukces - Pobrano dane z promocje centralne",
        'promocje': promocent_serializer.data,
        'error':  ""
    }
    return JsonResponse(odpowiedz, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def promcent_detail(request, nrprom):
    try:
        promcent = Poz_rach.objects.using('centrala'
                                          ).select_related('id_tow', 'id_nagrach').filter(id_nagrach__numer_rach=nrprom)
    except Poz_rach.DoesNotExist:
        exceptionError = {
            'wiadomosc': "Nie znaleziono promocja 0 nr_prom =%s" % nrprom,
            'promocje': "[]",
            'error': "Nie znaleziono - kod 404 error"
        }
        return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        pozycje_prom = []
        for pozp in promcent:
            pozycje_prom.append({
                'status': pozp.status,
                # 'id_pprom': pozp.id_pprom,
                # 'id_prom': pozp.id_prom,
                'id_tow': pozp.id_tow.id_tow,
                'nazwa_tow': pozp.id_tow.nazwa_tow,
                'cena_d_tow': pozp.id_tow.cena_d_tow,
                'bar_kod_tow': pozp.id_tow.bar_kod_tow,
                'cena_d_old': pozp.stara_cena,
                'cena_d_prom': pozp.nowa_cena,
                # 'ilosc_prom': pozp.ilosc_prom,
                # 'obrot_prom': pozp.obrot_prom,
                # 'id_knt': pozp.id_knt,
                # 'data_b_prom': pozp.data_e_prom,
                # 'data_e_prom': pozp.data_e_prom,
                # 'stat_prom': pozp.stat_prom,
                'cena_zakupu': pozp.cena_zakupu,
                # 'ilosc_prog': pozp.ilosc_prog
            })

        #pozprom_serializer = PozPromSerializer(promocja, many=True)
        pozprom_serializer = SzczPromCentSerializer(pozycje_prom, many=True)
        odpowiedz = {
            'wiadomosc': "Odczyt promocje o id = %s" % nrprom,
            'promocje': pozprom_serializer.data,
            'error': ""
        }
        return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
