# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from carService.models import Car, ServiceSituation, ServiceProduct, Service
from carService.models.Setting import Setting


def send_mail(service, to):
    if service.car.profile.isSendMail:
        situation = ServiceSituation.objects.filter(service=service).order_by('-id')[:1][
            0].situation.name
        car = Car.objects.get(uuid=service.car.uuid)
        logo = Setting.objects.get(key="logo-dark").value
        site_link = Setting.objects.get(key="site-link").value
        car_model = car.model
        car_brand = car.brand
        service_products = ServiceProduct.objects.filter(service=service)
        products = []

        for serviceProduct in service_products:
            isExist = False
            for productArr in products:
                if serviceProduct.product.uuid == productArr.uuid:
                    productArr.quantity = productArr.quantity + serviceProduct.quantity
                    productArr.netPrice = serviceProduct.productNetPrice * productArr.quantity
                    isExist = True

            if not isExist:
                product = serviceProduct.product
                product.netPrice = serviceProduct.productNetPrice
                product.totalProduct = serviceProduct.productTotalPrice
                product.taxRate = serviceProduct.productTaxRate
                product.quantity = serviceProduct.quantity
                products.append(product)
        labor = ServiceProduct.product
        labor.barcodeNumber = '-'
        labor.name = service.laborName
        labor.brand = None
        labor.quantity = 1
        labor.netPrice = service.laborPrice
        labor.taxRate = service.laborTaxRate
        labor.totalProduct = (
                float(service.laborPrice) + (float(service.laborPrice) * float(service.laborTaxRate) / 100))
        if labor.name != None:
            products.append(labor)
        profile = car.profile
        receiver = "-"
        if service.receiverPerson != None:
            receiver = service.receiverPerson
        name = ""
        product_table = ""

        for product in products:
            brand_name = ""
            if product.brand != None:
                brand_name = product.brand.name
            product_table = product_table + '''<tr>
                         <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;">''' + product.barcodeNumber + '''</td>
                         <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;">''' + product.name + '''</td>
                         <td style="font-size: 12px;   border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: right; padding: 7px;">''' + brand_name + '''</td>
                         <td style="font-size: 12px;   border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: right; padding: 7px;">''' + str(
                product.quantity) + '''</td>
                         <td style="font-size: 12px;   border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: right; padding: 7px;">''' + str(
                product.netPrice) + '''</td>
                         <td style="font-size: 12px;   border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: right; padding: 7px;">''' + str(
                product.taxRate) + '''</td>
                         <td style="font-size: 12px;   border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: right; padding: 7px;">''' + str(
                product.totalProduct) + '''</td>
                       </tr>'''
        if situation == "M????teri Onay?? Bekleniyor":
            product_table = '''
            <table style="border-collapse: collapse; width: 100%; border-top: 1px solid #DDDDDD; border-left: 1px solid #DDDDDD; margin-bottom: 20px;">
               <thead>
                 <tr>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: left; padding: 7px; color: #222222;" colspan="2">''' + "??ikayet" + '''</td>
                 </tr>
               </thead>
               <tbody>
                  <tr>
                   <td style="font-size: 12px;	border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;"><b>M????teri</b>''' + profile.firmName + "-" + \
                            profile.user.first_name + " " + profile.user.last_name + '''<br />
                     <b>Servise Getiren:</b> ''' + service.responsiblePerson + '''<br />
                     <b>Plaka:</b> ''' + car.plate + '''<br/>
                     <b>Marka/Model:</b> ''' + car_brand + '''/''' + car_model + '''</td>
                   <td style="font-size: 12px;	border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;"><b>Kilometre:</b>''' + str(
                service.serviceKM) + '''<br />
                     <b>Giri?? zaman??:</b> ''' + str(service.creationDate).split(".")[0] + '''<br />
                     <b>Teslim Alan:</b> ''' + receiver + '''<br /></td>
                 </tr>
               </tbody>
             </table>
            <table style="border-collapse: collapse; width: 100%; border-top: 1px solid #DDDDDD; border-left: 1px solid #DDDDDD; margin-bottom: 20px;">
               <thead>
                 <tr>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: left; padding: 7px; color: #222222;" colspan="2">''' + "??ikayet" + '''</td>
                 </tr>
               </thead>
               <tbody>
                 <tr>
                   <td style="font-size: 12px;	border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;">''' + service.complaint + '''</td>
                 </tr>
               </tbody>
             </table>
            <table style="border-collapse: collapse; width: 100%; border-top: 1px solid #DDDDDD; border-left: 1px solid #DDDDDD; margin-bottom: 20px;">
               <thead>
                 <tr>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: left; padding: 7px; color: #222222;" colspan="2">''' + "Tespit" + '''</td>
                 </tr>
               </thead>
               <tbody>
                 <tr>
                   <td style="font-size: 12px;	border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;">''' + service.description + '''</td>
                 </tr>
               </tbody>
             </table>
             <table style="border-collapse: collapse; width: 100%; border-top: 1px solid #DDDDDD; border-left: 1px solid #DDDDDD; margin-bottom: 20px;">
               <thead>
                 <tr>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: left; padding: 7px; color: #222222;">Barkod Numaras??:</td>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: left; padding: 7px; color: #222222;">??r??n Ad??:</td>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: right; padding: 7px; color: #222222;">Marka:</td>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: right; padding: 7px; color: #222222;">Adet:</td>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: right; padding: 7px; color: #222222;">Net Fiyat:</td>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: right; padding: 7px; color: #222222;">Vergi Oran??:</td>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: right; padding: 7px; color: #222222;">Toplam Fiyat:</td>
                 </tr>
               </thead>
               <tbody>
             ''' + product_table + '''</tbody>
               <tfoot>
               <tr>
                 <td style="font-size: 12px;	border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;" colspan="4"><b>Net Fiyat:     </b>''' + str(
                service.price) + '''</td>
                 <td style="font-size: 12px;	border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;" colspan="4"><b>Toplam Fiyat:     </b>''' + str(
                service.totalPrice) + '''</td>
               </tr>
               </tfoot>
             </table>'''
        elif situation == "Tamamland??":
            product_table = '''
            <table style="border-collapse: collapse; width: 40%; border-top: 1px solid #DDDDDD; border-left: 1px solid #DDDDDD; margin-bottom: 20px;">
               <thead>
                 <tr>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: left; padding: 7px; color: #222222;" colspan="2">''' + "DURUM" + '''</td>
                 </tr>
               </thead>
               <tbody>
                 <tr>
                   <td style="font-size: 12px;	border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;">Tamamland??</td>
                 </tr>
               </tbody>
             </table>
              <div>Arac??n??za ait servis i??lemi tamamlanm????t??r. Teslim almak i??in l??tfen servise geliniz.</div>'''

        elif situation == "Teslim Edildi":
            product_table = '''
            <table style="border-collapse: collapse; width: 40%; border-top: 1px solid #DDDDDD; border-left: 1px solid #DDDDDD; margin-bottom: 20px;">
               <thead>
                 <tr>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: left; padding: 7px; color: #222222;" colspan="2">''' + "DURUM" + '''</td>
                 </tr>
               </thead>
               <tbody>
                 <tr>
                   <td style="font-size: 12px;	border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;">Teslim edildi</td>
                 </tr>
               </tbody>
             </table>
                <div>''' + car.plate + '''  plakal?? arac??n??z ''' + receiver + ''' isimli ki??iye teslim edilmi??tir.</div>    
            '''

        else:
            product_table = ""
        if (profile.firmName):
            name = profile.firmName + "-" + \
                   profile.user.first_name + " " + profile.user.last_name
        else:
            name = profile.user.first_name + " " + profile.user.last_name
        serviceman = service.serviceman.user.first_name + \
                     " " + service.serviceman.user.last_name
        subject, from_email = 'Kulmer Motorlu Ara??lar Servis Bilgilendirme', 'servis@kulmer.com.tr'
        text_content = 'Kulmer Motorlu Ara??lar Servis Bilgilendirme'

        html = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/1999/REC-html401-19991224/strict.dtd">
           <html>
           <head>
           <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
           </head>
           <body style="font-family: Arial, Helvetica, sans-serif; font-size: 12px; color: #000000;">
            <div style="align-items: center; width: 680px;"><img src="''' + logo + '''" style="margin-left:auto; margin-right:auto; margin-bottom: 20px; width:200px; border: none;" />
             <h3><a href="''' + site_link + '''">Giri?? yapmak i??in t??klay??n??z</a></h3>
             ''' + product_table + '''
           </div>
           </body>
           </html>'''

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html, "text/html")
        msg.send()


def send_password(password, to):
    # bura m?? her yerde gitmi??
    text_content = 'Kulmer Motorlu Ara??lar Servis Takip Yaz??l??m?? Hesap Bilgileri'
    subject, from_email = 'Kulmer Motorlu Ara??lar Servis Takip Yaz??l??m?? Hesap Bilgileri', settings.EMAIL_HOST_USER
    logo = Setting.objects.get(key="logo-dark").value
    site_link = Setting.objects.get(key="site-link").value
    html = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/1999/REC-html401-19991224/strict.dtd">
 <html>
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  </head>
    <body style="font-family: Arial, Helvetica, sans-serif; font-size: 12px; color: #000000;">
    <div style="align-items: center; width: 900px;";><a href="''' + logo + '''" title=""><img src="''' + logo + '''" style="margin-left:auto; margin-right:auto; margin-bottom: 20px; width:200px; border: none;" /></a>
    <h3><a href="''' + site_link + '''">Giri?? yapmak i??in t??klay??n??z:</a></h3>	
    <h4>Merhaba, Kulmer Motorlu Ara??lar Servis Takip Sistemine ho??geldiniz.<br>A??a????da bulunan kullan??c?? ad?? ve ??ifrenizle sisteme giri?? yapabilirsiniz. <br>Sizleri aram??zda g??rmekten mutluluk duyuyoruz.</h4>
        </div>
    
     <table style="border-collapse: collapse; width: 40%; border-top: 1px solid #DDDDDD; border-left: 1px solid #DDDDDD; margin-bottom: 20px;"> 
               <thead>
                 <tr>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: left; padding: 7px; color: #222222;">Kullan??c?? Ad??</td>
                   <td style="font-size: 12px; border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; background-color: #EFEFEF; font-weight: bold; text-align: left; padding: 7px; color: #222222;">??ifre</td>
                 </tr>
               </thead>
               <tbody>
                 <tr>
                   <td style="font-size: 12px;	border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;">''' + to + '''</td>
                   <td style="font-size: 12px;	border-right: 1px solid #DDDDDD; border-bottom: 1px solid #DDDDDD; text-align: left; padding: 7px;">''' + password + '''</td>
                 </tr>
               </tbody>
             </table>
  </body>
  </html> 
  '''

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html, "text/html")
    msg.send()
