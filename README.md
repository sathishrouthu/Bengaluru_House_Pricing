# Bengaluru House Price Prediction

It is a Machine learning based regression project that predicts the price of a house in bangalore with given parameters.
Flask is used for the server side API and deployed on heroku to get the predicted price value.
The input parameters will be sent as a post request and the response to the client will be given in a json format.
Front end is built by using HTML, CSS, JavaScript & JQuery. 

* Deployed Web application link :   <a href = "https://bangalore-house-prices.netlify.app/"> https://bangalore-house-prices.netlify.app/ </a>


* Flask API End Point

<a href = "https://bengaluru-house-prices.herokuapp.com/predict_home_price"> https://bengaluru-house-prices.herokuapp.com/predict_home_price </a>

It accepts a POST Request with 4 input values : total_sqft , bhk, bath, location

It returns a response in json format 
```
{
  estimated_price : 93.5;
}
```


 


