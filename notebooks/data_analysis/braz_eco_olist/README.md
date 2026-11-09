# About the data

this data is from a brazilian e-commerce data of orders from olist store
the data is devided as follows :

![DATA SCHEMA](./HRhd2Y0.png)

Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers

### Business Scenario:

You are hired as a data analyst by an e-commerce company Olist. Management wants to understand why customers are dissatisfied and how delivery performance can improve.

Questions to investigate:

1. Which product categories generate the most revenue?
2. Which states generate the most orders?
3. What percentage of orders arrive late?
4. Does delivery delay correlate with lower review scores?
5. Which customers make repeat purchases?
6. Which sellers have the worst delivery performance?
7. which delivery partners have the most delayed delivery time?
8. in lower review orders , is the delay most comes from the seller or the delivery partner ?

## Definitions:

**Customer dataset :**

- customer_id :
  key to the orders dataset. Each order has a unique customer_id.

- ustomer_unique_id :
  unique identifier of a customer.

- customer_zip_code_prefix:
  first five digits of customer zip code

- customer_city :
  customer city name

- customer_state :
  customer state

**Geolocation Dataset :**
This dataset has information of Brazilian zip codes and its lat/lng coordinates. Use it to plot maps and find distances between sellers and customers.

- geolocation_zip_code_prefix :
  first 5 digits of zip code

- geolocation_lat :
  latitude

- geolocation_lng :
  longitude

- geolocation_city :
  city name

- geolocation_state :
  state

**Order Items Dataset :**
This dataset includes data about the items purchased within each order.

- order_item_id :
  sequential number identifying number of items included in the same order.

- shipping_limit_date :
  Shows the seller shipping limit date for handling the order over to the logistic partner.

- freight_value :
  item freight value item (if an order has more than one item the freight value is splitted between items)

**Payments Dataset :**

- payment_sequential :
  a customer may pay an order with more than one payment method. If he does so, a sequence will be created to accommodate all

- payment_type :
  method of payment chosen by the customer.

- payment_installments :
  number of installments chosen by the customer.

- payment_value :
  transaction value.

**Order Reviews :**

- review_score :
  Note ranging from 1 to 5 given by the customer on a satisfaction survey.

- review_creation_date
  Shows the date in which the satisfaction survey was sent to the customer.

- review_answer_timestamp :
  Shows satisfaction survey answer timestamp.

**Order Dataset :**

- order_status :
  Reference to the order status (delivered, shipped, etc).

- order_purchase_timestamp :
  Shows the purchase timestamp.

- order_approved_at
  Shows the payment approval timestamp.

- order_delivered_carrier_date :
  Shows the order posting timestamp. When it was handled to the logistic partner.

- order_delivered_customer_date :
  Shows the actual order delivery date to the customer.

- order_estimated_delivery_date :
  Shows the estimated delivery date that was informed to customer at the purchase moment.

**Products :**

- product_category_name :
  root category of product, in Portuguese.

- product_name_lenght :
  number of characters extracted from the product name.

- product_description_lenght :
  number of characters extracted from the product description.

- product_photos_qty :
  number of product published photos

- product_weight_g :
  product weight measured in grams.

- product_length_cm :
  product length measured in centimeters.

- product_height_cm :
  product height measured in centimeters.

- product_width_cm :
  product width measured in centimeters.

**Sellers :**

- seller_zip_code_prefix :
  first 5 digits of seller zip code

- seller_city :
  seller city name

- seller_state :
  seller state

**Category Name Translation :**

- product_category_name :
  category name in Portuguese

- product_category_name_english :
  category name in English
