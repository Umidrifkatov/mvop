from django.shortcuts import render
import random
from .models import patient




def passgenerate():
    keys = '123456789qwertyuipasdfghjklzxcvbnmQWERTYUIPASDFGHJKLZXCVBNM'
    bit = 64
    bit2 = 0
    result = ''
    while bit > bit2:
        bit2 += 1
        result += random.choice(keys)
    return result





def main(request):
    if not request.POST:
        key = passgenerate()
        print(key)
        pati = patient.objects.create(key=key)
        step = 1
        print(key)
        context = {
        "key": key,
        "step": step,
        }

        return render(request, 'main.html', context)
    
    
    elif request.POST and request.POST.get('age'):
        key = request.POST.get('key')
        pati = patient.objects.get(key=key)
        pati.age = request.POST.get('age')
        pati.save()
        step = 2
        print(key)
        context = {
        "key": key,
        "step": step,
        }

        return render(request, 'main.html', context)

    elif request.POST and request.POST.get('sex'):
        key = request.POST.get('key')
        pati = patient.objects.get(key=key)
        pati.sex = request.POST.get('sex')
        pati.save()
        step = 3
        context = {
        "key": key,
        "step": step,
        }

        return render(request, 'main.html', context)

    elif request.POST and request.POST.get('weight') and request.POST.get('height') :
        key = request.POST.get('key')
        pati = patient.objects.get(key=key)

        we = int(request.POST.get('weight'))
        he = int(request.POST.get('height'))
        he = he/100
        bmi = we/(he**2)
        print(bmi)
        if bmi > 25:
            bmi = True
        else:
            bmi = False

        print(bmi)


        pati.bmi = bmi

        pati.save()
        step = 4
        context = {
        "key": key,
        "step": step,
        }

        return render(request, 'main.html', context)



    elif request.POST and request.POST.get('echt'):
        key = request.POST.get('key')
        pati = patient.objects.get(key=key)
        pati.echt = request.POST.get('echt')
        pati.save()
        step = 5
        context = {
        "key": key,
        "step": step,
        }

        return render(request, 'main.html', context)


    elif request.POST and request.POST.get('sinovit'):
        key = request.POST.get('key')
        pati = patient.objects.get(key=key)
        pati.sinovit = request.POST.get('sinovit')
        pati.save()
        step = 6
        context = {
        "key": key,
        "step": step,
        }

        return render(request, 'main.html', context)


    elif request.POST and request.POST.get('c_react'):
        key = request.POST.get('key')
        pati = patient.objects.get(key=key)
        pati.c_react = request.POST.get('c_react')
        pati.save()
        step = 7
        context = {
        "key": key,
        "step": step,
        }
        return render(request, 'main.html', context)

    elif request.POST and request.POST.get('comp'):
        key = request.POST.get('key')
        pati = patient.objects.get(key=key)
        pati.comp = int(request.POST.get('comp'))
        if pati.comp <= 1000:
            pati.compc = 'norm'
        elif pati.comp > 1000 and pati.comp < 1500:
            if pati.age > 50 and pati.age < 66:
                pati.compc = 'norm'
            elif pati.age <= 50:
                pati.compc = 'up1'
            elif pati.age >= 65:
                pati.compc = 'up2'
        elif pati.comp >= 1500 and pati.comp < 2001:
            if pati.comp > 65:
                pati.compc = 'up3'
            else:
                pati.compc = 'up3'
        else:
            pati.compc = 'up3'

        pati.save()
        
        step = 8
        context = {
        "key": key,
        "step": step,
        }

        return render(request, 'main.html', context)

    elif request.POST and request.POST.get('xray'):
        key = request.POST.get('key')
        pati = patient.objects.get(key=key)
        pati.xray = request.POST.get('xray')
        pati.save()
        step = 9
        
        #comp123
        norm = "<b>Тоғай деструкцияси белгилари йўқ!</b>"
        text1 = """ <b>Тоғай деструкциясининг илк белгилари!</b> <br><br>
                Per os 3 ой давомида хондропротекторлар (хондроитин сульфат)+ Гарпогафитум 250 мг/кунига 6 ой (Суставин 2 таблетка кунига)
                \n"""
        text2 = """<b>Ифодаланган тоғай деструкцияси белгилари!</b> <br><br>
            Per os 3 ой давомида хондропротекторлар (хондроитин сульфат) + Гарпогафитум 500 мг/кунига 6 ой 
                (Суставин 2 таблеткадан 2маҳал кунига)\n"""
        text3 = """<b>Яққол ифодаланган тоғай деструкцияси белгилари!</b> <br><br>
                    Per os 3 ой давомида хондропротекторлар (хондроитин сульфат)+ Гарпогафитум 750 мг/кунига 6 ой (Суставин 2таблеткадан 3 маҳал кунига)\n"""
        #if xray > 2 ++ comp
        text31 = """+ НЯҚВ талабга кўра тавсия этиш """
        #if xray == 3-4
        text32 = """ Травматолог консультацияси, эндопротезлаш амалиёти масалаларини ҳал этиш """
        
        
        #sinovit
        text4 = """Локал бўғим ичига гормонал суспензия (бетаметазон) пункцияси """
        #bmi
        text5 = """Тана вазни меъёрий бўлгани боис, ортиқча тана вазни профилактикасига эътибор қаратиш зарур, соғлом турмуш тарзига амал қилиш тавсия этилади"""
        text6 = """Калория танқислиги ҳисобланган кўрсаткичга нисбатан 500-600 ккал бўлган, ёғ миқдори <30%, углеводлар 50-55%, оқсиллар - 15-20% бўлган гипокалорик парҳез + Изометрик машқ (овқатланишдан кейин ётмаслик ва 10-15 дақиқа давомида оддий харакатлар қилиш ёки юриш) 
                тавсия этилади."""
        
        rec_text1 = ''
        rec_text2 = ''
        rec_text3 = ''

        if int(pati.xray) <= 2:
            if pati.compc == 'up1':
                rec_text1 += text1
            elif pati.compc == "up2":
                rec_text1 += text2
            elif pati.compc == 'up3':
                rec_text1 += text3
            elif pati.compc == 'norm':
                rec_text1 += norm
                text31 = ''

        if int(pati.xray) == 2:
            rec_text1 += text31
        if int(pati.xray) > 2:
            rec_text1 = text32
        if pati.sinovit:
            rec_text2 += text4
        if pati.bmi:
            rec_text3 += text6
        else:
            rec_text3 += text5
        
        





        lfk_text1 = """
                    1-юкламасиз машқ.
 Текис юзада,  бемор чалқанчасига ётган вазиятда бажарилади. Бунда бемор гўёки “велосипед ҳайдаш” жараёнидаги ҳаракатларни имитация қилиб, иккала оёқни тизза бўғимида бирин кетин букиш ва ёзиш машқларини амалга оширади Бунда  тизза бўғимида бирин кетин букиш ва ёзиш 10 марта амалга оширилади. 
        """

        lfk_text2 = """ 2-юкламасиз машқ. 
Текис юзада,  бемор чалқанчасига ётган вазиятда бажарилади. Бунда бемор аввал ўнг (чап) оёғини тизза бўғимида букиб, сонига яқинлаштиради. Бунда шу оёқнинг товони ердан узилмаслиги лозим.  Тизза бўғимида букилган ҳолатда оёқни кўтариб, 10-20 сония  вазият фиксацияланиб, сўнг секинлик билан тизза бўғими ёзилади. Ҳар бир оёқ учун 10 марта бажарилади """

        lfk_text3 = """  3-юкламасиз машқ. 
Текис юзада,  бемор чалқанчасига ётган вазиятда бўлиши лозим. Бемор оёқлари узатилган ҳолатда, қўллари тананинг ён томонида жойлаштирилиб, иккала оёқ панжаларини максимал танага яқинлаштириб, узоқлаштириш (юқорига ва пастга) машқлари бажарилади. Ҳар бир оёқ учун 10 марта бажарилади.  """




        


        context = {
        "key": key,
        "step": step,
        "rec1": rec_text1,
        "lfk1": lfk_text1,
        "lfk2": lfk_text2,
        "lfk3": lfk_text3,
        "rec2":rec_text2,
        "rec3":rec_text3,


        }

        return render(request, 'main.html', context)

        

    # Рекомендации
    