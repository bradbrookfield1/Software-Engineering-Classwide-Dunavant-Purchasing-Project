from django import forms

INVENTORY_FIELD_CHOICES = [
    ('asset_tag','Asset Tag'),
    ('last_audit_date','Last Audit Date'),
    ('company','Company'),
    ('department','Departments'),
    ('location','Locations'),
    ('equipment_type','Equipment Type'),
    ('vendor','Vendors'),
    ('purchase_price','Purchase Price'),
    ('purchase_date','Purchase Date'),
    ('equipment_manufacturer','Equipment Manufacturer'),
    ('equipment_model','Equipment Model'),
    ('assigned_to','Assigned To'),
    ('equipment_status','Equipment Status'),
    ('serial_number','Serial Number'),
    ('phone_number','Phone Number'),
    ('spare_location','Spare Inventory Location'),
    ('verizon_cost_center','Verizon Cost Center'),
    ('equipment_issue','Equipment Issue'),
    ('special_notes','Special Notes'),
    ('modified','Modified By'),
    ('purchase_order_number','Purchase Order #'),
    ('date_approved','Date Approved'),
    ('approving_supervisor', 'Approving Supervisor'),
    ('carrier_tracking_number','Carrier Tracking'),
    ('equipment_name','Equipment Name'),
    ('ip_address','IP Address'),
    ('konica_service_code','Konica Minolta Service Code'),
    ('notes','Notes'),
    ('item_type','Item Type'),
    ('path','Path'),
]
#class FieldSelectionList(forms.Form):
#