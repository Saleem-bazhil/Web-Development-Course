from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def home(request):
    return render(request, "login.html")


@login_required(login_url="/")
def main(request):

    return render(request, "main.html")


@login_required(login_url="/")
def Courses(request):

    cards = [
        {"image": "ht.png", "links": "/inventory/html/"},
        {"image": "css.jpeg", "links": "/inventory/css/"},
        {"image": "js.jpeg", "links": "/inventory/js/"},
        {"image": "react.png", "links": "/inventory/react"},
        {"image": "bootstrap.png", "links": "/inventory/bootstrap/"},
        {"image": "python.png", "links": "/inventory/python"},
        {"image": "django.png", "links": "/inventory/django"},
    ]

    return render(request, "courses.html", {"cards": cards})


@login_required(login_url="/")
def Htmlpage(request):

    data = [
        {"links": "https://www.youtube.com/embed/3jkub2c0kLA?si=8j26EJLpLUYQcdcd"},
        {"links": "https://www.w3schools.com/html/default.asp"},
    ]

    return render(request, "htmlcourse.html", {"data": data})


@login_required(login_url="/")
def Csspage(request):

    data = [
        {"links": "https://www.youtube.com/embed/vfs1wBDoqBY?si=LhMMTVJGsgIUQmQY"},
        {"links": "https://www.youtube.com/embed/ARZF2m8HBmQ?si=tQg8xQrz9Hp_1fwy"},
        {"links": "https://www.youtube.com/embed/1ungCm4GqZI?si=wmH_zTLsFTykHmoJ"},
        {"links": "https://www.youtube.com/embed/GLIPX_OwW1g?si=gJDsjjp6r3FGsJgG"},
        {"links": "https://www.youtube.com/embed/t4ElOfZZB-E?si=YAz6sPS9d_4RrcJq"},
        {"links": "https://www.youtube.com/embed/M1Q_wZtylqc?si=NOGFQ3JF4nt_csxO"},
        {"links": "https://www.youtube.com/embed/_k907kBlmDw?si=IQN1rPRR3xhEPbIn"},
        {"links": "https://www.youtube.com/embed/92yEIa045u8?si=rk8clEXlfSWtuQWe"},
        {"links": "https://www.youtube.com/embed/qWSIFFa_EfY?si=YpAzNnUWnFALYu18"},
        {"links": "https://www.youtube.com/embed/6S8FoeBmnsE?si=y005K0AkvWMRR88P"},
        {"links": "https://www.youtube.com/embed/9iySv0paX_4?si=5ALAze7Sjkfj1Jlr"},
        {"links": "https://www.youtube.com/embed/hVWhsHOQbXM?si=eQqSo8QH2fmwMPlW"},
        {"links": "https://www.youtube.com/embed/VN9hkmTvq3Y?si=oID-KYbSnzXQ6A_v"},
        {"links": "https://www.youtube.com/embed/4-bJX9xLGAQ?si=oINb16yODefZWOHf"},
        {"links": "https://www.youtube.com/embed/YJsqKbqgpEY?si=uCP7rmWQ7C_m7qdg"},
    ]

    return render(request, "css.html", {"data": data})


@login_required(login_url="/")
def JavacriptPage(request):

    data = [
        {"links": "https://www.youtube.com/embed/YrOkVD_YUro?si=8cMxePbIV-rmuoek"},
        {"links": "https://www.youtube.com/embed/4zlr_Ez_EYo?si=2rFlg0vcDZQmvTBH"},
        {"links": "https://www.youtube.com/embed/AoEohhf6Avc?si=qMCvnbQ3HUzWi0nn"},
        {"links": "https://www.youtube.com/embed/xs8bTPpONqA?si=TTiL5Q144F1auwNn"},
        {"links": "https://www.youtube.com/embed/csFBVXrsxck?si=Vrb9nB_NypaNqQIF"},
        {"links": "https://www.youtube.com/embed/Ub87voAYIWQ?si=kILiLYjJefS5Tn46"},
        {"links": "https://www.youtube.com/embed/eTaqetO9Ey8?si=MqkTXad9eBgU2yTV"},
        {"links": "https://www.youtube.com/embed/fbQ7xxXCusE?si=x7oB1hqKD_PK6eRQ"},
        {"links": "https://www.youtube.com/embed/OOHduxkXQAw?si=3HKPKXQPaFqxqACe"},
        {"links": "https://www.youtube.com/embed/B6DyTGL3ES8?si=QU6Akk8yWsqbsOSR"},
        {"links": "https://www.youtube.com/embed/HfVXI85nda8?si=ux62tKtcIehCirbN"},
        {"links": "https://www.youtube.com/embed/oukocVSYIDQ?si=93O8rTdHr1GXyzX0"},
        {"links": "https://www.youtube.com/embed/nhFYUGcC8jg?si=q_E6saIklTbrlVl8"},
        {"links": "https://www.youtube.com/embed/8__9yNADp_Q?si=TZxf-8bp50MjnAm_"},
        {"links": "https://www.youtube.com/embed/NiJxx4gxTBk?si=lU3PyOFlJ17aRszd"},
        {"links": "https://www.youtube.com/embed/jEmGxg3qURY?si=wPDqQyb-UShNarnU"},
        {"links": "https://www.youtube.com/embed/xN1boxJ99e0?si=BRSDnETs7GuBpLIK"},
        {"links": "https://www.youtube.com/embed/z62MfLU-QyQ?si=MtG6KrmlI5ElycrF"},
        {"links": "https://www.youtube.com/embed/JSPutp3KAu4?si=Ly53VEOzfEBLAVRu"},
        {"links": "https://www.youtube.com/embed/SOHdxS57HIo?si=Dk7sh_KjBp33xWsq"},
        {"links": "https://www.youtube.com/embed/g_aWNVwr0rE?si=EvkD4FQuTRZM-ed4"},
        {"links": "https://www.youtube.com/embed/ULr1zldSUOM?si=0ewMMqn3A7Uccj3Q"},
        {"links": "https://www.youtube.com/embed/0xeqwvBJJHk?si=ACIK-2WFmesO1l3x"},
        {"links": "https://www.youtube.com/embed/dGZRro2eFYA?si=1UpxIXwd1Kj1Gxz7"},
        {"links": "https://www.youtube.com/embed/JHP-G2npIac?si=GcKa-hQLALwQsZv8"},
        {"links": "https://www.youtube.com/embed/pVEd31BRD7g?si=HifkEG_K1hJbTJ5Y"},
        {"links": "https://www.youtube.com/embed/NDarzjLXCwg?si=vOMt6zR8C7s87xGt"},
        {"links": "https://www.youtube.com/embed/jkAp3eu2_tk?si=GJN-XGbOZcIoylYY"},
        {"links": "https://www.youtube.com/embed/WC5JgNrBwYU?si=GgBHCbapxci8Q-Zd"},
        {"links": "https://www.youtube.com/embed/w2nzvpCAvSs?si=UAcHK3d7w0mrRiG5"},
        {"links": "https://www.youtube.com/embed/qFU6cwT3_w4?si=bWNjChhVME8wTpZB"},
        {"links": "https://www.youtube.com/embed/c-o40o5Eyh4?si=VAxh2h1BeN3Bf0st"},
        {"links": "https://www.youtube.com/embed/4v_DdvoUj0k?si=NIFy7a8s62nEL02z"},
    ]

    return render(request, "js.html", {"data": data})


