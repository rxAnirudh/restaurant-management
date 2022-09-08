# Multi Vendor Restaurant
- Created multi vendor project in which vendors can register there restaurant and do business online and get access to all details they need using admin panel.

### Admin panel
<img src="https://github.com/RxMobile-Dummy/django-taskmanager/blob/main/media/admin-panel.gif" />


#### Features

- ##### Admin Users Can
  - Manage Category (Add, Update, Filter and Delete).
  - Manage Products (Add, Update, Filter and Delete).
  - Manage Users (Update, Filter and Delete).
  - Manage Orders (View and Process).
   
    
- ##### Vendors Can
  - Add Products.
  - Update Profile.
  - Gets Notification When an Order is made by Users.
  - Get Orders and Manage Them.
  
    
- ##### Users Can 
  - Add to Cart.
  - Pay with Debit/Credit Card and Order.
  - While Checkout, User should give the address to deliver.
  - Get Email Notification about the confirmation of the order.
  

#### App Architecture :

A typical architecture of our Django app in development looks like this:

<img src="https://miro.medium.com/max/646/1*-PPNwQaTjVDViOM_xZzSwg.png" width="500" style="max-width:500%;">

So we can identify 3 main components:

 - Model: This handles your data representation, it serves as an interface to the data stored in the database itself, and also allows you to interact with your data without having to get perturbed with all the complexities of the underlying database.

 - View: This component includes the core logic of all APIs (Application programming interface)

 - Controller: provides the logic to either handle presentation flow in the view or update the model’s data i.e it uses programmed logic to figure out what is pulled from the database through the model and passed to the view,also gets information from the user through the view and implements the given logic by either changing the view or updating the data via the model , To make it more simpler, see it as the engine room.

#### Project Structure

```sh
.
├── accounts
├── customers
├── foodOnline_main
│   ├── static
│   │   ├── css
│   │   ├── extra-images
│   │   ├── fonts
│   │   ├── images
│   │   ├── js
│   │   └── logo
├── marketplace
├── media
│   ├── foodimages
│   └── vendor
│       └── license
├── menu
├── orders
├── static
│   ├── admin
│   │   ├── css
│   │   │   ├── vendor
│   │   │   │   └── select2
│   │   ├── fonts
│   │   ├── img
│   │   │   ├── gis
│   │   └── js
│   │       ├── admin
│   │       ├── vendor
│   │       │   ├── jquery
│   │       │   ├── select2
│   │       │   └── xregexp
│   ├── css
│   ├── extra-images
│   ├── fonts
│   ├── gis
│   │   ├── css
│   │   ├── img
│   │   └── js
│   ├── images
│   ├── js
│   └── logo
├── templates
│   ├── accounts
│   │   ├── emails
│   ├── customers
│   ├── includes
│   ├── marketplace
│   ├── orders
│   ├── vendor
├── vendor
```

#### Command to create a new Django Project : 
```sh
django-admin startproject mysite
```

#### Command to create new django App : 
```sh
python manage.py startapp polls
```

#### Command to run django App : 
```sh
python manage.py runserver
```
#### Command to migrate your django code : (run when made database level changes in your models) 
```sh
python manage.py migrate
python manage.py makemigratons
```
