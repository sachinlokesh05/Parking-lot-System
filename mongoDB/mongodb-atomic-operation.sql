/* Model Data for Atomic Operations */

/* The recommended approach to maintain atomicity would be to keep all the related information, 
which is frequently updated together in a single document using embedded documents. 
This would make sure that all the updates for a single document are atomic. */

>db.createCollection("products")
>db.productDetails.insert(
	{
		"_id":1,
		"product_name": "Samsung S3",
		"category": "mobiles",
		"product_total": 5,
		"product_available": 3,
		"product_bought_by": [
			{
				"customer": "john",
				"date": "7-Jan-2014"
			},
			{
				"customer": "mark",
				"date": "8-Jan-2014"
			}
		]
	}
)

>db.products.findAndModify({ 
   query:{_id:2,product_available:{$gt:0}}, 
   update:{ 
      $inc:{product_available:-1}, 
      $push:{product_bought_by:{customer:"rob",date:"9-Jan-2014"}} 
   }    
})

/* Our approach of embedded document and using findAndModify query makes sure 
that the product purchase information is updated only if it the product is available. 
And the whole of this transaction being in the same query, is atomic.*/
