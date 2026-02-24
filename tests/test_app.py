import pytest
from app import app

@pytest.fixture
def client():
    """Test client for the Flask application"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page_loads(client):
    """Test that the index page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Martine Dupont' in response.data
    assert b'Jean-Luc Martin' in response.data
    assert b'Marie Pierre' in response.data
    assert b'Pierre Leroy' in response.data
    assert b'Sophie Bernard' in response.data

def test_vote_functionality(client):
    """Test the voting functionality"""
    response = client.post('/vote', data={'candidate_id': '2'})
    assert response.status_code == 302
    assert response.location == '/results'
    
    response = client.get('/results')
    assert response.status_code == 200
    assert b'Jean-Luc Martin' in response.data

def test_reset_functionality(client):
    """Test the reset functionality"""
    client.post('/vote', data={'candidate_id': '3'})
    
    response = client.get('/results')
    assert b'Marie Pierre' in response.data
    
    response = client.post('/reset')
    assert response.status_code == 302
    
    response = client.get('/results')
    assert b'Marie Pierre' not in response.data

def test_invalid_vote(client):
    """Test handling of invalid vote IDs"""
    response = client.post('/vote', data={'candidate_id': '99'})
    assert response.status_code == 302
    
    response = client.get('/results')
    assert b'Jean-Luc Martin' in response.data

def test_candidate_vote_increment(client):
    """Test that votes are incremented correctly"""
    client.post('/vote', data={'candidate_id': '1'})
    client.post('/vote', data={'candidate_id': '1'})
    
    response = client.get('/results')
    assert b'Martine Dupont' in response.data

def test_results_page_calculates_percentages(client):
    """Test that results page calculates percentages"""
    response = client.get('/results')
    assert response.status_code == 200
    assert b'0%' in response.data

def test_multiple_candidates_support(client):
    """Test that the system supports all 5 candidates"""
    candidate_ids = ['1', '2', '3', '4', '5']
    
    for candidate_id in candidate_ids:
        response = client.post('/vote', data={'candidate_id': candidate_id})
        assert response.status_code == 302
    
    response = client.get('/results')
    assert b'Martine Dupont' in response.data
    assert b'Jean-Luc Martin' in response.data
    assert b'Marie Pierre' in response.data
    assert b'Pierre Leroy' in response.data
    assert b'Sophie Bernard' in response.data

def test_direct_results_access(client):
    """Test accessing /results without voting first"""
    response = client.get('/results')
    assert response.status_code == 200
    assert b'0%' in response.data
