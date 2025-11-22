import datetime
import calendar

def monthly_charge(month, subscription, users):
    if not subscription or not users:
        return 0

    year, month_num = map(int, month.split('-'))
    start_date = datetime.date(year, month_num, 1)
    _, last_day = calendar.monthrange(year, month_num)
    end_date = datetime.date(year, month_num, last_day)

    active_users = []
    for u in users:
        if u["customer_id"] != subscription["customer_id"]:
            continue

        activated_str = u.get("activated_on")
        deactivated_str = u.get("deactivated_on")

        activated = datetime.date.fromisoformat(activated_str) if activated_str else None
        deactivated = datetime.date.fromisoformat(deactivated_str) if deactivated_str else None

        if (not activated or activated <= end_date) and (not deactivated or deactivated >= start_date):
            active_users.append(u)

    if not active_users:
        return 0

    total = len(active_users) * subscription["monthly_price_in_cents"]
    return round(total)