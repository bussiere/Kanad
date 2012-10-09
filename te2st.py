
def ensurefirstuser(firstname, lastname, email, password):
	users = db(db.auth_user.email == email).select()
	if users:
		user_id = users[0].id
		created = False
		if settings.debug_ensure_first_user == True:
			print ('found user_id so created equals %s') % created
		return (user_id, created)

	else:
		my_crypt = CRYPT(key=auth.settings.hmac_key)
		crypt_pass = my_crypt(password)[0]		
		id_user = db.auth_user.insert(
							  	 first_name=firstname,
							  	 last_name=lastname,
							  	 email=email,
							  	 password=crypt_pass
							  							  	 )
		created = True
		if settings.debug_ensure_first_user == True:
			print ('creating user_id')
		return (id_user, created)

		


def ensure_users():
	user_id, created = _ensure_user('first', 'last', 'email@address.com', 'UserPassword12345')
	if settings.debug_ensure_users == True:
		print ('user id %i') % user_id
		print ('created %s') % created

def ensure_group_role(role, description):
	if not auth.id_group(role=role):	
		auth.add_group(role=role, description=description)	
		if settings.debug_ensure_group_role == True:
			print ('created role %s') % (role)

def ensure_membership(group_id, user_id):
	return_group_id = auth.add_membership(role=role, user_id=user_id)
	if settings.debug_ensure_membership == True:
		print ('made user_id member of %s') % (role)
	return return_group_id
 
def ensure_permissions(role, description, user_id):
	ensure_group_role(role, description)
	return_group_id = ensure_membership(group_id, user_id)
	if settings.debug_ensure_permissions == True:
		print return_group_id
