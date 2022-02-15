import starkbank


def webhooksite():
    webhook = starkbank.webhook.create(
        url="https://webhook.site/117b85f8-2b69-4325-8c54-0d0f5eb8f0c2?",
        subscriptions=["invoice"],
    )

    print(webhook)
    return webhook

'''

response = listen()  # this is the method you made to get the events posted to your webhook endpoint

event = starkbank.event.parse(
    content=response.data.decode("utf-8"),
    signature=response.headers["Digital-Signature"],
)

if event.subscription == "transfer":
    print(event.log.transfer)

elif event.subscription == "boleto":
    print(event.log.boleto)

elif event.subscription == "boleto-payment":
    print(event.log.payment)

elif event.subscription == "boleto-holmes":
    print(event.log.holmes)

elif event.subscription == "brcode-payment":
    print(event.log.payment)

elif event.subscription == "utility-payment":
    print(event.log.payment)

elif event.subscription == "deposit":
    print(event.log.deposit)

elif event.subscription == "invoice":
    print(event.log.invoice)

'''