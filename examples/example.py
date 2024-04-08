from FinPay import FinPayAPI, FinPayInvoice

api = FinPayAPI(1337,
                '*****',
                '*****',)

invoice: FinPayInvoice = api.create_invoice("Invoice-123", "Just description.", 999, "card_cis", "RU", "RUB")

print(invoice.check_status())
print(invoice)
print(invoice.url)

invoice.cancel_invoice()
