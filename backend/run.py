from IPython import embed
from application.app import app
import traceback
import logging

if __name__ == '__main__':
    try:
        app.run(debug=True, use_reloader=False)
    except:
        logging.error(traceback.format_exc())
