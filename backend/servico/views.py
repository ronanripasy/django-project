from django.shortcuts import render

# Create your views here.
def ordem_servico_list(request):
    template_name = 'servico/ordem_servico_list.html'
    object_list = OrdemServico.objects.all()
    context = {
        'object_list': object_list
    }
    return render(request, template_name, context)

def ordem_servico_create(request, pk):
    ...

def ordem_servico_detail(request, pk):
    ...

def ordem_servico_update(request, pk):
    ...