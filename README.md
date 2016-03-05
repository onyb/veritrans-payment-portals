# Veritrans Payment Portals

This project is a pseudo backend application which lets users search
and list payment gateway details conveniently. It is a part of
HackerEarth's Veritrans backend programming challenge.

#### Sample Payment Portal data

```js
{
  "id": "7",
  "name": "Stripe",
  "image": "http://www.commercegurus.com/wp-content/uploads/2014/09/Stripe-Logo.png",
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
 
#### API documentation
- `GET /api`
  - API root - returns a 400 error
  - e.g. [/api](http://immense-stream-97040.herokuapp.com/api)
- `POST /api/payments`
  - Endpoint to validate and add payment data through POST request
  
- `GET /api/payments/list`
  - Returns a JSON containing all payment details, paginated by 3 results per page by default.
  - e.g. [/api/payments/list](http://immense-stream-97040.herokuapp.com/api/payments/list)
  - Accepts query parameters `page` and `limit` for custom pagination.
  - e.g. [/api/payments/list?limit=2](http://immense-stream-97040.herokuapp.com/api/payments/list?limit=2)
  - e.g. [/api/payments/list?page=3](http://immense-stream-97040.herokuapp.com/api/payments/list?page=3)
  - e.g. [/api/payments/list?limit=2&page=3](http://immense-stream-97040.herokuapp.com/api/payments/list?limit=2&page=3)
- `GET /api/payments/search`
  - Perform search operations on various fields, with the `name` field being a full text search
  - e.g. [/api/payments/search?name=VT](http://immense-stream-97040.herokuapp.com/api/payments/search?name=VT)
  - Search results can be paginated just like in `/api/payments/list`
  - e.g. [/api/payments/search?name=VT&limit=2&page=2](http://immense-stream-97040.herokuapp.com/api/payments/search?name=VT&limit=2&page=2)
  - Search by currency
  - e.g. [/api/payments/search?currency=SGD](http://immense-stream-97040.herokuapp.com/api/payments/search?currency=SGD)
  - Full text search and currency search can be performed together, along with optional pagination
  - e.g. [/api/payments/search?currency=INR&name=stripe](http://immense-stream-97040.herokuapp.com/api/payments/search?currency=INR&name=stripe)
  

#### Tech Stack
- Python 3 (tested on 3.5.1)
- Flask for the web application and API
- MongoDB for the backend database
- Flask-PyMongo, a wrapper around PyMongo
- Gunicorn as the WSGI HTTP server
- Heroku for deployement

#### Contributing
Once the challenge is over, I will switch to a public domain license, so that it
can be reused for bigger projects without second thoughts. The project can be
used as a boilerplate for applications based on Flask and MongoDB.
