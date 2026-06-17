from .models import TickerItem, TickerSetting

def ticker_context(request):
    try:
        ticker_items = TickerItem.objects.filter(is_active=True)
        ticker_settings = TickerSetting.objects.first()
    except Exception:
        ticker_items = None
        ticker_settings = None
    return {
        'global_ticker_items': ticker_items,
        'global_ticker_settings': ticker_settings,
    }