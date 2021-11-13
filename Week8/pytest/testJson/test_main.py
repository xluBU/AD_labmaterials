from Unittests.Pytestexample.testJson import main
from flask import json

def test_add():
    main.app.testing = True
    client = main.app.test_client()

    response = client.post(
        '/add',
        data=json.dumps({'a': 1, 'b': 2}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['sum'] == 3