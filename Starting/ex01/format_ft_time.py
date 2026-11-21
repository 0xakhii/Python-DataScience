import datetime as dtm
import decimal as dc
epoch = dtm.datetime(1970, 1, 1)
seconds = (dtm.datetime(2026, 6, 23) - epoch).total_seconds()
datetime_now = dtm.datetime.now()
pretty_dtm_now = "%b %d %Y"
dtmNow = datetime_now.strftime(pretty_dtm_now)
print("Second since January 1, 1970: ", f"{seconds:,}", "or", '%.2E' % dc.Decimal(seconds), "in scientific notation")
print(dtmNow)
