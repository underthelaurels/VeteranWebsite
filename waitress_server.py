from waitress import serve

import veteran_connect

app = veteran_connect.create_app()
serve(app, host='0.0.0.0', port='80')
