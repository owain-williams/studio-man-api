from models.client import Client, getallclients, getoneclient, getclientsbylastname


def test_createclient():
    # create a client
    test_client = Client(None, 'John', 'Doe')
    # commit the client
    test_client.commit()
    # assert that the client was added
    retrieved_client = getoneclient(test_client.ClientID)
    assert retrieved_client.ContactFirstName == 'John'
    assert retrieved_client.ContactLastName == 'Doe'
    # delete the client
    test_client.delete()


def test_readclient():
    # create a client
    test_client = Client(None, 'John', 'Doe')
    # commit the client
    test_client.commit()
    # assert that client was added by searching for it's ID
    assert test_client.ClientID in [
        client.ClientID for client in getallclients()]

def test_updateclient():
    # create a client
    test_client = Client(None, 'John', 'Doe')
    # commit the client
    test_client.commit()
    # update the client's first name
    test_client.ContactFirstName = 'Jane'
    test_client.commit()
    # assert that the client's first name was updated
    fn_retrieved_client = getoneclient(test_client.ClientID)
    assert fn_retrieved_client.ContactFirstName == 'Jane'
    # update the client's last name
    test_client.ContactLastName = 'Smith'
    test_client.commit()
    # assert that the client's last name was updated
    ln_retrieved_client = getoneclient(test_client.ClientID)
    assert ln_retrieved_client.ContactLastName == 'Smith'
    # delete the client
    test_client.delete()
    
def deleteclient():
    # create a client
    test_client = Client(None, 'John', 'Doe')
    # commit the client
    test_client.commit()
    # delete the client
    retrieved_client = getoneclient(test_client.ClientID)
    assert retrieved_client.ClientID in [
        client.ClientID for client in getallclients()]
    # assert that the client was deleted
    assert test_client.ClientID not in [
        client.ClientID for client in getallclients()]
    