# SNS  

This is a service that provides basic functions of SNS.  

## Functions

In this *SNS*, the following functions are implemented by default.  
Please add additional functions if necessary.

* Blog post & display function
![sns](https://user-images.githubusercontent.com/38198918/50765746-3a217900-12ba-11e9-8dde-54c4e9e93611.png)

	* You can use the Markdown language
	* Pagination is supported
	* Other users can post comments on posted blogs
* User management function
![sns_-_login](https://user-images.githubusercontent.com/38198918/50765868-9be1e300-12ba-11e9-9358-3ce54567fea3.png)
	* User creation
	* User authentication 
	* Email confirmation
* User Role Management
	* User
		* Basic permissions to write articles and comments and this other users.
	* Moderator
		* Adds permission to moderate comments made by other users.
	* Administrator
		* Full access, which includes permission to change the roles of other users.

* User follow function
* REST API

## Dependency

Please refer to requirements/common.txt for dependencies necessary to activate SNS.

## Setup

```
$git clone https://github.com/shosato0306/SNS.git
$cd SNS
$pip install -r requirements/dev.txt
$flask db init
$flask db migrate
$flask db upgrade
$flask shell
>>> Role.insert_roles()
>>> Role.query.all()
>>> exit()
$export FLASK_APP=sns.py
$export SNS_ADMIN=<Administrator's email address>
$export MAIL_USERNAME=<Mail account username>
$export MAIL_PASSWORD=<Mail account password>
$flask run
```

## Usage

## Contribution
1. Fork this repository
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am ‘Add some feature’)
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## Licence
This software is released under the MIT License.

