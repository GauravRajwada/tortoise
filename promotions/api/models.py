from django.db import models


"""
super users
UserName: admin
password: aa

"""
# Create your models here.
class Plans(models.Model):
    planId=models.AutoField(primary_key=True,auto_created = True)
    planName=models.CharField(max_length=100)
    amounts=models.FloatField()
    tenure=models.CharField(max_length=100)
    benifitPercentage=models.FloatField()
    CASHBACK='Cashback'
    EXTRAVOUCHER='ExtraVoucher'

    bTypes=[(CASHBACK,'Cashback'),
            (EXTRAVOUCHER,'ExtraVoucher')]
    benifitTypes=models.CharField(max_length=100,
                choices=bTypes,
                default=EXTRAVOUCHER)