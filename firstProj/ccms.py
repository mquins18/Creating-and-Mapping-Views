from django.http import HttpResponse

def Mission(request):
    return HttpResponse('<h1>Mission</h1><br> The College of Computer Studies shall Produce technically competent <br> Information Technology professionals adequately prepared in the practice of their profession <br> supportive of national development goals and standards of global excellence.')


def Vision(request):
    return HttpResponse('<h1>Vision</h1><br> The College of Computer Studies shall be a Center of Excellence in Information Technology education')



def Objectives(request):
    return HttpResponse('<h1>Objectives</h1><br> <h4> After graduation, Alumnio of MSEUF-CCMS programs shall</h4><br> 1.Be employed and demonstrate  professionalism, competence and passion <br> in solving contemporary computing problems by developing or utilizing innovative IT solutions <br> <br>2. Embark in lifelong learning or research to attune to the continuous innovation in the IT industry <br> in order to adapt to the changing demands of the global market; and <br> <br>3. Exhibit leadership and teamwork, and commitment to their respective local or global organizations. ')