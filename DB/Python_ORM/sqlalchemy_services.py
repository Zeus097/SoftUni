from models import Session, User, Order





# # ADDING a new user to the database
#
# with Session() as session:
#     new_user = User(
#         username='john_doe',
#         email='john@example.com'
#     )
#
#     session.add(new_user)
#     session.commit()





# # RETREIVING all the data from a table
#
# with Session() as session:
#     users = session.query(User).all()
#     for user in users:
#         print(user.username, user.email)





# #  UPDATING a record from the database as retrieving it with 'filter_by' the first matching record
#
# with Session() as session:
#     user_to_update = session.query(User).filter_by(username='john_doe').first()
#
#     if user_to_update:
#         user_to_update.email = 'new_email@example.com'
#         session.commit()
#         print("User updated successfully")
#     else:
#         print("User not found")




# #  DELETING a record
#
# with Session() as session:
#     user_to_delete = session.query(User).filter_by(username='john_doe').first()
#
#     if user_to_delete:
#         session.delete(user_to_delete)  # MARKING FOR DELETION
#
#         session.commit()  # COMPLETE DELETION PROCESS
#
#         print("User deleted successfully")
#     else:
#         print("User not found")



# # CREATING A SESSION
#
# session = Session()
#
# try:
#     session.begin()
#     session.query(User).delete()
#     session.commit()
#     print("All users deleted successfully")
#
# except Exception as e:
#     session.rollback()
#     print("An error occurred", str(e))
#
# finally:
#     session.close()



# # Populating the new table
#
# with Session() as session:
#
#     session.add_all(
#         (
#             Order(user_id=2),
#             Order(user_id=4)
#         )
#     )
#
#     session.commit()




# with Session() as session:
#     orders = session.query(Order).order_by(Order.user_id.desc()).all()
#     if not orders:
#         print("No orders yet")
#     else:
#         for order in orders:
#             user = order.user
#             print(f"Order number {order.id}, Is completed: {order.is_completed}, Username: {user.username}")

