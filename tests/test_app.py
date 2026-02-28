import os
import pytest
from flask import Flask
from app import MinistryOfInteriorApp, app

def create_test_app():
    """Create a new Flask app instance for testing"""
    test_app = Flask('test_app', template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
    ministry_app = MinistryOfInteriorApp()
    ministry_app.app = test_app
    ministry_app.init_app()
    return test_app, ministry_app

@pytest.fixture
def fresh_client():
    """Get a fresh test client with routes initialized"""
    test_app, ministry_app = create_test_app()
    test_app.config['TESTING'] = True
    with test_app.test_client() as client:
        yield client

def test_index_page_loads(fresh_client):
    """Test that the index page loads successfully"""
    response = fresh_client.get('/')
    assert response.status_code == 200
    assert b'Martine Dupont' in response.data
    assert b'Jean-Luc Martin' in response.data
    assert b'Marie Pierre' in response.data
    assert b'Pierre Leroy' in response.data
    assert b'Sophie Bernard' in response.data

def test_vote_functionality(fresh_client):
    """Test the voting functionality"""
    response = fresh_client.post('/vote', data={'candidate_id': '2'})
    assert response.status_code == 302
    assert response.location == '/results'
    response = fresh_client.get('/results')
    assert response.status_code == 200
    assert b'Jean-Luc Martin' in response.data

def test_reset_functionality(fresh_client):
    """Test the reset functionality"""
    fresh_client.post('/vote', data={'candidate_id': '3'})
    response = fresh_client.get('/results')
    assert b'1 votes' in response.data
    reset_response = fresh_client.post('/reset')
    assert reset_response.status_code == 302
    response = fresh_client.get('/results')
    assert b'0 votes' in response.data

def test_invalid_vote(fresh_client):
    """Test handling of invalid vote IDs"""
    response = fresh_client.post('/vote', data={'candidate_id': '99'})
    assert response.status_code == 302
    response = fresh_client.get('/results')
    assert b'Jean-Luc Martin' in response.data

def test_candidate_vote_increment(fresh_client):
    """Test that votes are incremented correctly"""
    fresh_client.post('/vote', data={'candidate_id': '1'})
    fresh_client.post('/vote', data={'candidate_id': '1'})
    response = fresh_client.get('/results')
    assert b'Martine Dupont' in response.data

def test_results_page_calculates_percentages(fresh_client):
    """Test that results page calculates percentages"""
    response = fresh_client.get('/results')
    assert response.status_code == 200
    assert b'0%' in response.data

def test_multiple_candidates_support(fresh_client):
    """Test that the system supports all 5 candidates"""
    candidate_ids = ['1', '2', '3', '4', '5']
    for candidate_id in candidate_ids:
        response = fresh_client.post('/vote', data={'candidate_id': candidate_id})
        assert response.status_code == 302
    response = fresh_client.get('/results')
    assert b'Martine Dupont' in response.data
    assert b'Jean-Luc Martin' in response.data
    assert b'Marie Pierre' in response.data
    assert b'Pierre Leroy' in response.data
    assert b'Sophie Bernard' in response.data

def test_direct_results_access(fresh_client):
    """Test accessing /results without voting first"""
    response = fresh_client.get('/results')
    assert response.status_code == 200
    assert b'0%' in response.data