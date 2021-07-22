from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from django.http import response
from django.shortcuts import render
# Create your views here.


# Create your views here.
from pracownicy.serializers import PracownicySerializer, PracLoginSerializer
from pracownicy.models import Pracownicy
from pracownicyplac.models import PracownicyPlac

from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['POST'])
def pracownik_login(request):
    if request.method == 'POST':
        login_data = JSONParser().parse(request)
        login = login_data['nazwaUzytkownika']
        passwd = login_data['haslo']

        print('login:', login)
        print('haslo:', passwd)

    if passwd == '':
        if len(login) == 13 and login[:6] == '200000':

            prac_key = Pracownicy.objects.raw(
                'select distinct p.id_prac,\
                        p.nazw_prac, \
                        p.imie_prac, \
                        p.ident_prac,\
                        p.attr_prac,\
                        p.klucz_prac, \
                        pl.db_id, \
                        db.db_name, \
                        p.status, \
                        pl.status as plstatus \
                from pracownicy p left outer join pracownicy_plac pl \
                    on p.id_prac = pl.id_prac \
                        left outer join databases db on db.db_id = pl.db_id\
                where (pl.status is null or pl.status =0) and p.status = 0 and p.klucz_prac = %s', [login])
            if len(prac_key) > 0:
                for pr in prac_key:
                    daneprac = {
                        'nazw_prac': pr.nazw_prac,
                        'imie_prac': pr.imie_prac,
                        'ident_prac': pr.ident_prac,
                        'klucz_prac': pr.klucz_prac,
                        'attr_prac': pr.attr_prac,
                        'id_prac': pr.id_prac,
                        'db_id': pr.db_id,
                        'db_name': pr.db_name,
                        'status': pr.status,
                        'plstatus': pr.plstatus
                    }
                prac_serializer = PracLoginSerializer(daneprac, many=False)
                odpowiedz = {
                    'wiadomosc': "Odczyt pracownicy o klucz_prac = %s" % login,
                    'pracownicy': [prac_serializer.data],
                    'error': ""
                }
                return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
            else:
                exceptionError = {
                    'wiadomosc': "Zły klucz  pracownika  %s " % login,
                    'pracownicy': "[]",
                    'error': "Nie znaleziono - kod 404 error"
                }
                return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)

        else:
            exceptionError = {
                'wiadomosc': 'NIeprawidłowy format danych %s' % login,
                'pracownicy': '[]',
                'error': 'błąd'
            }
            return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
    else:
        prac_login = Pracownicy.objects.raw(
            'select distinct p.id_prac,\
                    p.nazw_prac, \
                    p.imie_prac, \
                    p.ident_prac,\
                    p.attr_prac,\
                    p.klucz_prac, \
                    pl.db_id, \
                    db.db_name, \
                    p.status, \
                    pl.status as plstatus \
            from pracownicy p left outer join pracownicy_plac pl \
                on p.id_prac = pl.id_prac \
                    left outer join databases db on db.db_id = pl.db_id \
            where (pl.status is null or pl.status =0) and p.status = 0 and p.ident_prac = %s', [login])
        if len(prac_login) == 0:
            exceptionError = {
                'wiadomosc': "Zly login  pracownika  %s " % login,
                'pracownicy': "[]",
                'error': "Nie znaleziono - kod 404 error"
            }
            return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
        else:
            prac_passwd = Pracownicy.objects.raw(
                'select distinct p.id_prac,\
                    p.nazw_prac, \
                    p.imie_prac, \
                    p.ident_prac,\
                    p.attr_prac,\
                    p.klucz_prac, \
                    pl.db_id, \
                    db.db_name, \
                    p.status, \
                    pl.status as plstatus \
            from pracownicy p left outer join pracownicy_plac pl \
                on p.id_prac = pl.id_prac \
                    left outer join databases db on db.db_id = pl.db_id \
             where (pl.status is null or pl.status =0) and p.status = 0 and p.haslo_prac = %s', [passwd])
            if len(prac_passwd) > 0:
                for pr in prac_passwd:
                    daneprac = {
                        'nazw_prac': pr.nazw_prac,
                        'imie_prac': pr.imie_prac,
                        'ident_prac': pr.ident_prac,
                        'klucz_prac': pr.klucz_prac,
                        'attr_prac': pr.attr_prac,
                        'id_prac': pr.id_prac,
                        'db_id': pr.db_id,
                        'db_name': pr.db_name,
                        'status': pr.status,
                        'plstatus': pr.plstatus
                    }
                    prac_serializer = PracLoginSerializer(daneprac, many=False)
                    odpowiedz = {
                        'wiadomosc': "Odczyt pracownicy o loginie = %s" % login,
                        'pracownicy': [prac_serializer.data],
                        'error': ""
                    }
                return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
            else:
                exceptionError = {
                    'wiadomosc': "Zły password  pracownika  %s " % passwd,
                    'pracownicy': "[]",
                    'error': "Nie znaleziono - kod 404 error"
                }
                return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
