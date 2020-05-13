from datetime import datetime

import unicodecsv
from django.contrib import admin
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.utils import timezone


class CSVAdmin(admin.ModelAdmin):
    """
    Adds a CSV export action to an admin view.
    """

    # This is the maximum number of records that will be written.
    # Exporting massive numbers of records should be done asynchronously.
    csv_record_limit = 1000
    export_fields = ()

    def get_actions(self, request):
        actions = self.actions if hasattr(self, 'actions') else []
        actions.append('csv_export')
        actions = super(CSVAdmin, self).get_actions(request)
        return actions

    def csv_export(self, request, qs=None, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % slugify(self.model.__name__)
        headers = self.export_fields if self.export_fields else list(self.list_display)
        writer = unicodecsv.DictWriter(response, headers)

        # Write header.
        header_data = {}
        for name in headers:
            if hasattr(self, name):
                try:
                    header_data[name] = getattr(
                        getattr(self, name), 'short_description')
                except AttributeError:
                    header_data[name] = name.title()
            else:
                field = self.model._meta.get_field(name)
                if field and field.verbose_name:
                    header_data[name] = field.verbose_name
                else:
                    header_data[name] = name
            header_data[name] = header_data[name].title()
        writer.writerow(header_data)

        # Write records.
        for r in qs[:self.csv_record_limit]:
            data = {}
            for name in headers:
                if hasattr(r, name):
                    value = getattr(r, name)
                    if isinstance(value, datetime):
                        data[name] = timezone.localtime(value)
                    else:
                        data[name] = value
                elif hasattr(self, name):
                    value = getattr(self, name)(r)
                    if isinstance(value, datetime):
                        data[name] = timezone.localtime(value)
                    else:
                        data[name] = value
                else:
                    raise Exception('Unknown field: %s' % (name,))

                if callable(data[name]):
                    data[name] = data[name]()
            writer.writerow(data)
        return response

    csv_export.short_description = 'Exported selected %(verbose_name_plural)s as CSV'