def BootstrapPage(request):

    data = [
        {"links": "https://www.youtube.com/embed/cwcRJkknjl4?si=NrBFbbgtlqz58rlG"},
        {"links": "https://www.youtube.com/embed/_8TrCzrhkJU?si=G8K8uxvSYUV23CLx"},
        {"links": "https://www.youtube.com/embed/O3qCdIL8F9w?si=nPUT8WX_3dw04RH5"},
        {"links": "https://www.youtube.com/embed/KYqllKwwf5A?si=wPBz_0Jt1nV3Y-jq"},
        {"links": "https://www.youtube.com/embed/dt5MaeDApwA?si=MgHzJlS2F8m5YbWS"},
        {"links": "https://www.youtube.com/embed/UHa9heaCpX0?si=O16ZimWBZjBRBuRc"},
        {"links": "https://www.youtube.com/embed/pVB8_tJmsso?si=_C7fVflsgRe7q87M"},
        {"links": "https://www.youtube.com/embed/iowddiMZu0s?si=A-FrgJ1mxKsGDSKN"},
        {"links": "https://www.youtube.com/embed/XZ_x08DDKuI?si=y47wwT1MerDzxeus"},
    ]

    return render(request, "bootstrap.html", {"data": data})


def React(request):

    data = [
        {"links": "https://www.youtube.com/embed/UYFtY7Acngw?si=OqnadcHvHCC55dcT"},
        {"links": "https://www.youtube.com/embed/SAUBFF4e50k?si=TwFN28eavH7bY6y4"},
        {"links": "https://www.youtube.com/embed/-kGdnjwTQww?si=yZQ5xPyQwh_GmnkAx"},
        {"links": "https://www.youtube.com/embed/c1KKItIY8tg?si=1swgw5D2mM1T_tkn"},
        {"links": "https://www.youtube.com/embed/9CvTo63v76k?si=483aGOpOu2q2s4wo"},
        {"links": "https://www.youtube.com/embed/D-RBvg6vva8?si=pV92Kx4FAkPCYjLL"},
    ]

    return render(request, "react.html", {"data": data})


def Python(request):

    data = [
        {"links": "https://www.youtube.com/embed/hSPwGniAafE?si=v-V61q4RGFhVrPFm"},
        {"links": "https://www.youtube.com/embed/BVIoAILnZ4Q?si=_3jkVvbEHkBAR4Ok"},
        {"links": "https://www.youtube.com/embed/Rtmgt2Qfqr4?si=eyRpvcgw9mV5GjiT"},
        {"links": "https://www.youtube.com/embed/qEWkjSRQ2dA?si=tXWeXUE--HM6pVsH"},
        {"links": "https://www.youtube.com/embed/CK938-UdPEE?si=dtBJmx_87vxma3Qc"},
        {"links": "https://www.youtube.com/embed/dHzYLjfr-uY?si=-KIpwqJ5pMK1exKx"},
    ]

    return render(request, "python.html", {"data": data})

def Django(request):
    
    data = [
        {"links":"https://www.youtube.com/embed/Vs-CmVKfWUA?si=MtSIdiavyw3cPaUl"},
        {"links":"https://www.youtube.com/embed/_6mfe54eUVc?si=0ww0sPYYNfLzotEA"},
        {"links":"https://www.youtube.com/embed/H_1VolxLMFw?si=gogjMLxS_o4-QeTM"},
        {"links":"https://www.youtube.com/embed/U-jtmc2ipLA?si=qyUJMoCWOeVeZSL7"},
        {"links":"https://www.youtube.com/embed/cVNTuZ_kVpg?si=ysadvyvkZ64_36OU"},
        {"links":"https://www.youtube.com/embed/Tdpbx5N_SOA?si=7NQFF0meLwAfCbZj"},
    ]
    
    return render(request,'django.html',{"data":data})