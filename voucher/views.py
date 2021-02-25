from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Voucher
from .forms import VoucherApplyForm

def voucher_apply(request):
    now = timezone.now()
    form = VoucherApplyForm(require_POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            voucher = Voucher.objects.get(code_iexact = code, valid_from_lte = now, valid_to__get =now, active=True)
            request.sessions['voucher_id'] = voucher.id
        except Voucher.DoesNotExist:
            request.sessions['voucher_id'] = None
    return redirect('cart:cart_detail')