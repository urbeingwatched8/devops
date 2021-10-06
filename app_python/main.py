from fastapi import FastAPI
import datetime
from fastapi.middleware.wsgi import WSGIMiddleware
from api import router
from configurations.wsgi import get_wsgi_application
import os
from fastapi.responses import StreamingResponse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "composeexample.settings")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    
django_app = get_wsgi_application()
now = datetime.datetime.now().strftime('%H:%M:%S')
app1 = FastAPI()
app.mount('/static',
    StaticFiles(
         directory=os.path.normpath(
              os.path.join(find_spec('django.contrib.admin').origin, '..', 'static')
         )
   ),
   name='static',
)
some_file_path="visit_logs/visits.txt"

#fastapi used following the advices from docs: https://fastapi.tiangolo.com/advanced/custom-response/


@app1.get("/visits")
def main_visits():
    def iterfile():  
        with open(some_file_path, mode="rb") as file_like:  
            answer=file_like.read()  
    return answer #StreamingResponse(iterfile()), media_type="video/mp4")
    
async def visits_time(now):
    with open("visit_logs/visits.txt", "a") as file_llike:
        file_llike.write("\n")
        file_llike.write(now)

app1.mount('/', WSGIMiddleware(django_app))
visits_time(now)
