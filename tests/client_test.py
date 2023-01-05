from client import Client, getallclients

def test_add_del_client():
    new_client = Client(None, 'John', 'Doe')
    new_client.commit()
    
    # assert that the client was added
    
    clients = getallclients()
    
    assert len(clients) == 1
    assert clients[0].ContactFirstName == 'John'
    assert clients[0].ContactLastName == 'Doe'
    
    new_client.delete()
    del new_client

