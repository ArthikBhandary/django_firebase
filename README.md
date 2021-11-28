#Testing

##Installing requirements
Making use of virtual environments suggested
>pip install virtualenv
> 
> virtualenv myenv
> 
> source activate myenv/bin/activate

Install the requirements
>pip install -r requirements.txt

## Set up gmail to send confirmation email

Go to settings.py and update the last two line/variables. (EMAIL_HOST_USER and EMAIL_HOST_PASSWORD)
>EMAIL_HOST_USER = "example@gmail.com"
>
>EMAIL_HOST_PASSWORD = "password"

## Run it on the local server

> python manage.py runserver


Then open [127.0.0.1:8000](127.0.0.1:8000) in a browser

