Situation: 

 

Company provides a parcel locker service.

We need a simple Python webservice that would allow us to work with 2 entities:

parcel – a parcel to be delivered. You can decide the fields to describe the parcel, what makes sense in your opinion.
parcel_locker – again, feel free to pick the fields which are relevant in your opinion.


Parcel is supposed to have at least information about the sender, receiver, size of the parcel (e.g. XS/S/M/L/XL), information about the locker it’s stored at.

Locker would require information about relevant sizes (see parcel), status of the locker, address of a locker.

 

We need REST API methods for CRUD operations on parcels and parcel lockers.

Methods should persist data in database (any of your choice). Implement validations that would be appropriate. 

 

You can use Python web development framework of your choice.

Follow good API development practices which you consider relevant in this case.

 

If you got time, having a front-end implementation for this is a bonus, but you can skip that part.