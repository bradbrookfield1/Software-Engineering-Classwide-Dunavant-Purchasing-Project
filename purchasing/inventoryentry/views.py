from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Asset, Log
from .forms import AssetForm

allFields = ['asset_Tag', 'purchase_Order_Number', 'company',
             'department', 'location', 'iP_Address', 'spare_Inventory_Location', 'RMA',
             'equipment_Name', 'equipment_Manufacturer', 'vendor',
             'equipment_Type', 'tracking_Number', 'equipment_Model', 'price',
             'serial_Number', 'status', 'phone', 'verizon_Cost_Center',
             'attachments', 'additional_Specs', 'approval_Date', 'last_Audit_Date',
             'purchase_Date', 'incident_Status', 'equipment_Issues', 'special_Notes',
             'last_Modified']


class AssetListView(LoginRequiredMixin, ListView):
    model = Asset
    ordering = ['asset_Tag']


class AssetDetailView(LoginRequiredMixin, DetailView):
    model = Asset


class AssetCreateView(LoginRequiredMixin, CreateView):
    model = Asset
    form_class = AssetForm

    def form_valid(self, form):
        log = Log(
            author=self.request.user,
            action="created",
            asset=form.cleaned_data['asset_Tag'],
        )
        log.save()
        return super().form_valid(form)


class AssetUpdateView(LoginRequiredMixin, UpdateView):
    model = Asset
    form_class = AssetForm

    def form_valid(self, form):
        log = Log(
            author=self.request.user,
            action="updated",
            asset=form.cleaned_data['asset_Tag'],
        )
        log.save()
        return super().form_valid(form)


class AssetDeleteView(LoginRequiredMixin, DeleteView):
    model = Asset
    success_url = 'inventory:asset-list'

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        log = Log(
            author=self.request.user,
            action="deleted",
            asset=obj.asset_Tag,
        )
        log.save()
        return super().post(request)

    def get_success_url(self):
        return reverse('inventory:asset-list')


class LogListView(LoginRequiredMixin, ListView):
    model = Log
    ordering = ['-date']


class LogDeleteView(LoginRequiredMixin, DeleteView):
    model = Log
    success_url = 'inventory:log-list'

    def get_success_url(self):
        return reverse('inventory:log-list')
