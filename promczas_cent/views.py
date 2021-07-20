from django.shortcuts import render

# Create your views here.
from promczas_info.models import PromCzasInfo
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from promczas_cent.models import PromocjaCzas, PromocjaCzas_pozycja
from promczas_info.models import PromCzasInfo,PromCzasInfoOnly
from promczas_cent.serializers import PromocjaCzasSerializer, PromocjaCzasPozycjaSerializer
from rest_framework import status


@csrf_exempt
@api_view(['GET'])
def promczascent_oddo(request, data_od, data_do):
    try:
        promczas_li = PromocjaCzas.objects.using('centrala').select_related(
            'PromCzas').filter(data_p_do__gt=data_od, data_p_od__lte=data_do)

        #promczas_li = PromocjaCzas.objects.using('centrala').filter(data_p_do__gt=data_od, data_p_od__lte=data_do)

        lista_promczas = []
        for pczas in promczas_li:
            try:
                lista_promczas.append({
                    'status': pczas.status,
                    'id_pczas': pczas.id_pczas,
                    'godz_prom': pczas.godz_prom,
                    'dt_prom': pczas.dt_prom,
                    'mr_prom': pczas.mr_prom,
                    'data_p_od': pczas.data_p_od,
                    'data_p_do': pczas.data_p_do,
                    'nr_prom': pczas.nr_prom,
                    'nazwa_prom': pczas.nazwa_prom,
                    'nr_rabat_k': pczas.nr_rabat_k,
                    'typ_prom': pczas.typ_prom,
                    'uwagi_prom': pczas.uwagi_prom,
                    'data_mod': pczas.data_mod,
                    'user_id': pczas.user_id,
                    'kwota_prog': pczas.kwota_prog,
                    'max_prom': pczas.max_prom,
                    'datazak_od': pczas.PromCzas.datazak_od,
                    'datazak_do': pczas.PromCzas.datazak_do,
                    'uwagi': pczas.PromCzas.uwagi
                })
            except ObjectDoesNotExist:
                lista_promczas.append({
                    'status': pczas.status,
                    'id_pczas': pczas.id_pczas,
                    'godz_prom': pczas.godz_prom,
                    'dt_prom': pczas.dt_prom,
                    'mr_prom': pczas.mr_prom,
                    'data_p_od': pczas.data_p_od,
                    'data_p_do': pczas.data_p_do,
                    'nr_prom': pczas.nr_prom,
                    'nazwa_prom': pczas.nazwa_prom,
                    'nr_rabat_k': pczas.nr_rabat_k,
                    'typ_prom': pczas.typ_prom,
                    'uwagi_prom': pczas.uwagi_prom,
                    'data_mod': pczas.data_mod,
                    'user_id': pczas.user_id,
                    'kwota_prog': pczas.kwota_prog,
                    'max_prom': pczas.max_prom,
                    'datazak_od': None,
                    'datazak_do': None,
                    'uwagi': None
                })

        promczas_serializer = PromocjaCzasSerializer(lista_promczas, many=True)
        odpowiedz = {
            'wiadomosc': "Sukces - Pobrano dane z promocje czasowe",
            'promocje': promczas_serializer.data,
            'error':  ""
        }
        return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
    except :
        error = {
            'wiadomosc': "Bład -> nie mogę odczytać promocje_czasowe",
            'promczas_cent': "[]",
            'error': "error"
        }
        return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['GET'])
def promczascent_detail(request, nrprom):
    try:
        promczas = PromocjaCzas_pozycja.objects.using('centrala').select_related('id_tow', 'id_prom_czas').filter(id_prom_czas__nr_prom=nrprom)
    except PromocjaCzas_pozycja.DoesNotExist:
        exceptionError = {
            'wiadomosc': "Nie znaleziono promocja czas o nr_prom =%s" % nrprom,
            'promocje': "[]",
            'error': "Nie znaleziono - kod 404 error"
        }
        return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        pozycje_pczas = []
        for pozp in promczas:
            pozycje_pczas.append({
                'status': pozp.status,
                'id_pczasp': pozp.id_pczasp,
                'id_prom_czas': pozp.id_prom_czas.id_pczas,
                'id_tow': pozp.id_tow.id_tow,
                'nazwa_tow':pozp.id_tow.nazwa_tow,
                'bar_kod_tow':pozp.id_tow.bar_kod_tow,
                'rabat': pozp.rabat,
                'nr_poz': pozp.nr_poz,
                'attr_prom': pozp.attr_prom,
                'ilosc_prom': pozp.ilosc_prom,
                'kwota_rab': pozp.kwota_rab,
                'cena_d_prom': pozp.cena_d_prom,
                'ilosc_plat':pozp.ilosc_plat,
                'ilosc_pkt':pozp.ilosc_pkt,
                'przelicz':pozp.przelicz,
                'nazwa_prom':pozp.id_prom_czas.nazwa_prom,
                'nr_prom': pozp.id_prom_czas.nr_prom,
                'typ_prom':pozp.id_prom_czas.typ_prom
            })

        #pozprom_serializer = PozPromSerializer(promocja, many=True)
        pozprom_serializer = PromocjaCzasPozycjaSerializer(pozycje_pczas, many=True)
        odpowiedz = {
            'wiadomosc': "Odczyt promocje o id = %s" % nrprom,
            'promocje': pozprom_serializer.data,
            'error': ""
        }
        return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
