from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth.models import Permission
import stripe
from django.shortcuts import render

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    # contextデータをオーバーライドして、シークレットキーをテンプレート側に渡す

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request):
    # 購入したユーザに本のアクセス権を追加
    u = request.user
    permission = Permission.objects.get(codename='special_status')
    u.user_permissions.add(permission)

    if request.method == "POST":
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken'],
        )
        return render(request, 'orders/charge.html')
