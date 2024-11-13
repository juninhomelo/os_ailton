from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa

from django.contrib import admin
from service_orders.models import Brand, ServiceOrder


def generate_pdf(self, request, queryset):
    for obj in queryset:
        html_string = render_to_string('pdf.html', {'object': obj})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=OS_{obj.id}.pdf'

        pisa_status = pisa.CreatePDF(html_string, dest=response)

        if pisa_status.err:
            return HttpResponse(f'Erro ao gerar PDF para a OS {obj.id} <pre>{html_string}</pre>')
    return response


class ServiceOrderAdmin(admin.ModelAdmin):
    '''def formated_phone(self):
        phone = self.phone.strip()  # Remove espaços extras, caso existam
        if len(phone) == 11:  # Celular (9 dígitos + DDD)
            return f'({phone[0:2]}) {phone[2:7]}-{phone[7:11]}'
        elif len(phone) == 10:  # Fixo (8 dígitos + DDD)
            return f'({phone[0:2]}) {phone[2:6]}-{phone[6:10]}'
        return phone  # Retorna o número original se não tiver o número de dígitos esperado
    formated_phone.short_description = 'Telefone com DDD'
    '''
    ordering = ['id']
    actions = [generate_pdf]


class BrandAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']
  



generate_pdf.short_description = 'Gerar PDF'

admin.site.register(Brand, BrandAdmin)
admin.site.register(ServiceOrder, ServiceOrderAdmin)
