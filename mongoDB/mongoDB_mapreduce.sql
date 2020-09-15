> book1 = {name : "Understanding JAVA", pages : 100}  
{ "name" : "Understanding JAVA", "pages" : 100 }
> book2 = {name : "Understanding JSON", pages : 200}  
{ "name" : "Understanding JSON", "pages" : 200 }
>  db.books.save(book1)  
WriteResult({ "nInserted" : 1 })
> db.books.save(book2)  
WriteResult({ "nInserted" : 1 })
> db.books.find()
{ "_id" : ObjectId("5f602c9fac2f56ef907abee2"), "name" : "Understanding JAVA", "pages" : 100 }
{ "_id" : ObjectId("5f602ca7ac2f56ef907abee3"), "name" : "Understanding JSON", "pages" : 200 }
> db.books.find();
{ "_id" : ObjectId("5f602c9fac2f56ef907abee2"), "name" : "Understanding JAVA", "pages" : 100 }
{ "_id" : ObjectId("5f602ca7ac2f56ef907abee3"), "name" : "Understanding JSON", "pages" : 200 }
> book = {name : "Understanding XML", pages : 300}  
{ "name" : "Understanding XML", "pages" : 300 }
> db.books.save(book)  
WriteResult({ "nInserted" : 1 })
> db.books.save(book)  
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> book = {name : "Understanding Web Services", pages : 400} 
{ "name" : "Understanding Web Services", "pages" : 400 }
> db.books.save(book)
WriteResult({ "nInserted" : 1 })
> book = {name : "Understanding Axis2", pages : 150}  
{ "name" : "Understanding Axis2", "pages" : 150 }
> db.books.save(book)
WriteResult({ "nInserted" : 1 })
> var map = function(){
... var category ;
... if ( this.pages >= 250 )
... category = "Big Books";
... else 
... category = "Small Books";
... emit( category,{name:this.name});
... };
> var reduce = function(key,values) {
... var sum = 0;
... values.forEach(function(doc) {
... sum += 1;
... });
... return {books:sum};
... };
> var count = db.books.mapReduce(map,reduce,{out:"book_results"});
> db[cou
CountDownLatch  count
> db[count.
count.constructor             count.propertyIsEnumerable(
count.convertToSingleObject(  count.result
count.counts                  count.timeMillis
count.drop(                   count.toLocaleString(
count.find(                   count.toString(
count.hasOwnProperty(         count.valueOf(
count.ok
> db[count.result].find();
{ "_id" : "Big Books", "value" : { "books" : 2 } }
{ "_id" : "Small Books", "value" : { "books" : 3 } }
