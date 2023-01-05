from client import Client, get_all_clients

new_client = Client(None, 'John', 'Doe')

new_client.commit()
print(get_all_clients())
new_client.delete()
print(get_all_clients())