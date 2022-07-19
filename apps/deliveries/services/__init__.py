from apps.deliveries.services.currency_rate import get_rate
from apps.deliveries.services.google_sheets import GoogleSheet
from apps.database import db
from apps.deliveries.models import Delivery
from time import sleep


def update_delivery_database(app, freq_sec: int):
    sheet = GoogleSheet("Sheet1", "Test Case")

    with app.app_context():
        while True:
            try:
                usd_rate = get_rate()

                cur_rows = Delivery.query.all()

                new_rows = []

                sheets_rows = sheet.extract_table()
                if len(sheets_rows) == 0:
                    sleep(5)
                    continue

                for row in sheets_rows:
                    usd = float(row[1])
                    delivery = Delivery(number=row[0],
                                        cost_usd=usd,
                                        cost_rub=round(usd * usd_rate, 2),
                                        term="-".join(reversed(row[2].split(".")))
                                        )

                    if delivery not in cur_rows:
                        db.session.add(delivery)
                        db.session.commit()

                    new_rows.append(delivery)

                for row in cur_rows:
                    if row not in new_rows:
                        db.session.query(Delivery).filter(Delivery.id == row.id).delete()
                        db.session.commit()

                sleep(freq_sec)
            except:
                continue
