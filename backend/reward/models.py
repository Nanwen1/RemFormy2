from django.db import models


class Rem(models.Model):
    ASSETS = (
        ('NiW', 'NiW'),
        ('WAIO', 'WAIO'),
    )

    REGIONS = (
        ('MinAus', 'MinAus'),
        ('MinAm', 'MinAm'),
        ('Functions', 'Functions'),
        ('Petroleum', 'Petroleum'),
    )

    GRADES = (
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
    )

    asset_Func = models.CharField(max_length=120, null=True, blank=True, choices=ASSETS)
    grade = models.TextField(max_length=2, default="6", choices=GRADES)
    jobFamily = models.CharField(max_length=120)
    midpoint = models.IntegerField(default="100000")
    STI = models.IntegerField(default="10")
    superannuation = models.IntegerField()
    region = models.CharField(max_length=120, default="MinAus", choices=REGIONS)

    def __str__(self):
        return self.asset_Func


class Allowance(models.Model):
    name = models.CharField(max_length=120)
    annual_amount = models.IntegerField()
    asset_Func = models.ForeignKey(Rem, on_delete=models.CASCADE)
    annual_leave = models.CharField(max_length=120)
    annual_hours = models.IntegerField()

    def __str__(self):
        return self.name
