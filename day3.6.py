role=input('enter designation')
if role=='Admin':
    print('View all users')
    print('Add users')
    print('Remove users')
elif role =='Developer':
    print('Create APIs')
    print('Manage API ')
elif role =="DBA":
    print('Write queries for database')
    print('Maintain database')
elif role=="Client":
    print('View profile')
    print('Edit and manage posts')
else:
    print('Invalid Role please contact manager or support team')
    
