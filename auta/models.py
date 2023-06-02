from django.db import models


class Auto(models.Model):
    marka = models.CharField(max_length=64, blank=False, unique=True)
    model = models.CharField(max_length=64, blank=False, unique=True)
    rok_produkcji = models.PositiveSmallIntegerField(blank=False)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    oceny = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    w_sprzedazy = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.marka, str(self.rok_produkcji))


class ExtraInfo(models.Model):
    NADWOZIE = {
        (0, 'pick-up'),
        (1, 'Hatchback'),
        (2, 'combi'),
        (3, 'sedan'),
        (4, 'kabriolet'),
        (5, 'coupe'),
        (6, 'roadster')
    }
    przebieg = models.PositiveSmallIntegerField(null=True, blank=True)
    nadwozie = models.PositiveSmallIntegerField(choices=NADWOZIE, null=True, blank=True)
    punkty_kierowcow = models.PositiveSmallIntegerField(default=0)
    auto = models.OneToOneField(Auto, on_delete=models.CASCADE, null=True, blank=True)   # <-- relacja 1-to-1 z modelem 'Auto'

# Po ustaleniu relacji z modelem Auto możliwa jest następująca zmiana reprezentacji tekstowej modelu ExtraInfo
    def __str__(self):
        for g in list(self.NADWOZIE):
            if g[0] == self.nadwozie:
                gok = g[1]
        return "Auto: {}, gatunek: {}, przebieg: {}, punkty od widzów: {}".format(self.auto.marka, gok, self.przebieg, self.punkty_kierowcow)

class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)        # <-- relacja many-to-1 z modelem 'Auto'

    # Po ustaleniu relacji z modelem Auto możliwa jest następująca zmiana reprezentacji tekstowej modelu Ocena
    def __str__(self):
        rec = self.recenzja[:20] + ' ...'
        return "Auto: {}, gwiazdki: {}, recenzja: {}".format(self.auto.marka, str(self.gwiazdki), rec)

class Model_auta(models.Model):
    pojemnosc = models.CharField(max_length=32)
    konie_mechaniczne = models.CharField(max_length=32)
    auto = models.ManyToManyField(Auto)  # <-- relacja many-to-many z modelem 'Autoilm'

    # Po ustaleniu relacji z modelem Auto możliwa jest następująca zmiana reprezentacji tekstowej modelu Aktor

    def __str__(self):
        return "{} {}, w {} autach z bazy danych".format(self.pojemnosc, self.konie_mechaniczne, str(self.auto.count()))
