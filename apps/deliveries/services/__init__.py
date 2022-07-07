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

                Delivery.query.delete()
                db.session.commit()

                rows_to_insert = list()

                for row in sheet.extract_table():
                    usd = float(row[1])
                    rows_to_insert.append(Delivery(number=row[0],
                                                   cost_usd=usd,
                                                   cost_rub=round(usd * usd_rate, 2),
                                                   term="-".join(reversed(row[2].split(".")))
                                                   )
                                          )

                db.session.add_all(rows_to_insert)
                db.session.commit()

                print("Delivery-DB has been successfully updated!")

                sleep(freq_sec)
            except:
                continue
