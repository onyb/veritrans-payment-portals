# Veritrans Payment Portals

This project is a pseudo backend application which lets users search
and list payment gateway details conveniently. It is a part of HackerEarth's Veritrans
backend programming challenge.

#### Sample Payment Portal data

```js
{
  "id": "7",
  "name": "Stripe",
  "image": "http://hackerearth.0x10.info/api/img?img=http://www.commercegurus.com/wp-content/uploads/2014/09/Stripe-Logo.png",
  "description": "Stripe is a suite of APIs that powers commerce for businesses of all sizes.",
  "branding": "1",
  "rating": "4.1",
  "currencies": "USD, AUD, CAD, GDP, EUR, INR",
  "setup_fee": "0",
  "transaction_fees": "2.9% + 0.30$",
  "how_to_url": "https://stripe.com/docs/checkout/tutorial"
}
```

#### Features implemented
- Full text search on `name` field, powered by MongoDB
- Search by currencies
- Pagination of response to 3 items per page
- Page size can be modified using query params
- Sort by `rating`
- Deployed using Heroku, and mLab
- API endpoints implemented are `/api/payments/list`, `/api/payments/count`, and `/api/payments/search`

#### Tech Stack
- Python 3 (tested on 3.5.1)
- Flask for the web application and API
- MongoDB for the backend database
- Flask-PyMongo, a wrapper around PyMongo
- Gunicorn as the WSGI HTTP server
- Heroku for deployement

#### API documentation
TODO

#### Contributing
Once the challenge is over, I will switch to a public domain license, so that it
can be reused for bigger projects without second thoughts. The project can be
used a boilerplate for applications using Flask and MongoDB.
