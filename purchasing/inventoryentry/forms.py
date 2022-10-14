from django import forms
from .models import Asset

RMA_choices = (('Yes', 'Yes'), ('No', 'No'))
status_choices = (('Approved', 'Approved'), ('Damaged', 'Damaged'),
                  ('Disposed', 'Disposed'), ('Donated', 'Donated'),
                  ('In Service', 'In Service'), ('Missing', 'Missing'),
                  ('Needs Investigation', 'Needs Investigation'),
                  ('Needs Repair', 'Needs Repair'),
                  ('Not In Service', 'Not In Service'),
                  ('Ordered', 'Ordered'), ('Out Of Service', 'Out Of Service'),
                  ('Recycled', 'Recycled'), ('RMA', 'RMA'),
                  ('Spare (Ready For Service)', 'Spare (Ready For Service)'),
                  ('Stolen', 'Stolen'))
location_choices = (('Atlanta', 'Atlanta'), ('Baltimore', 'Baltimore'), ('Baytown', 'Baytown'),
                    ('Charleston', 'Charleston'), ('Dallas',
                                                   'Dallas'), ('Fort Worth', 'Fort Worth'),
                    ('La Porte (437)', 'La Porte (437)'), ('La Porte (437B)',
                                                           'La Porte (437B)'),
                    ('La Porte (501)', 'La Porte (501)'), ('La Porte (501B)',
                                                           'La Porte (501B)'),
                    ('Los Angeles', 'Los Angeles'), ('Memphis Headquarters',
                                                     'Memphis Headquarters'),
                    ('Memphis Terminal', 'Memphis Terminal'), ('Mobile', 'Mobile'),
                    ('Nashville', 'Nashville'), ('Norfolk', 'Norfolk'),
                    ('Pasadena (9401)', 'Pasadena (9401)'), ('Pasadena (9431)',
                                                             'Pasadena (9431)'),
                    ('Pasadena (9501)', 'Pasadena (9501)'), ('Pasadena (9531)',
                                                             'Pasadena (9531)'),
                    ('Puerto Rico', 'Puerto Rico'), ('Savannah', 'Savannah'),
                    ('Wallisville', 'Wallisville'), ('Wilmington', 'Wilmington'))


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ['asset_Tag', 'purchase_Order_Number', 'company',
                  'department', 'location', 'iP_Address', 'spare_Inventory_Location', 'RMA',
                  'equipment_Name', 'equipment_Manufacturer', 'vendor',
                  'equipment_Type', 'tracking_Number', 'equipment_Model', 'price',
                  'serial_Number', 'status', 'phone', 'verizon_Cost_Center',
                  'attachments', 'additional_Specs', 'approval_Date', 'last_Audit_Date',
                  'purchase_Date', 'incident_Status', 'equipment_Issues', 'special_Notes',
                  'last_Modified']
        widgets = {
            'RMA': forms.Select(choices=RMA_choices),
            'location': forms.Select(choices=location_choices),
            'status': forms.Select(choices=status_choices)
        }
