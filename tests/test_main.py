from app.main import app

def test_health():
    tester = app.test_client()
    response = tester.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {'status': 'ok'}
