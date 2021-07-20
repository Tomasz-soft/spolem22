from django.db import router
from towary.models import Towary
from promocje.models import Promocje, PozProm
from sklepy.models import Sklepy


class kalendarzRouter:

    aplikacje = {'promocje', 'towary'}
    ap_centra = {'sklepy', 'pracownicy', 'prominfo', 'pracownicyplac'}
    ap_prominfo = {'prominfo'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.aplikacje:
            print('akuku')
            return True
        else:
            if model._meta.app_label in self.ap_centra:
                print(model._meta.app_label)
                return 'centrala'
            else:
                print('cekuku')
                return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.ap_prominfo:
            print('do zapsiu')
            return 'centrala'
        else:
            print('dekuku')
            return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.aplikacje or
            obj2._meta.app_label in self.aplikacje
        ):
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.aplikacje:
            return False
        return None
