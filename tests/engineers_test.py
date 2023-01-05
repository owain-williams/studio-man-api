from engineers import Engineer, getallengineers, getengineerbyid
from decimal import Decimal
from pytest import approx


def test_createengineer():
    '''Test creating an engineer.'''
    # create an engineer
    test_engineer = Engineer(None, 'John', 'Doe', 123.45)
    # commit the engineer
    test_engineer.commit()
    # assert that the engineer was added
    retrieved_engineer = getengineerbyid(test_engineer.EngineerID)
    assert retrieved_engineer.FirstName == 'John'
    assert retrieved_engineer.LastName == 'Doe'
    assert retrieved_engineer.Rate == Decimal('123.45')
    # delete the engineer
    retrieved_engineer.delete()


def test_readengineer():
    '''Test reading an engineer.'''
    # create an engineer
    test_engineer = Engineer(None, 'John', 'Doe', 123.45)
    # commit the engineer
    test_engineer.commit()
    # assert that engineer was added by searching for it's ID
    assert test_engineer.EngineerID in [
        engineer.EngineerID for engineer in getallengineers()]


def test_updateengineer():
    # create an engineer
    test_engineer = Engineer(None, 'John', 'Doe', 123.45)
    # commit the engineer
    test_engineer.commit()
    # update the engineer's first name
    test_engineer.FirstName = 'Jane'
    test_engineer.commit()
    # assert that the engineer's first name was updated
    fn_retrieved_engineer = getengineerbyid(test_engineer.EngineerID)
    assert fn_retrieved_engineer.FirstName == 'Jane'
    # update the engineer's last name
    test_engineer.LastName = 'Smith'
    test_engineer.commit()
    # assert that the engineer's last name was updated
    ln_retrieved_engineer = getengineerbyid(test_engineer.EngineerID)
    assert ln_retrieved_engineer.LastName == 'Smith'
    # delete the engineer
    test_engineer.delete()


def test_deleteengineer():
    # create an engineer
    test_engineer = Engineer(None, 'John', 'Doe', 123.45)
    # commit the engineer
    test_engineer.commit()
    # delete the engineer
    test_engineer.delete()
    # assert that the engineer was deleted
    assert test_engineer.EngineerID not in [
        engineer.EngineerID for engineer in getallengineers()]


def test_setengineerrate():
    # create an engineer
    test_engineer = Engineer(None, 'John', 'Doe', 123.45)
    # commit the engineer
    test_engineer.commit()
    # set the engineer's rate
    test_engineer.setrate(234.56)
    # assert that the engineer's rate was set
    retrieved_engineer = getengineerbyid(test_engineer.EngineerID)
    assert retrieved_engineer.Rate == approx(Decimal('234.56'))
    # delete the engineer
    test_engineer.delete()
